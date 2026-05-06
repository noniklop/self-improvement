# improve.py

import os
import anthropic
import subprocess
from pathlib import Path

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def read_files():
    """Читає всі .py файли з репо"""
    files = {}
    for path in Path(".").rglob("*.py"):
        if ".git" in str(path):
            continue
        files[str(path)] = path.read_text()
    return files

def ask_claude_to_improve(files: dict) -> dict:
    """Просить Claude покращити код і повернути змінені файли"""
    
    files_content = "\n\n".join(
        f"### FILE: {name}\n```python\n{content}\n```"
        for name, content in files.items()
    )

    prompt = f"""You are a senior Python developer doing a code review and improvement pass.

Here are the current files in the repository:

{files_content}

Your task:
- Improve code quality (add docstrings, type hints, better error handling)
- You may add small useful features to todo.py
- Keep or improve existing tests, add new ones if needed
- Do NOT break existing functionality
- Make meaningful but focused changes — not everything at once

Respond ONLY with a JSON object in this exact format:
{{
  "changes": [
    {{
      "file": "src/todo.py",
      "content": "...full new file content..."
    }}
  ],
  "summary": "Short description of what was improved"
}}

Return only files you actually changed. Return valid JSON only, no markdown."""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )
    
    import json
    response_text = message.content[0].text
    return json.loads(response_text)

def apply_changes(result: dict):
    """Записує змінені файли на диск"""
    for change in result["changes"]:
        path = Path(change["file"])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(change["content"])
        print(f"✅ Updated: {change['file']}")

def git_commit(summary: str):
    """Комітить зміни в репо"""
    subprocess.run(["git", "config", "user.email", "ai-agent@self-improvement.bot"])
    subprocess.run(["git", "config", "user.name", "AI Improvement Agent"])
    subprocess.run(["git", "add", "-A"])
    
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        capture_output=True
    )
    
    if result.returncode != 0:
        subprocess.run(["git", "commit", "-m", f"🤖 AI improvement: {summary}"])
        subprocess.run(["git", "push"])
        print(f"✅ Committed: {summary}")
    else:
        print("ℹ️ No changes to commit")

if __name__ == "__main__":
    print("🔍 Reading repository files...")
    files = read_files()
    
    print("🤖 Asking Claude to improve the code...")
    result = ask_claude_to_improve(files)
    
    print(f"📝 Summary: {result['summary']}")
    apply_changes(result)
    
    print("📦 Committing changes...")
    git_commit(result["summary"])
