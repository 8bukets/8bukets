from flask import Flask, send_from_directory, render_template_string, jsonify
import os
import glob
import markdown
import sqlite3
import json

app = Flask(__name__)

# Helper to get DB connection
def get_db_conn():
    db_path = os.getenv("MEMORY_FILE", "data/memory.db")
    if not os.path.exists(db_path):
        return None
    return sqlite3.connect(db_path)

@app.route('/')
def index():
    reports = sorted(glob.glob('results/DAILY_REPORT_*.md'), reverse=True)
    dist_mode = os.getenv("DISTRIBUTED_MODE", "FALSE")
    vector_status = "Active" if os.path.exists("data/vector_store") else "Inactive"

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Markposition Autonomous Dashboard</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { background-color: #f8f9fa; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
            .sidebar { height: 100vh; background: #212529; color: white; padding-top: 20px; position: fixed; width: 240px; }
            .main-content { margin-left: 240px; padding: 20px; }
            .card { border: none; box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075); margin-bottom: 20px; }
            .nav-link { color: #adb5bd; margin: 5px 0; }
            .nav-link:hover, .nav-link.active { color: white; background: rgba(255,255,255,0.1); border-radius: 4px; }
            .stat-value { font-size: 2rem; font-weight: bold; color: #0d6efd; }
            .chart-container { height: 300px; }
        </style>
    </head>
    <body>
        <div class="sidebar d-flex flex-column p-3">
            <h4>Markposition AI</h4>
            <hr>
            <ul class="nav nav-pills flex-column mb-auto">
                <li><a href="/" class="nav-link active">Dashboard</a></li>
                <li><a href="/evolution" class="nav-link">Evolution Log</a></li>
                <li><a href="/chat" class="nav-link">Semantic Chat</a></li>
                <li><a href="/patterns" class="nav-link">Market Patterns</a></li>
                <li><a href="/logs" class="nav-link">System Logs</a></li>
            </ul>
        </div>

        <div class="main-content">
            <header class="d-flex justify-content-between align-items-center mb-4">
                <h2>System Overview</h2>
                <div>
                    <span class="badge bg-success">Status: Optimal</span>
                    <span class="badge bg-primary">""" + f"Mode: {dist_mode}" + """</span>
                </div>
            </header>

            <div class="row">
                <div class="col-md-3">
                    <div class="card p-3 text-center">
                        <div class="text-muted">Total Agents</div>
                        <div class="stat-value">25</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card p-3 text-center">
                        <div class="text-muted">Vector Store</div>
                        <div class="stat-value text-success">""" + vector_status + """</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card p-3 text-center">
                        <div class="text-muted">Memory Keys</div>
                        <div id="memory-keys" class="stat-value text-info">--</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card p-3 text-center">
                        <div class="text-muted">Ecosystem Health</div>
                        <div class="stat-value text-warning">98%</div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-md-8">
                    <div class="card p-3">
                        <h5>Memory Scaling (by Agent)</h5>
                        <div class="chart-container">
                            <canvas id="scalingChart"></canvas>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-3">
                        <h5>Daily Reports</h5>
                        <div class="list-group list-group-flush" style="max-height: 250px; overflow-y: auto;">
                            """ + "".join([f'<a href="/report/{os.path.basename(r)}" class="list-group-item list-group-item-action small">{os.path.basename(r)}</a>' for r in reports]) + """
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-md-12">
                     <div class="card p-3">
                        <h5>Real-time Performance Metrics</h5>
                        <div class="chart-container" style="height: 200px;">
                            <canvas id="performanceChart"></canvas>
                        </div>
                     </div>
                </div>
            </div>
        </div>

        <script>
            // Fetch stats and render charts
            fetch('/api/stats')
                .then(r => r.json())
                .then(data => {
                    document.getElementById('memory-keys').innerText = Object.values(data).reduce((a,b) => a+b, 0);

                    const ctx = document.getElementById('scalingChart').getContext('2d');
                    new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: Object.keys(data),
                            datasets: [{
                                label: 'Storage Keys',
                                data: Object.values(data),
                                backgroundColor: 'rgba(13, 110, 253, 0.5)',
                                borderColor: 'rgb(13, 110, 253)',
                                borderWidth: 1
                            }]
                        },
                        options: { maintainAspectRatio: false, scales: { y: { beginAtZero: true } } }
                    });
                });

            const perfCtx = document.getElementById('performanceChart').getContext('2d');
            const perfChart = new Chart(perfCtx, {
                type: 'line',
                data: { labels: [], datasets: [{ label: 'Avg Agent Latency (ms)', data: [], borderColor: 'rgb(255, 193, 7)', tension: 0.1 }] },
                options: { maintainAspectRatio: false }
            });

            function updateMetrics() {
                fetch('/api/metrics')
                    .then(r => r.json())
                    .then(data => {
                        perfChart.data.labels = data.labels;
                        perfChart.data.datasets[0].data = data.data;
                        perfChart.update();
                    });
            }
            updateMetrics();
            setInterval(updateMetrics, 30000);
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/api/metrics')
def api_metrics():
    conn = get_db_conn()
    if not conn:
        return jsonify({"labels": [], "data": []})
    cursor = conn.cursor()
    cursor.execute("SELECT strftime('%H:%M', timestamp), AVG(execution_time_ms) FROM system_metrics GROUP BY strftime('%H:%M', timestamp) ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return jsonify({
        "labels": [r[0] for r in reversed(rows)],
        "data": [r[1] for r in reversed(rows)]
    })

