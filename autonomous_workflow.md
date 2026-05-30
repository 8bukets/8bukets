# Autonomous Automatic Workflows

To set up the system for fully autonomous, automatic execution, you have a few options:

## 1. Using `systemd` (Linux Background Service - Recommended for VPS/Dedicated Server)
This ensures the system runs in the background and restarts automatically if the server reboots.

1. Create a service file: `sudo nano /etc/systemd/system/sigma-seo.service`
2. Add the following configuration (adjust `/path/to/project`):
```ini
[Unit]
Description=Massive Scale Autonomous Sigma SEO System
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/path/to/project
Environment="SYSTEM_AUTH_TOKEN=your_secure_token"
Environment="MONGODB_URI=your_mongodb_uri"
Environment="NEXT_PUBLIC_SUPABASE_URL=your_supabase_url"
Environment="NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key"
Environment="GOOGLE_API_KEY=your_google_api_key"
Environment="GEMINI_API_KEY=your_gemini_api_key"
ExecStart=/usr/bin/npm run ignite
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```
3. Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable sigma-seo
sudo systemctl start sigma-seo
```

## 2. Using `cron` (Scheduled Execution)
If you prefer running it daily at a specific time (e.g., 2 AM) instead of a continuous loop:

1. Open crontab: `crontab -e`
2. Add the following line:
```cron
0 2 * * * cd /path/to/project && SYSTEM_AUTH_TOKEN=your_secure_token MONGODB_URI=your_mongodb_uri NEXT_PUBLIC_SUPABASE_URL=your_supabase_url NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key GOOGLE_API_KEY=your_google_api_key GEMINI_API_KEY=your_gemini_api_key /usr/bin/npm run daily > /path/to/project/results/cron.log 2>&1
```

## 3. GitHub Actions (CI/CD Automation)
A GitHub Actions workflow has been created in `.github/workflows/autonomous_cycle.yml` to run the tests and cycle automatically on pushes or on a daily schedule.
