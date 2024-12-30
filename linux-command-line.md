---
title: Linux Commands and Practice Tasks
description: Comprehensive Linux commands, categorized with practice tasks for mastering Linux.
date: 03-24-2024
status: published
priority: 998
---

# Linux Commands

## **1. Navigation and Basic Commands**

- **Navigation**:

  - `pwd` – Print the current working directory.
  - `cd` – Change directory.
  - `cd /` – Go to the root directory.
  - `cd -` – Go to the previous directory.
  - `cd ~` – Go to the home directory.

- **Listing Files**:

  - `ls` – List files and directories.
  - `ls -l` – Long listing format.
  - `ls -a` – Show hidden files.
  - `ls -lah` – Long listing with human-readable sizes.
  - `ls --ignore=test` – Ignore files matching a pattern.

- **File Creation**:
  - `touch` – Create an empty file.
  - `touch file{1,2,3,4}.txt` – Create multiple files.

---

## **2. File and Directory Management**

- **Directories**:

  - `mkdir my-new-folder` – Create a new directory.
  - `mkdir -p ~/temp/subdir` – Create nested directories.

- **File Operations**:

  - `cp s-file d-file` – Copy a file.
  - `cp -r` – Copy directories recursively.
  - `mv` – Move or rename files or directories.
  - `rm` – Remove files.
  - `rm -r` – Remove directories recursively.
  - `rm -rf` – Force remove files and directories.

- **Archives and Compression**:
  - `tar -cf archive.tar folder` – Create a tar archive.
  - `tar -zcf archive.tar.gz folder` – Create a compressed tar.gz archive.
  - `tar -xzf archive.tar.gz` – Extract a tar.gz archive.

---

## **3. Text Editing and Viewing**

- **Nano**:

  - `ctrl+o` – Save a file.
  - `ctrl+x` – Exit Nano.

- **Vim**:

  - `i` – Insert mode.
  - `:q` – Quit.
  - `:q!` – Quit without saving.
  - `:w` – Save.
  - `:d` – Delete line(s).

- **Reading Files**:
  - `cat` – Display file contents.
  - `less` – View file contents one page at a time.
  - `/` – Search within `less`.
  - `head` – Show the first few lines of a file.
  - `tail` – Show the last few lines of a file.
  - `tail -f` – Monitor a file in real-time.

---

## **4. File Permissions and Ownership**

- `chmod u=rw,g=rw,o=rw file.txt` – Set specific permissions.
- `chmod 777 file.txt` – Give full permissions.
- `chown user:group file.txt` – Change file ownership.
- `chmod +x file.sh` – Make a file executable.

---

## **5. Processes and Job Control**

- **Process Management**:

  - `ps` – View running processes.
  - `ps aux` – Detailed list of processes.
  - `ps aux | grep "process-name"` – Search for a process.
  - `kill -9 PID` – Force kill a process.
  - `kill -l` – List all signal types.

- **Job Control**:
  - `sleep 1000` – Start a long process.
  - `ctrl+z` – Pause a process.
  - `jobs` – View background jobs.
  - `bg 1` – Resume a job in the background.
  - `fg 1` – Resume a job in the foreground.

---

## **6. Shell Utilities and Shortcuts**

- **Redirection**:

  - `echo "hello" > file.txt` – Redirect output to a file.
  - `echo "hello" >> file.txt` – Append output to a file.
  - `2>` – Redirect errors.
  - `/dev/null` – Discard output.

- **Pipes**:

  - `ps aux | grep "process-name"` – Combine commands.

- **Shortcuts**:
  - `!!` – Repeat the last command.
  - `sudo !!` – Run the last command as superuser.
  - `ctrl+r` – Search command history.
  - `ctrl+a` – Go to the start of the line.
  - `ctrl+e` – Go to the end of the line.

---

## **7. Environment Variables**