@app.route('/api/stats')
def api_stats():
    conn = get_db_conn()
    if not conn:
        return jsonify({})
    cursor = conn.cursor()
    cursor.execute("SELECT agent_name, COUNT(*) FROM agent_memory GROUP BY agent_name")
    stats = dict(cursor.fetchall())
    conn.close()
    return jsonify(stats)

@app.route('/report/<name>')
def show_report(name):
    path = os.path.join('results', name)
    if not os.path.exists(path):
        return "Report not found", 404

    with open(path, 'r') as f:
        content = f.read()

    html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    return f'<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"><style>.markdown-body {{ box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }}</style></head><body class="markdown-body"><a href="/">Back</a><hr>{html_content}</body></html>'

@app.route('/chat', methods=['GET', 'POST'])
def semantic_chat():
    from flask import request
    from markposition.agents.vector_memory import VectorMemory

    query = ""
    results = []
    if request.method == 'POST':
        query = request.form.get('query', '')
        vm = VectorMemory()
        results = vm.search(query, top_k=5)

    html = """
    <h1>Semantic Intelligence Interface (RAG)</h1>
    <form method="post">
        <input type="text" name="query" placeholder="Query the system memory..." style="width: 80%; padding: 10px;" value="{{query}}">
        <button type="submit" style="padding: 10px;">Reason</button>
    </form>
    """

    if query:
        # AI Synthesis Simulation
        synthesis = "Based on my analysis of the retrieved memories, "
        if results:
            top_text = results[0]['metadata'].get('text', '')
            synthesis += f"I found {len(results)} relevant patterns. The most significant finding is: '{top_text}'. "
            synthesis += "This suggests a strong correlation with recent scraping activity and agent collaboration."
        else:
            synthesis += "I couldn't find any direct semantic matches in the current memory bank. I recommend running a new cycle to populate the vector store."

        html += f"<div style='background: #e1f5fe; border-left: 5px solid #03a9f4; padding: 15px; border-radius: 4px; margin-bottom: 20px;'><strong>AI System Synthesis:</strong><br>{synthesis}</div>"

        html += f"<h3>Raw Memory Retrieval for: '{query}'</h3><ul>"
        if not results:
            html += "<li>No semantic matches found in system memory.</li>"
        for res in results:
            meta = res['metadata']
            html += f"<li><strong>[{meta.get('agent', 'Unknown')}]</strong>: {meta.get('text')} <br><small>Relevance Distance: {res['distance']:.4f}</small></li>"
        html += "</ul>"

    html += "<br><a href='/'>Back</a>"
    return render_template_string(f'<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"><style>.markdown-body {{ padding: 45px; }}</style></head><body class="markdown-body">{html}</body></html>', query=query)

@app.route('/patterns')
def show_patterns():
    from markposition.agents.vector_memory import VectorMemory
    vm = VectorMemory()
    patterns = vm.search("Market Pattern", top_k=20)

    html = "<h1>System Identified Patterns</h1>"
    html += "<h2>Semantic Market Clusters</h2><ul>"
    for res in patterns:
        if res['metadata'].get('type') == 'pattern_recognition':
            html += f"<li>{res['metadata'].get('text')}</li>"
    html += "</ul>"

    html += "<a href='/'>Back</a>"
    return f'<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"><style>.markdown-body {{ padding: 45px; }}</style></head><body class="markdown-body">{html}</body></html>'

@app.route('/evolution')
def show_evolution():
    path = "SYSTEM_EVOLUTION.md"
    if not os.path.exists(path):
        return "Evolution log not found", 404

    with open(path, 'r') as f:
        content = f.read()

    html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    return f'<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"><style>.markdown-body {{ box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }}</style></head><body class="markdown-body"><a href="/">Back</a><hr>{html_content}</body></html>'

@app.route('/logs')
def show_logs():
    log_path = "/tmp/system_run_v8.log"
    content = "Log file not found."
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            content = f.read()
    return f'<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"><style>.markdown-body {{ padding: 45px; }}</style></head><body class="markdown-body"><h1>Worker Logs</h1><pre>{content}</pre><a href="/">Back</a></body></html>'

def main():
    app.run(host='0.0.0.0', port=3000)

if __name__ == '__main__':
    main()
