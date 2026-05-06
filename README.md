# 🤖 Self-Improving Repository

A Python Todo application that automatically improves itself every 2 hours using AI,
with tests running on an ephemeral Hetzner VPS via a secure Tailscale tunnel.

## How It Works

### Part 1 — AI Self-Improvement (every 2 hours)
1. GitHub Actions triggers the AI agent
2. Agent reads all Python files in the repository
3. Sends them to GPT-4o via GitHub Models API
4. AI suggests improvements (type hints, docstrings, error handling, new features)
5. Changes are committed automatically to main

### Part 2 — Testing on Ephemeral Hetzner VPS
1. Triggered automatically after AI improvement workflow
2. Script creates a Hetzner VPS (cx22, ~2.99€/month)
3. VPS connects to private network via Tailscale (no public SSH)
4. GitHub Actions self-hosted runner starts on the VPS
5. Tests run on the VPS
6. VPS is deleted immediately after tests finish

## Setup

### Required Secrets
Add these in **Repo Settings → Secrets and variables → Actions**:

| Secret | Description |
|---|---|
| `MODELS_TOKEN` | GitHub Personal Access Token for GitHub Models API |
| `HETZNER_API_TOKEN` | Hetzner Cloud API token (Read & Write) |
| `TAILSCALE_AUTH_KEY` | Tailscale auth key (Reusable + Ephemeral) |

### Infrastructure
- **AI Model:** GPT-4o via GitHub Models
- **VPS:** Hetzner cx23 — deleted after each test run
- **Tunnel:** Tailscale — no public SSH access to the VPS
- **CI/CD:** GitHub Actions
