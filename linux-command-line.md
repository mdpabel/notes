---
title: Linux Commands and Practice Tasks
description: Comprehensive Linux commands, categorized with practice tasks for mastering Linux.
date: 03-24-2024
status: published
priority: 999
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

## **3. Searching and Filtering**

- **Find Files**:

  - `find . -name "*.txt"` – Find all .txt files in the current directory.
  - `find /path -type f -name "*.log"` – Search for log files in a directory.
  - `find . -type f -exec chmod 644 {} \;` – Change permissions of all files.
  - `find . -mtime -7` – Find files modified in the last 7 days.
  - `find . -size +1M` – Find files larger than 1MB.
  - `find . -empty` – Find empty files and directories.

- **Grep**:

  - `grep "error" file.txt` – Search for a pattern in a file.
  - `grep -r "error" /var/log` – Search recursively in directories.
  - `grep -i "error" file.txt` – Case-insensitive search.
  - `grep -v "pattern" file.txt` – Exclude lines with a specific pattern.

- **Locate**:
  - `locate file-name` – Find a file by name.
  - `updatedb` – Update the file database for locate.

---

## **4. File Permissions and Ownership**

- `chmod u=rw,g=rw,o=rw file.txt` – Set specific permissions.
- `chmod 777 file.txt` – Give full permissions.
- `chmod +x file.sh` – Make a file executable.
- `chown user:group file.txt` – Change file ownership.
- `chown -R user:group folder` – Change ownership recursively.
- `chmod -R 755 folder` – Apply permissions recursively.
- `stat file.txt` – Display detailed file permissions and metadata.

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
  - `nice -n 10 process` – Start a process with a lower priority.
  - `renice -n 5 -p PID` – Change priority of a running process.

---

## **6. Shell Utilities and Shortcuts**

- **Redirection**:

  - `echo "hello" > file.txt` – Redirect output to a file.
  - `echo "hello" >> file.txt` – Append output to a file.
  - `2>` – Redirect errors.
  - `/dev/null` – Discard output.

- **Pipes**:

  - `ps aux | grep "process-name"` – Combine commands.
  - `cat file.txt | sort | uniq` – Sort and remove duplicates.

- **Shortcuts**:
  - `!!` – Repeat the last command.
  - `sudo !!` – Run the last command as superuser.
  - `ctrl+r` – Search command history.
  - `ctrl+a` – Go to the start of the line.
  - `ctrl+e` – Go to the end of the line.
  - `ctrl+w` – Delete the previous word.
  - `ctrl+u` – Clear the current line.

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
  - `ping example.com` – Test network connectivity.
  - `traceroute example.com` – Trace the route to a host.
  - `netstat -tuln` – View network connections.
  - `nmap -sP 192.168.1.0/24` – Scan a network for devices.

---

## **9. Package Management**

- **APT (Ubuntu/Debian)**:

  - `apt update` – Update package lists.
  - `apt upgrade` – Upgrade installed packages.
  - `apt install package` – Install a package.
  - `apt autoremove` – Remove unused packages.

- **YUM (CentOS/RedHat)**:
  - `yum update` – Update packages.
  - `yum install package` – Install a package.
  - `yum remove package` – Remove a package.

---

## **10. Advanced Commands**

- **Disk Usage**:

  - `df -h` – Show disk space usage.
  - `du -sh folder` – Show folder size.
  - `du -ah` – Show all files and directories with sizes.

- **System Monitoring**:

  - `htop` – Interactive process viewer.
  - `top` – Real-time system stats.
  - `vmstat` – Show system performance metrics.
  - `iotop` – Monitor disk I/O.

- **Logs**:

  - `tail -f /var/log/syslog` – Monitor logs in real-time.
  - `grep "error" /var/log/syslog` – Search for errors in logs.

- **Advanced File Operations**:

  - `rsync -av source/ destination/` – Sync files and directories.
  - `scp file.txt user@host:/path` – Securely copy files to a remote server.
  - `dd if=/dev/sda of=/dev/sdb bs=64K conv=noerror,sync` – Clone a disk.

- **Disk and Partition Management**:

  - `fdisk -l` – List all disks and partitions.
  - `mount /dev/sdX /mnt` – Mount a disk.
  - `umount /mnt` – Unmount a disk.
  - `lsblk` – List information about block devices.
  - `blkid` – Get UUID and filesystem information for devices.

- **Debugging and Testing**:
  - `strace program` – Trace system calls.
  - `lsof -i :80` – List processes using port 80.
  - `dmesg` – View kernel messages.

---

## **11. Automation and Scheduling**

- **Cron Jobs**:

  - `crontab -e` – Edit cron jobs for a user.
  - `@reboot` – Run a task at system startup.
  - `0 2 * * *` – Schedule a task (e.g., daily at 2 AM).

- **At Command**:
  - `at 2pm` – Schedule a one-time task.
  - `atq` – View pending tasks.
  - `atrm <job_id>` – Remove a pending task.

---

## **12. Backup and Recovery**

- **File Backup**:

  - `cp -r source_dir backup_dir` – Basic directory backup.
  - `rsync -av --progress /source /backup` – Efficient file synchronization for backup.
  - `tar -czvf backup.tar.gz /path/to/directory` – Create a compressed backup archive.
  - `tar -xzvf backup.tar.gz -C /restore/path` – Restore files from a backup archive.

- **Database Backup**:

  - `mysqldump -u root -p database_name > backup.sql` – Backup a MySQL database.
  - `mysqldump -u root -p --all-databases > all_backup.sql` – Backup all MySQL databases.
  - `pg_dump -U username -d database_name -f backup.sql` – Backup a PostgreSQL database.

- **Database Restoration**:

  - `mysql -u root -p database_name < backup.sql` – Restore a MySQL database.
  - `psql -U username -d database_name -f backup.sql` – Restore a PostgreSQL database.

- **Snapshot Backups**:
  - `rsnapshot config_file` – Use rsnapshot for incremental backups.
  - `btrfs subvolume snapshot /source /backup/snapshot_name` – Create a Btrfs snapshot.

---

## **13. Other Useful Commands**

- **Disk Cleanup**:

  - `sudo apt-get clean` – Clear cached package files.
  - `sudo apt-get autoclean` – Remove old cached files.
  - `sudo apt-get autoremove` – Remove unused packages.

- **User Management**:

  - `adduser username` – Add a new user.
  - `passwd username` – Set or change a user’s password.
  - `deluser username` – Delete a user.
  - `usermod -aG groupname username` – Add a user to a group.

- **Networking Tools**:

  - `ip a` – Display network interfaces and IP addresses.
  - `hostnamectl` – Manage hostname settings.
  - `ifconfig` – Display or configure network interfaces (deprecated, use `ip` instead).

- **System Performance**:

  - `uptime` – Show system uptime and load.
  - `free -h` – Display memory usage.
  - `sar` – Monitor CPU usage over time.

- **Filesystem Checks**:

  - `fsck /dev/sdX` – Check and repair a filesystem.
  - `tune2fs -l /dev/sdX` – Show filesystem parameters.

- **Hardware Information**:
  - `lscpu` – Display CPU architecture details.
  - `lsusb` – List USB devices.
  - `lspci` – List PCI devices.

---
