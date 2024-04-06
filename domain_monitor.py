import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Disable SSL warnings

# GitHub API configuration
github_repo_api_url = 'https://api.github.com/repos/<REPO>/contents/'  # GitHub repo URL
github_token = '<GITHUB_TOKEN>'  # GitHub PAT

# Splunk HEC configuration
splunk_hec_url = 'https://<SPLUNK_HEC_URL>:8088/services/collector'  # Splunk HEC endpoint, Change the port if needed
splunk_hec_token = '<SPLUNK_HEC_TOKEN>'  # Splunk HEC token
headers = {
    'Authorization': f'Splunk {splunk_hec_token}',
    'Content-Type': 'application/json',
}

def fetch_file_list(github_token):
    """Fetch list of .txt files from the GitHub repository."""
    auth_headers = {'Authorization': f'token {github_token}'}
    response = requests.get(github_repo_api_url, headers=auth_headers, verify=False)  # Fetch files list
    response.raise_for_status()  # Check for errors
    # Extract download URLs for .txt files
    files = [file['download_url'] for file in response.json() if file['name'].endswith('.txt')]
    return files

def send_domain_to_splunk(domain):
    """Send each domain to Splunk."""
    event = {
        "event": {"domain": domain},
        "sourcetype": "_json",
        "index": "",  # Splunk index to send data to
    }
    try:
        response = requests.post(splunk_hec_url, headers=headers, json=event, verify=False)  # Send data to Splunk
        response.raise_for_status()  # Check for errors
        print(f"Data sent to Splunk successfully: {domain}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send domain to Splunk: {domain}, Error: {e}")

def main():
    try:
        files = fetch_file_list(github_token)
        for file_url in files:
            response = requests.get(file_url, verify=False)  # Fetch domain list file
            domains = response.text.strip().splitlines()  # Process file into domain list
            for domain in domains:
                send_domain_to_splunk(domain)  # Send each domain to Splunk
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
