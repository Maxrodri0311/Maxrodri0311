import os
import sys
import requests
import re
from datetime import datetime

# UTF-8 Console Encoding for Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# GitHub vars
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
USERNAME = "Maxrodri0311"

def get_latest_commit_narrative():
    """Extrae el último evento de push en los repositorios públicos de Maximiliano."""
    url = f"https://api.github.com/users/{USERNAME}/events/public"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            events = response.json()
            for event in events:
                if event.get("type") == "PushEvent":
                    repo_name = event.get("repo", {}).get("name", "")
                    commits = event.get("payload", {}).get("commits", [])
                    if commits:
                        latest_commit = commits[0].get("message", "Sync updates")
                        commit_hash = commits[0].get("sha", "")[:7]
                        commit_url = f"https://github.com/{repo_name}/commit/{commits[0].get('sha')}"
                        short_repo = repo_name.split("/")[-1] if "/" in repo_name else repo_name
                        
                        return f"> 🚀 **Último despliegue en [{short_repo}](https://github.com/{repo_name}):**<br>\n> `{commit_hash}` — [{latest_commit}]({commit_url})"
            
            return "> ⚡ **Despliegues Activos:** Mantenimiento de arquitecturas y pipelines en producción."
        else:
            return f"> ⚡ **Despliegues Activos:** Sincronización continua de arquitecturas en OCI y microservicios."
    except Exception:
        return "> ⚡ **Despliegues Activos:** Sincronización continua de arquitecturas y pipelines."

def generate_dashboard_svgs():
    """Genera widgets de telemetría con tarjetas de alta estabilidad y estética TokyoNight."""
    html = f'''<div align="center">
  <img width="48%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={USERNAME}&theme=tokyonight" alt="GitHub Profile Details" />
  <img width="48%" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username={USERNAME}&theme=tokyonight" alt="Top Languages by Commit" />
</div>
<br>
<div align="center">
  <img width="98%" src="https://github-readme-activity-graph.vercel.app/graph?username={USERNAME}&theme=tokyo-night&hide_border=true&area=true" alt="Contribution Activity Graph" />
</div>'''
    return html

def update_readme():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(script_dir, "README.md")
    
    if not os.path.exists(readme_path):
        print(f"Error: No se encontró {readme_path}")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # 1. Inyectar el Dashboard SVG
    dashboard_html = generate_dashboard_svgs()
    readme_content = re.sub(
        r"(<!-- START_DASHBOARD -->\n).*?(\n<!-- END_DASHBOARD -->)",
        f"\\1{dashboard_html}\\2",
        readme_content,
        flags=re.DOTALL
    )

    # 2. Inyectar Currently Engineering
    latest_commit = get_latest_commit_narrative()
    readme_content = re.sub(
        r"(<!-- START_CURRENT_ENGINEERING -->\n).*?(\n<!-- END_CURRENT_ENGINEERING -->)",
        f"\\1{latest_commit}\\2",
        readme_content,
        flags=re.DOTALL
    )

    # Sobreescribir con encoding UTF-8 estricto
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    print("✅ Dashboard y telemetría de README.md actualizados con éxito.")

if __name__ == "__main__":
    update_readme()
