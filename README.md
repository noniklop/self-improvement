# 🤖 Self-Improving Repository

A Python Todo application that automatically improves itself every 2 hours using AI (GitHub Models / GPT-4o).

## How It Works

Every 2 hours, a GitHub Actions workflow:
1. Reads all Python files in the repository
2. Sends them to GPT-4o via GitHub Models API
3. AI suggests improvements (type hints, docstrings, error handling, new features)
4. Changes are committed automatically
5. Tests run to verify nothing is broken

## Setup

### Prerequisites
- Public GitHub repository
- Personal Access Token (PAT) with no special scopes

### Configuration
1. Create a PAT: **GitHub Settings → Developer settings → Personal access tokens → Generate new token**
2. Add it to repository secrets: **Repo Settings → Secrets and variables → Actions → New secret**
   - Name: `MODELS_TOKEN`
   - Value: your PAT

### Run Manually
Go to **Actions → AI Self-Improvement → Run workflow**

## Tech Stack

- **Language:** Python 3.11
- **AI Model:** GPT-4o
- **CI/CD:** GitHub Actions
- **Testing:** pytest

## Example AI Improvements

Each automated commit improves the codebase incrementally:
- Adding type hints and docstrings
- Better error handling and input validation
- New helper methods and features
- Additional test coverage
