import subprocess
import sys

def git_auto_commit(message):
    # Configure paths and Git credentials
    repo_path = "C:\\Users\\oloye_p5znpgw\\Desktop\\Transferme-Banking-App\\Transferme-Banking-App\\Banking"
    git_user = "Mista-Log"
    git_email = "oloyedeibrahimsmile@gmail.com"

    try:
        # Configure Git
        subprocess.run(["git", "config", "--global", "user.name", git_user], check=True, cwd=repo_path)
        subprocess.run(["git", "config", "--global", "user.email", git_email], check=True, cwd=repo_path)

        # Optional: Append message to a file
        # with open(f"{repo_path}/messages.txt", "a") as f:
        #     f.write(f"{message}\n")

        # Stage changes, commit, and push
        subprocess.run(["git", "add", "."], check=True, cwd=repo_path)
        subprocess.run(["git", "commit", "-m", message], check=True, cwd=repo_path)
        subprocess.run(["git", "push", "origin", "main"], check=True, cwd=repo_path)  # Replace 'main' with your branch
        print("Commit successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python git-bot.py 'Your commit message'")
        sys.exit(1)
    git_auto_commit(sys.argv[1])