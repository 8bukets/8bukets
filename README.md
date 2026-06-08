[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/8bukets/8bukets&fullConfiguration=true)

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

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