- `printenv` – Show environment variables.
- `export VAR=value` – Set a temporary variable.
- **Set environment variables permanently**:
  - Add them to `~/.bashrc` or `~/.bash_profile`.
  - Use `vim ~/.bashrc` and add: `export VAR=value`.
  - Run `source ~/.bashrc` to apply changes.
- **System-wide variables**:
  - Edit `/etc/environment` to set system-wide environment variables.

---

## **8. Networking**

- **SSH**:

  - `ssh-keygen -t rsa` – Generate SSH keys.
  - `ssh user@host` – Connect to a remote machine.
  - `chmod 700 ~/.ssh` – Secure SSH directory.

- **SFTP**:

  - `sftp user@host` – Open an SFTP session.
  - `pwd` – Show the current directory on the remote server.
  - `lpwd` – Show the current local directory.
  - `ls` – List files on the remote server.
  - `lls` – List files locally.
  - `put file.txt` – Upload a file to the remote server.
  - `get file.txt` – Download a file from the remote server.
  - `bye` – Exit the SFTP session.

- **Testing Connections**:
  - `curl http://localhost:8000/` – Test HTTP requests.
  - `wget http://example.com/file` – Download a file.

---

## **9. Package Management**

- **APT (Ubuntu/Debian)**:
  - `apt update` – Update package lists.
  - `apt upgrade` – Upgrade installed packages.
  - `apt install package` – Install a package.
  - `apt autoremove` – Remove unused packages.

---

## **10. Advanced Commands**

- **Disk Usage**:

  - `df -h` – Show disk space usage.
  - `du -sh folder` – Show folder size.

- **System Monitoring**:

  - `htop` – Interactive process viewer.
  - `top` – Real-time system stats.

- **Logs**:
  - `tail -f /var/log/syslog` – Monitor logs in real-time.
  - `grep "error" /var/log/syslog` – Search for errors in logs.

---

## **11. Debugging and Testing**

- `strace` – Trace system calls of a program.
- `lsof` – List open files.
- `dmesg` – View kernel messages.

---

## **12. Automation and Scheduling**

- **Cron Jobs**:
  - `crontab -e` – Edit cron jobs for a user.
  - `@reboot` – Run a task at system startup.
  - `0 2 * * *` – Schedule a task (e.g., daily at 2 AM).

---

# Linux Commands Practice

## **1. Navigation and Basic Commands**

### **Task 1: Navigate and Explore**

1. Print the current working directory and navigate to the root directory, then back:

   ```bash
   pwd
   cd /
   cd -
   ```

   **Expected Output**:

   ```
   /home/your-username
   /
   /home/your-username
   ```

2. List all files in `/etc` sorted by size in human-readable format:

   ```bash
   ls -lSh /etc
   ```

   **Expected Output** (example):

   ```
   -rw-r--r-- 1 root root 1.2M Jan  1 10:00 file1
   -rw-r--r-- 1 root root  512 Jan  1 10:00 file2
   ```

3. Count the number of hidden files in your home directory:
   ```bash
   ls -A ~ | grep "^\." | wc -l
   ```
   **Expected Output**:
   ```
   10
   ```

---

## **2. File and Directory Management**

### **Task 2: Organize and Manage Files**

1. Create a directory structure and files:

   ```bash
   mkdir -p ~/projects/{frontend,backend}
   touch ~/projects/frontend/{index.html,styles.css}
   touch ~/projects/backend/{app.js,server.js}
   ```

   **Expected Output**:
   Use `ls -R ~/projects` to verify:

   ```
   projects:
   backend  frontend

   projects/backend:
   app.js  server.js

   projects/frontend:
   index.html  styles.css
   ```

2. Move and rename files:

   ```bash
   mv ~/projects/frontend/index.html ~/projects/backend/
   mv ~/projects/backend/app.js ~/projects/backend/app-backup.js
   ```

   **Expected Output**:
   Use `ls ~/projects/backend` to verify:

   ```
   index.html  app-backup.js  server.js
   ```

