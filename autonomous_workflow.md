# Autonomous Automatic Workflows

To set up the system for fully autonomous, automatic execution, the "fully autonomous automatic workflow" should be implemented as a CI/CD pipeline executing `scripts/execute_creation_cycle.ts`, rather than as a hardcoded local systemd service.

## GitHub Actions (CI/CD Automation)
A GitHub Actions workflow should be created (e.g., `.github/workflows/full_autonomous_automatic_workflow.yml`) to execute `scripts/execute_creation_cycle.ts` via `npx tsx scripts/execute_creation_cycle.ts` to run the cycle automatically. This ensures cloud independence.

A separate workflow is available at `.github/workflows/autonomous_cycle.yml` to run the tests and cycle automatically on pushes or on a daily schedule.
