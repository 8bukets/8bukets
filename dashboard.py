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
        <title>Autonomous System Dashboard</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css">
        <style>
            .markdown-body { box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }
            @media (max-width: 767px) { .markdown-body { padding: 15px; } }
            .nav { margin-bottom: 20px; }
        </style>
    </head>
    <body class="markdown-body">
        <h1>Autonomous System Dashboard</h1>
        <div class="nav">
            <a href="/evolution">System Evolution Log</a>
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