3. Compress the `projects` directory:
   ```bash
   tar -zcf projects.tar.gz ~/projects
   ```
   Verify:
   ```bash
   ls -lh projects.tar.gz
   ```
   **Expected Output**:
   ```
   -rw-r--r-- 1 user user 4.0K Jan  1 10:10 projects.tar.gz
   ```

---

## **3. File Permissions and Ownership**

### **Task 3: Secure Files**

1. Create a file and set restrictive permissions:

   ```bash
   touch secure-data.txt
   chmod 600 secure-data.txt
   ls -l secure-data.txt
   ```

   **Expected Output**:

   ```
   -rw------- 1 user user 0 Jan  1 10:15 secure-data.txt
   ```

2. Change the ownership of the file:
   ```bash
   sudo chown root:root secure-data.txt
   ls -l secure-data.txt
   ```
   **Expected Output**:
   ```
   -rw------- 1 root root 0 Jan  1 10:15 secure-data.txt
   ```

---

## **4. Processes and Job Control**

### **Task 4: Manage Processes**

1. Start a background task:

   ```bash
   sleep 100 &
   jobs
   ```

   **Expected Output**:

   ```
   [1]+  Running                 sleep 100 &
   ```

2. Bring the task to the foreground and then terminate it:

   ```bash
   fg 1
   ctrl+c
   ```

   **Expected Output**:

   ```
   ^C
   ```

3. View and kill a specific process:
   ```bash
   ps aux | grep "sleep"
   kill -9 <PID>
   ```
   **Expected Output**:
   ```
   (No output if the process is successfully terminated.)
   ```

---

## **5. Networking**

### **Task 5: Test Remote Connections**

1. Start a local HTTP server:

   ```bash
   python3 -m http.server 8000 &
   curl http://localhost:8000
   ```

   **Expected Output** (example):

   ```
   <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
   <html>
   <head>
   <title>Index of /</title>
   </head>
   <body>
   <h1>Index of /</h1>
   ...
   ```

2. Securely transfer files using `sftp`:
   ```bash
   sftp user@remote-server
   put secure-data.txt
   ls
   ```
   **Expected Output**:
   ```
   sftp> put secure-data.txt
   Uploading secure-data.txt to /home/user/secure-data.txt
   sftp> ls
   secure-data.txt
   ```

---

## **6. Environment Variables**

### **Task 6: Set and Use Environment Variables**

1. Set a temporary environment variable:

   ```bash
   export MY_VAR="Hello, Linux!"
   echo $MY_VAR
   ```

   **Expected Output**:

   ```
   Hello, Linux!
   ```

2. Make it permanent:
   ```bash
   echo 'export MY_VAR="Persistent Value"' >> ~/.bashrc
   source ~/.bashrc
   echo $MY_VAR
   ```
   **Expected Output**:
   ```
   Persistent Value
   ```

---

## **7. System Monitoring**

### **Task 7: Monitor Resource Usage**

1. Check disk usage:

   ```bash
   df -h
   ```

   **Expected Output** (example):

   ```
   Filesystem      Size  Used Avail Use% Mounted on
   /dev/sda1        50G   20G   30G  40% /
   ```

2. Monitor CPU and memory:
   ```bash
   htop
   ```
   **Expected Output**: (Interactive process viewer opens showing real-time system stats.)

---

## **8. Debugging**

### **Task 8: Debug Scripts**

1. Create a script with an intentional error:

   ```bash
   echo -e '#!/bin/bash\ncat nonexistent-file' > faulty.sh
   chmod +x faulty.sh
   ./faulty.sh
   ```

   **Expected Output**:

   ```
   cat: nonexistent-file: No such file or directory
   ```

2. Debug the script:
   ```bash
   bash -x faulty.sh
   ```
   **Expected Output**:
   ```
   + cat nonexistent-file
   cat: nonexistent-file: No such file or directory
   ```
