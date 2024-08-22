## Configure git

```bash
# Set your Git username and email globally
git config --global user.name "MD Pabel"
git config --global user.email "mdpabel385@gmail.com"

# Verify your global Git configuration settings
git config --global --list
```

## Repository

- **Working Directory:** This is where your project files live. Changes made here are untracked by Git until you stage them.
- **Staging Area (Index):** A temporary area where you can group changes you intend to commit. Staged files are ready to be committed.
- **Local Repository:** A hidden .git folder in your project directory. It stores all your commits, branches, and history for the repository.
- **Remote Repository:** A version of your project hosted on a server (e.g., GitHub, GitLab).

```bash
# Initializes a new Git repository in your project directory.
git init
# Displays the state of the working directory and staging area.
git status
# Unstages a file that was previously staged for commit, moving it back to the working directory.
git restore --staged filename.txt
# Moves changes from the working directory to the staging area.
git add
# Stages all changes in the entire repository.
git add -A
# Stages changes in the current directory.
git add .
# Records a snapshot of the changes in the staging area to the local repository.
git commit
```

## History

```bash
# Shows the commit history of the repository.
git log
# Displays a compact view of the commit history, showing just the commit hash and message.
git log --oneline
# Modify the most recent commit, either by changing the commit message or adding more changes.
git commit --amend -m "New commit message"
# It removes the most recent commit from the local repository
git reset HEAD~1
# Create a new commit that undoes the changes from a previous commit without modifying the existing history.
git revert d853732
# Restore the specific files from that commit.
git git checkout 1677f61 c.txt
```
