import requests

# You must get your API key from https://www.virustotal.com
VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY"

def check_url_virustotal(url):
    headers = {
        "x-apikey": VT_API_KEY
    }

    scan_url = "https://www.virustotal.com/api/v3/urls"
    report_url = "https://www.virustotal.com/api/v3/analyses/{}"

    try:
        # Encode and submit URL
        response = requests.post(scan_url, headers=headers, data={"url": url})
        response.raise_for_status()
        analysis_id = response.json()["data"]["id"]

        # Poll results (basic implementation)
        result = requests.get(report_url.format(analysis_id), headers=headers).json()
        malicious_score = result["data"]["attributes"]["stats"]["malicious"]

        return malicious_score > 0  # True if it's malicious
    except Exception as e:
        print(f"API Error: {e}")
        return False
