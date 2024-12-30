---
title:
description:
date: 04-22-2024
status: published
priority: 951
---

## Website Enumeration

### Google Dorks

```bash
# Search for PDF files specifically on the tesla.com domain
site:tesla.com filetype:pdf

# Find instances of '@tesla.com' email addresses but exclude results from tesla.com domain itself
"@tesla.com" -site:tesla.com

# Look for admin pages on tesla.com by using either 'admin' in the title or 'admin' in the URL
intitle:admin OR inurl:admin site:tesla.com

# A reference to the Exploit Database's Google Hacking Database (GHDB) for other useful Google dorking queries
https://www.exploit-db.com/google-hacking-database?category=8

```

### Basic Network Enumeration

```bash
# Send a ping request to mdpabel.com to check network connectivity
ping mdpabel.com

# Perform a DNS lookup for mdpabel.com (typo corrected to 'nslookup')
nslookup mdpabel.com

# Get DNS information about mdpabel.com, including its IP address and mail servers
host mdpabel.com
```

### whatweb

```bash
# Basic scan of a website
whatweb mdpabel.com

# More aggressive scan with additional details
whatweb -v -a 3 mdpabel.com

# Scanning multiple websites listed in a file
whatweb -i websites.txt
```

### dirb

```bash
# Basic scan of a website using the default wordlist
dirb http://mdpabel.com

# Scan with a custom wordlist
dirb http://mdpabel.com /path/to/custom-wordlist.txt

# Recursive scan (scans found subdirectories as well)
dirb http://mdpabel.com -r

# Scanning a specific directory
dirb http://mdpabel.com/admin/

# Scan for specific file extensions (e.g., .php, .html)
dirb http://mdpabel.com -X .php,.html
```
