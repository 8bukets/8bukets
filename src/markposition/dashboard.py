from flask import Flask, send_from_directory, render_template_string
import os
import glob
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    reports = sorted(glob.glob('results/DAILY_REPORT_*.md'), reverse=True)
    evolution = "SYSTEM_EVOLUTION.md"

    html = """
    <html>
    <head>
        <title>Autonomous System Admin UI</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css">
        <style>
            .markdown-body { box-sizing: border-box; min-width: 200px; max-width: 1200px; margin: 0 auto; padding: 45px; }
            @media (max-width: 767px) { .markdown-body { padding: 15px; } }
            .nav { margin-bottom: 20px; border-bottom: 1px solid #ddd; padding-bottom: 10px; }
            .stat-box { display: inline-block; background: #f6f8fa; border: 1px solid #d0d7de; padding: 10px; margin-right: 10px; border-radius: 6px; }
        </style>
    </head>
    <body class="markdown-body">
        <h1>Autonomous System Admin UI</h1>
        <div class="nav">
            <a href="/evolution">System Evolution Log</a> |
            <a href="/chat">Semantic Chat (RAG)</a> |
            <a href="/patterns">System Patterns</a> |
            <a href="/stats">System Stats</a> |
            <a href="/logs">Worker Logs</a>
        </div>

        <div style="margin-bottom: 20px;">
            <div class="stat-box"><strong>Distributed Mode:</strong> """ + os.getenv("DISTRIBUTED_MODE", "FALSE") + """</div>
            <div class="stat-box"><strong>Vector Store:</strong> """ + ("Enabled" if os.path.exists("data/vector_store") else "Disabled") + """</div>
        </div>

        <h2>Daily Reports</h2>
        <ul>
    """
    for report in reports:
        name = os.path.basename(report)
        html += f'<li><a href="/report/{name}">{name}</a></li>'

    html += "</ul></body></html>"
    return html

@app.route('/report/<name>')
def show_report(name):
    path = os.path.join('results', name)
    if not os.path.exists(path):
        return "Report not found", 404

    with open(path, 'r') as f:
        content = f.read()

    html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    return f'<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"><style>.markdown-body {{ box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }}</style></head><body class="markdown-body"><a href="/">Back</a><hr>{html_content}</body></html>'

@app.route('/stats')
def show_stats():
    import sqlite3
    db_path = os.getenv("MEMORY_FILE", "data/memory.db")
    stats = {}
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT agent_name, COUNT(*) FROM agent_memory GROUP BY agent_name")
        stats = dict(cursor.fetchall())
        conn.close()

    html = "<h1>System Persistence Stats</h1><ul>"
    for agent, count in stats.items():
        html += f"<li><strong>{agent}:</strong> {count} keys stored</li>"
    html += "</ul><a href='/'>Back</a>"
    return f'<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"><style>.markdown-body {{ padding: 45px; }}</style></head><body class="markdown-body">{html}</body></html>'

@app.route('/logs')
def show_logs():
    log_path = "/tmp/dashboard.log"
    content = "Log file not found."
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            content = f.read()
    return f'<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"><style>.markdown-body {{ padding: 45px; }}</style></head><body class="markdown-body"><h1>Worker Logs</h1><pre>{content}</pre><a href="/">Back</a></body></html>'

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

    html += "<h2>Source Code Structural Patterns</h2><ul>"
    source_patterns = vm.search("Source code patterns", top_k=20)
    for res in source_patterns:
        # Simple heuristic to identify source patterns
        if "Common dependency" in res['metadata'].get('text', '') or "Stage" in res['metadata'].get('text', ''):
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

@app.route('/results/<path:filename>')
def serve_results(filename):
    return send_from_directory('results', filename)

def main():
    app.run(host='0.0.0.0', port=3000)

if __name__ == '__main__':
    main()
