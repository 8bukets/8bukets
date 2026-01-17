
import asyncio
import time
from bs4 import BeautifulSoup
import functools

# A moderately complex HTML structure repeated to simulate a large page
SAMPLE_HTML = """
<article class="post">
    <h1 class="entry-title"><a href="http://example.com/post1">Sample Post Title</a></h1>
    <time class="entry-date" datetime="2023-01-01T12:00:00+00:00">January 1, 2023</time>
    <div class="author vcard"><span class="fn">Bolt</span></div>
    <div class="entry-content">
        <p>Some content with <a href="http://external.com">external link</a>.</p>
        <p>More text to parse.</p>
        <ul>
            <li>List item 1</li>
            <li>List item 2</li>
        </ul>
    </div>
</article>
""" * 500  # Repeat to make it heavy

async def parse_page_blocking(html):
    # Simulates the blocking behavior
    soup = BeautifulSoup(html, 'html.parser')
    return len(soup.find_all('article'))

async def parse_page_non_blocking(html):
    # Simulates the non-blocking behavior
    loop = asyncio.get_running_loop()
    # Using run_in_executor to offload to thread pool
    soup = await loop.run_in_executor(None, BeautifulSoup, html, 'html.parser')
    # Or cleaner with asyncio.to_thread in 3.9+
    # soup = await asyncio.to_thread(BeautifulSoup, html, 'html.parser')
    return len(soup.find_all('article'))

async def heartbeat(duration, interval=0.01):
    """
    Monitors event loop responsiveness.
    Returns the maximum delay observed between ticks.
    """
    start_time = time.time()
    max_delay = 0
    last_tick = start_time

    while time.time() - start_time < duration:
        await asyncio.sleep(interval)
        now = time.time()
        delay = (now - last_tick) - interval
        if delay > max_delay:
            max_delay = delay
        last_tick = now

    return max_delay

async def benchmark(parse_func, iterations=10):
    start = time.time()

    # Start heartbeat monitor for approx duration of the test
    # We don't know duration exactly, so we'll run it as a task and cancel it?
    # Or just run it alongside.

    # We run N concurrent parsing tasks
    tasks = [parse_func(SAMPLE_HTML) for _ in range(iterations)]

    # We also run a heartbeat task to measure loop blocking
    # The heartbeat task will run for a fixed time, but we want it to run while tasks are running.
    # We can wrapping tasks in gather, and measure loop lag.

    # Better approach:
    # Launch a background task that records loop lag.
    # Launch the workload.
    # Cancel background task when workload done.

    loop_monitor = asyncio.create_task(monitor_loop())

    await asyncio.gather(*tasks)

    loop_monitor.cancel()
    try:
        max_lag = await loop_monitor
    except asyncio.CancelledError:
        max_lag = 0 # Should have returned value before cancel if possible, but let's use a shared var

    return time.time() - start

# Shared variable for monitor
max_lag_observed = 0

async def monitor_loop():
    global max_lag_observed
    max_lag_observed = 0
    last_time = time.time()
    interval = 0.01
    try:
        while True:
            await asyncio.sleep(interval)
            now = time.time()
            lag = (now - last_time) - interval
            if lag > max_lag_observed:
                max_lag_observed = lag
            last_time = now
    except asyncio.CancelledError:
        return max_lag_observed

async def main():
    iterations = 20
    print(f"Benchmarking with {iterations} iterations on heavy HTML...")

    # Warmup
    await parse_page_blocking(SAMPLE_HTML)

    # Test Blocking
    global max_lag_observed
    max_lag_observed = 0
    start = time.time()
    monitor = asyncio.create_task(monitor_loop())

    tasks = [parse_page_blocking(SAMPLE_HTML) for _ in range(iterations)]
    await asyncio.gather(*tasks)

    monitor.cancel()
    duration_blocking = time.time() - start
    lag_blocking = max_lag_observed

    print(f"Blocking implementation:")
    print(f"  Total time: {duration_blocking:.4f}s")
    print(f"  Max Event Loop Lag: {lag_blocking:.4f}s")

    # Test Non-Blocking
    max_lag_observed = 0
    start = time.time()
    monitor = asyncio.create_task(monitor_loop())

    tasks = [parse_page_non_blocking(SAMPLE_HTML) for _ in range(iterations)]
    await asyncio.gather(*tasks)

    monitor.cancel()
    duration_non_blocking = time.time() - start
    lag_non_blocking = max_lag_observed

    print(f"Non-Blocking (Threaded) implementation:")
    print(f"  Total time: {duration_non_blocking:.4f}s")
    print(f"  Max Event Loop Lag: {lag_non_blocking:.4f}s")

if __name__ == "__main__":
    asyncio.run(main())
