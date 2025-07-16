import os
import subprocess
from datetime import datetime, timedelta
import shutil

# === CONFIG ===
source_folder = "/Users/macbookpro/Documents/CS"
repo_folder = "/Users/macbookpro/Library/CloudStorage/GoogleDrive-mp352@njit.edu/My Drive/cs-archive"
branch = "main"
remote = "origin"

# === GATHER FILES ===
all_files = []
for root, _, files in os.walk(source_folder):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, start=source_folder)
        all_files.append((full_path, rel_path))

all_files.sort()
commit_date = datetime.now() - timedelta(days=len(all_files))

progress_file = os.path.join(repo_folder, ".progress.txt")
already_committed = set()

if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        already_committed = set(f.read().splitlines())

for full_path, rel_path in all_files:
    if rel_path in already_committed:
        continue

    dest_path = os.path.join(repo_folder, rel_path)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.copy2(full_path, dest_path)

    subprocess.run(["git", "add", rel_path], cwd=repo_folder, check=True)

    env = os.environ.copy()
    commit_time = commit_date.strftime("%Y-%m-%dT12:00:00")
    env["GIT_AUTHOR_DATE"] = commit_time
    env["GIT_COMMITTER_DATE"] = commit_time

    subprocess.run(["git", "commit", "-m", f"Add {rel_path}"], cwd=repo_folder, env=env, check=True)
    subprocess.run(["git", "push", remote, branch], cwd=repo_folder, check=True)

    print(f"✅ Committed and pushed: {rel_path} — {commit_time}")

    with open(progress_file, "a") as f:
        f.write(rel_path + "\n")

    break  # Only one file per day
