import subprocess
import urllib.request
import json
import os

repo_dir = r"C:\Users\dell\Documents\microservices\TP 3 - Spring IoC & OCP - Stratégies d'Injection et Sélection d'Implémentations"
repo_name = "TP-3-Spring-IoC-OCP-Strategies-d-Injection-et-Selection-d-Implementations"
repo_desc = "TP 3 : Spring IoC & OCP - Stratégies d'Injection et Sélection d'Implémentations"

# 1. Get token from git credential
p = subprocess.Popen(
    ["git", "credential", "fill"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
out, err = p.communicate("protocol=https\nhost=github.com\n\n")
token = None
for line in out.splitlines():
    if line.startswith("password="):
        token = line.split("=", 1)[1]

if not token:
    print("Could not retrieve GitHub token")
    exit(1)

# 2. Check if repo exists or create it
create_data = json.dumps({
    "name": repo_name,
    "description": repo_desc,
    "private": False
}).encode("utf-8")

req = urllib.request.Request(
    "https://api.github.com/user/repos",
    data=create_data,
    headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "Antigravity",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("GitHub Repository created successfully:", res.get("html_url"))
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    if e.code == 422 and "already exists" in body:
        print("Repo already exists on GitHub. Continuing with push...")
    else:
        print(f"HTTPError: {e.code} {body}")
except Exception as e:
    print("Exception during repo creation:", e)

# 3. Git commands inside repo_dir
def run_git(args):
    print("Running: git", " ".join(args))
    res = subprocess.run(["git"] + args, cwd=repo_dir, capture_output=True, text=True)
    if res.stdout.strip():
        print("STDOUT:", res.stdout.strip())
    if res.stderr.strip():
        print("STDERR:", res.stderr.strip())
    return res.returncode

# Init if needed
if not os.path.exists(os.path.join(repo_dir, ".git")):
    run_git(["init"])

run_git(["config", "user.name", "OussamaFETOUAKI"])
run_git(["config", "user.email", "oussamafetouaki2@gmail.com"])
run_git(["add", "."])
run_git(["commit", "-m", "TP 3 : Spring IoC & OCP - Stratégies d'Injection et Sélection d'Implémentations"])
run_git(["branch", "-M", "main"])

remote_with_token = f"https://OussamaFETOUAKI:{token}@github.com/OussamaFETOUAKI/{repo_name}.git"
clean_remote = f"https://github.com/OussamaFETOUAKI/{repo_name}.git"

run_git(["remote", "remove", "origin"])
run_git(["remote", "add", "origin", remote_with_token])

print("Pushing to GitHub...")
push_code = run_git(["push", "-u", "origin", "main", "--force"])

# Clean up token in remote URL for security
run_git(["remote", "set-url", "origin", clean_remote])

if push_code == 0:
    print("\nSUCCESS! Repository pushed to:", clean_remote)
else:
    print("\nPush failed with code:", push_code)
