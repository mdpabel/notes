# VPS Setup Guide

This guide provides steps to set up and configure a VPS, categorized for better organization.

---

## System Initialization

### Update the Package Index

Before installing any packages, update the package index to ensure you're working with the latest versions.

```bash
sudo apt update
```

### Check Memory Usage

Use the `free` command to display memory usage in a human-readable format, including total, used, free, and available memory.

**Command:**

```bash
free -h
```

**Example Output:**

```
              total        used        free      shared  buff/cache   available
Mem:           1.9Gi       317Mi       865Mi       1.0Mi       924Mi       1.6Gi
Swap:             0B          0B          0B
```

### Disk Usage Information

Check the disk space usage of all mounted filesystems.

**Command:**

```bash
df -h
```

**Example Output:**

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        19G  2.0G   17G  11% /
```

---

## Nano (Text Editor)

### Install Nano

Nano is a lightweight text editor that is easy to use for editing files directly on your VPS.

**Install Nano:**

```bash
sudo apt install nano
```

### Verify Installation

Ensure Nano is successfully installed.

```bash
nano --version
```

---

## Swap Configuration

### Create a Swap File

Swap space is a portion of the disk used as virtual memory when physical RAM is full.

**Step 1: Create a Swap File**

```bash
sudo fallocate -l 1G /swapfile
```

**Step 2: Secure the Swap File**

```bash
sudo chmod 600 /swapfile
```

**Step 3: Set Up the Swap File**

```bash
sudo mkswap /swapfile
```

**Step 4: Enable the Swap File**

```bash
sudo swapon /swapfile
```

**Step 5: Verify Swap**

```bash
sudo swapon --show
```

### Make Swap Permanent

To ensure the swap file persists after a reboot, add it to the `/etc/fstab` file:

```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

---

## Webuzo Control Panel Installation

Webuzo is a control panel to manage your server efficiently.

### Steps to Install Webuzo

1. Update the package index:

   ```bash
   sudo apt update
   ```

2. Download the Webuzo installer script:

   ```bash
   wget -N http://files.webuzo.com/install.sh
   ```

3. Set executable permissions for the installer:

   ```bash
   chmod 755 install.sh
   ```

4. Run the installer:
   ```bash
   sudo ./install.sh
   ```

Once the installation is complete, follow the on-screen instructions to access and configure Webuzo.

---

### Useful Tips

- **Keep your system updated:** Regularly run `sudo apt update && sudo apt upgrade` to maintain security and performance.
- **Monitor system resources:** Use tools like `htop` or `top` for real-time monitoring of CPU and memory usage.

---

**Your VPS is now configured and ready for use!**
