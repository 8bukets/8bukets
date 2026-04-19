import os
import json
from flask import Flask, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markposition Autonomous Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; }
        .card { margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .agent-badge { font-size: 0.8rem; margin: 2px; }
    </style>
</head>
<body>
    <nav class="navbar navbar-dark bg-dark">
        <div class="container">
            <span class="navbar-brand mb-0 h1">Markposition Dashboard v{{ version }}</span>
        </div>
    </nav>

    <div class="container mt-4">
        <div class="row">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-header bg-primary text-white">System Status</div>
                    <div class="card-body">
                        <h5 class="card-title">Sigma Status: <span id="sigma-score">--</span></h5>
                        <p class="card-text">Active Agents: <span id="agent-count">--</span></p>
                        <p class="card-text">Current Version: <b>v{{ version }}</b></p>
                    </div>
                </div>
            </div>
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header bg-success text-white">Latest Evolution Entry</div>
                    <div class="card-body" id="latest-evolution">
                        Loading...
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header">Real-Time Telemetry Feed</div>
                    <div class="card-body">
                        <ul class="list-group list-group-flush" id="telemetry-feed">
                            <li class="list-group-item">Waiting for cycle data...</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        async def fetchData() {
            try {
                const response = await fetch('/api/data');
                const data = await response.json();

                document.getElementById('sigma-score').innerText = data.sigma_score;
                document.getElementById('agent-count').innerText = data.agent_count;
                document.getElementById('latest-evolution').innerText = data.evolution_summary;

                const feed = document.getElementById('telemetry-feed');
                feed.innerHTML = '';
                data.telemetry.slice(-10).reverse().forEach(event => {
                    const li = document.createElement('li');
                    li.className = 'list-group-item';
                    li.innerHTML = `<strong>[${event.agent}]</strong> ${event.event_type}: ${JSON.stringify(event.payload)}`;
                    feed.appendChild(li);
                });
            } catch (e) { console.error(e); }
        }
        setInterval(fetchData, 5000);
        fetchData();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    # Load version from config
    version = "1.0"
    if os.path.exists("config/evolution_params.json"):
        with open("config/evolution_params.json", 'r') as f:
            version = json.load(f).get("current_version", "1.0")
    return render_template_string(INDEX_HTML, version=version)

@app.route('/api/data')
def get_data():
    data = {
        "sigma_score": "0.0",
        "agent_count": 0,
        "evolution_summary": "No evolution log found.",
        "telemetry": []
    }

    # Load telemetry
    if os.path.exists("data/telemetry.json"):
        with open("data/telemetry.json", 'r') as f:
            data["telemetry"] = json.load(f)

    # Load evolution log (last line)
    if os.path.exists("SYSTEM_EVOLUTION.md"):
        with open("SYSTEM_EVOLUTION.md", 'r') as f:
            lines = f.readlines()
            # Find the last entry block
            data["evolution_summary"] = "".join(lines[-10:])

    # Load latest report for stats
    if os.path.exists("config/evolution_params.json"):
        with open("config/evolution_params.json", 'r') as f:
            config = json.load(f)
            data["sigma_score"] = str(config.get("seo_impact_threshold", "0.0"))

    return jsonify(data)

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
