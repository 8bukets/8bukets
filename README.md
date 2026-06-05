# 🌌 Antigravity: The Autonomous Evolution Engine

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/8bukets/8bukets&fullConfiguration=true)

**Antigravity** is a multi-layered autonomous system designed for continuous cognitive evolution, multi-agent orchestration, and sovereign fleet management. It integrates high-level architectural ideation with ground-level execution, maintaining a permanent online presence across cloud and local environments.

---

## 🏗️ System Architecture

### 1. **The Jules Agent (Cognitive Layer)**
The lead architect, **Jules**, orchestrates the ecosystem's evolution. It performs:
- **Daily Work Cycles:** Autonomous self-repair, security audits, and dependency management.
- **Synthesis:** Generates architectural proposals based on system gaps and market intelligence.
- **Autonomous Merge:** Manages a fleet of over 2,300 branches, autonomously merging validated features into the production core.

### 2. **Autonomous Creation Engine (Execution Layer)**
Translates synthesized ideas into actionable work order chains:
- `BOOTSTRAP_SERVICE` → `SMOKE_TEST` → `DEPLOYMENT`
- Maintains zero-touch operations via a prioritized task queue.

### 3. **Omni-Presence Matrix (Connectivity Layer)**
Ensures 24/7 uptime through a hybrid synchronization strategy:
- **Cloud Simulation:** GitHub Actions and GitLab CI maintain constant activity.
- **iCloud Sync:** Real-time synchronization of intelligence data and code backups to Apple Cloud Docs.
- **Sovereign Fleet:** Deploys edge nodes with APAC regional optimization (<50ms latency).

---

## 📊 Dashboard & Monitoring

The **Antigravity Command** dashboard provides a real-time view of the ecosystem's health:
- **System Posture:** Live status of MongoDB, Supabase, and Docker sovereignty.
- **Cognitive Pulse:** Real-time log of autonomous decisions and predictive refactors.
- **Global Neural Network:** Tracking connectivity across Tokyo, Singapore, and European edge nodes.

---

## 🚀 Getting Started

### Development Environment
```bash
npm run dev      # Start the Antigravity Command Dashboard
npm run daily    # Manually trigger a Jules Daily Routine
npm run ignite   # Start the Continuous Autonomous Loop
```

### macOS Native Persistence
To install the **Jules LaunchAgent** for automated local maintenance:
1. Update `com.sigma.jules.plist` with your macOS username.
2. `cp com.sigma.jules.plist ~/Library/LaunchAgents/`
3. `launchctl load ~/Library/LaunchAgents/com.sigma.jules.plist`

---

## 📜 Licensing

Antigravity is dual-licensed:
1. **MIT License**: Applies to the software codebase.
2. **Creative Commons Attribution 4.0 International (CC BY 4.0)**: Applies to documentation, telemetry, and visual results.

Copyright (c) 2026 Filip Keser.

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

## Cloud Deployments (Docker, Supabase, MongoDB)

The autonomous system supports continuous cloud deployments using standard infrastructure primitives:

- **Docker Configs:** Ensure you use `docker-compose.cloud.yml` when spinning up nodes in external environments (it bypasses local MongoDB expectations).
- **Online Presence:** The autonomous system remains permanently on via GitHub Actions (`.github/workflows/continuous-presence.yml`) and GitLab CI schedules (`.gitlab-ci.yml`), performing data sync back to the main branches using GitKraken visual commit strategies.
- **Data Persistence:** Relies purely on remote MongoDB clusters and remote Supabase APIs, connected via standard deployment variables.

## Autonomous Daily Sync & Persistence

The Antigravity system includes an autonomous daily work cycle that performs Git synchronization (pull/upload) and iCloud folder backups.

### 1. Daily Automation (Persistence)

To "work every day" automatically, Antigravity provides scheduling scripts for both macOS and Linux.

#### macOS (LaunchAgent)
1. Run the installation script:
   ```bash
   ./scripts/install_launchd.sh
   ```
   Or manually copy and load `com.sigma.jules.plist` to `~/Library/LaunchAgents/`.

#### Linux (Cron)
1. Run the installation script:
   ```bash
   ./scripts/install_cron.sh
   ```
   This adds a daily job to your user's crontab.

Once installed, Jules will execute the daily work cycle every day at midnight.

### 2. Manual Commands

You can manually trigger the core synchronization tasks using the following commands:

- **Pull changes (pluu):** `npm run pluu`
- **Upload changes:** `npm run upload`
- **iCloud Sync:** `npm run sync:icloud`
- **Full Daily Cycle:** `npm run daily`

### 3. iCloud Synchronization

By default, the system syncs to `~/Library/Mobile Documents/com~apple~CloudDocs/Antigravity_Sync`. You can customize this by setting the `ICLOUD_SYNC_PATH` environment variable in your `.env` file.
