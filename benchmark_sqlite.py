import sqlite3
import time
import os

DB_NAME = "benchmark.db"

def setup_db():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test (
                id INTEGER PRIMARY KEY,
                data TEXT
            )
        ''')

def test_separate_connections(n):
    start = time.time()
    for i in range(n):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO test (data) VALUES (?)", (f"data_{i}",))
            conn.commit()
    end = time.time()
    return end - start

def test_single_connection(n):
    setup_db() # Reset
    start = time.time()
    with sqlite3.connect(DB_NAME) as conn:
        for i in range(n):
            cursor = conn.cursor()
            cursor.execute("INSERT INTO test (data) VALUES (?)", (f"data_{i}",))
            conn.commit()
    end = time.time()
    return end - start

def test_single_connection_batched(n):
    setup_db() # Reset
    start = time.time()
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        for i in range(n):
            cursor.execute("INSERT INTO test (data) VALUES (?)", (f"data_{i}",))
        conn.commit()
    end = time.time()
    return end - start

def main():
    N = 1000
    setup_db()

    print(f"Benchmarking {N} inserts...")

    time_separate = test_separate_connections(N)
    print(f"Separate connections (commit each): {time_separate:.4f}s")

    time_single = test_single_connection(N)
    print(f"Single connection (commit each):    {time_single:.4f}s")

    time_batched = test_single_connection_batched(N)
    print(f"Single connection (batched commit): {time_batched:.4f}s")

    print(f"Speedup (Single vs Separate): {time_separate / time_single:.2f}x")
    print(f"Speedup (Batched vs Separate): {time_separate / time_batched:.2f}x")

    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

if __name__ == "__main__":
    main()
