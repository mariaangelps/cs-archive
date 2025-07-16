import os
import shutil
import subprocess
from datetime import datetime, timedelta

# --- CONFIG ---
repo_folder = "/Users/macbookpro/Library/CloudStorage/GoogleDrive-mp352@njit.edu/My Drive/cs-archive"
source_folder = os.path.join(repo_folder, "CS")  # The full CS folder is now inside the repo
branch = "main"
remote = "origin"

# --- GET ALL FILES ---
all_files = []
for root, _, files in os.walk(source_folder):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, start=repo_folder)  # Include CS/ in path
        all_files.append((full_path, rel_path))

# --- Sort for consistency ---
all_files.sort()
commit_date = datetime.now() - timedelta(days=len(all_files))

# --- Load progress ---
progress_file = os.path.join(repo_folder, ".progress.txt")
already_committed = set()

if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        already_committed = set(f.read().splitlines())

# --- Upload one file ---
for full_path, rel_path in all_files:
    if rel_path in already_committed:
        continue

    # Add to Git
    subprocess.run(["git", "add", rel_path], cwd=repo_folder, check=True)

    # Backdated commit
    env = os.environ.copy()
    commit_time = commit_date.strftime("%Y-%m-%dT12:00:00")
    env["GIT_AUTHOR_DATE"] = commit_time
    env["GIT_COMMITTER_DATE"] = commit_time

    subprocess.run(
        ["git", "commit", "-m", f"Add {rel_path}"],
        cwd=repo_folder,
        env=env,
        check=True
    )

    subprocess.run(["git", "push", remote, branch], cwd=repo_folder, check=True)

    print(f"✅ Committed and pushed: {rel_path} — {commit_time}")

    # Save progress
    with open(progress_file, "a") as f:
        f.write(rel_path + "\n")

    break  # Only one file per run
