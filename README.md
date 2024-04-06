# Splunk-GitHub Domain Monitor

A Python script designed to automate the monitoring of domain lists. It fetches domain lists from specified GitHub repositories and forwards each domain to Splunk for real-time monitoring and analysis. This tool is invaluable for cybersecurity professionals seeking to automate the tracking of domain lists for security research or operational monitoring.

## Features

- Automated fetching of domain lists from GitHub repositories.
- Forwarding of domains to Splunk via the HTTP Event Collector (HEC) for analysis.
- SSL warning suppression for internal networks using self-signed certificates.

## Prerequisites

- Python 3
- Splunk instance with HTTP Event Collector (HEC) enabled
- GitHub Personal Access Token (PAT) with repo access
- Splunk HEC Token

## Setup

1. Replace placeholder tokens and URLs in the script with actual values from your Splunk instance and GitHub account.
2. Ensure your Splunk HEC is configured to receive data.

## Usage

Run the script with Python 3:

```bash
python domain_monitor.py
```

## Contributions
Contributions are welcome. Please feel free to fork, modify, and make pull requests or report issues.
