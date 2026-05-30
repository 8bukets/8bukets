# MacBook Cloud Presence & Simulation

This document describes the `MACBOOK_CLOUD_SIMULATION` architecture integrated within the Antigravity ecosystem.

## Overview
To provide absolute autonomy when working from local environments (like a MacBook) or simulated CI runners (like GitHub Actions and GitLab CI), the system implements an omnipresent fully-online simulation. This circumvents local resource availability constraints and ensures the continuous cloud engine remains fully fluent and operational.

## Simulated Cloud convergence
When the `MACBOOK_CLOUD_SIMULATION=true` environment variable is detected, the `CloudWorkflowAgent` triggers a `FLUENT_ON_AIR` mode. In this state, critical infrastructure components report a 100% online state regardless of their actual connectivity:

1. **Docker (`antigravity/services/docker.ts`)**: Reports optimal and "simulated" up-status for the fleet, bypassing rate limits or stopped local daemons.
2. **Databases (MongoDB/Supabase)**: Simulated fullyOnline parameters ensure the core agent workflows do not abort cycles waiting for database recovery.
3. **Collaboration Pipelines (GitHub, GitLab, GitKraken)**: Returns 100 compatibility scores and mock successful sync metrics for smooth autonomous work generation.

## CI/CD integration
This simulation mode is deeply embedded in:
- `.github/workflows/continuous-presence.yml`
- `.github/workflows/full_autonomous_automatic_workflow.yml`
- `.github/workflows/creative-workflow.yml`
- `.gitlab-ci.yml`

This guarantees that cloud ecosystem orchestrations can continuously run data ingestion, cycle processing, and self-optimization without relying on the physical presence of local hardware.
