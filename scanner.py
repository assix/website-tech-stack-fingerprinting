import sys
import socket
import requests
from urllib.parse import urlparse
from Wappalyzer import Wappalyzer, WebPage
import warnings

# Suppress BeautifulSoup/Wappalyzer warnings for clean terminal output
warnings.filterwarnings("ignore")

def get_domain(url):
    parsed = urlparse(url)
    return parsed.netloc or parsed.path

def analyze_website(url):
    if not url.startswith('http'):
        url = 'https://' + url
        
    print(f"\n--- Analyzing {url} ---\n")
    domain = get_domain(url)

    # 1. Network, Hosting, and Geolocation
    print("[*] HOSTING & NETWORK")
    try:
        ip = socket.gethostbyname(domain)
        print(f"  IP Address: {ip}")
        
        # Free IP geolocation API
        geo = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if geo.get("status") == "success":
            print(f"  Country: {geo.get('country')}")
            print(f"  ISP/Cloud Provider: {geo.get('isp')} / {geo.get('org')}")
        else:
            print("  Geolocation lookup failed.")
    except Exception as e:
        print(f"  Network lookup error: {e}")

    # 2. HTTP Headers & Security
    print("\n[*] SECURITY & SERVER HEADERS")
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        print(f"  Web Server (Header): {headers.get('Server', 'Hidden/Not specified')}")
        print(f"  X-Powered-By: {headers.get('X-Powered-By', 'Hidden/Not specified')}")
        print(f"  X-XSS-Protection: {headers.get('X-XSS-Protection', 'Missing')}")
        print(f"  X-Frame-Options (Clickjacking): {headers.get('X-Frame-Options', 'Missing')}")
        print(f"  Content-Security-Policy (CSP): {'Present' if 'Content-Security-Policy' in headers else 'Missing'}")
        print(f"  Strict-Transport-Security (HSTS): {'Present' if 'Strict-Transport-Security' in headers else 'Missing'}")
    except Exception as e:
        print(f"  Header lookup error: {e}")

    # 3. Deep Tech Stack Fingerprinting
    print("\n[*] TECHNOLOGY STACK")
    try:
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        techs = wappalyzer.analyze_with_versions_and_categories(webpage)
        
        if not techs:
            print("  No recognizable stack signatures found.")
            
        grouped_tech = {}
        for tech, details in techs.items():
            for category in details['categories']:
                if category not in grouped_tech:
                    grouped_tech[category] = []
                
                version = f" (v{details['versions'][0]})" if details['versions'] else ""
                grouped_tech[category].append(f"{tech}{version}")
                
        # Print grouped by Wappalyzer's categories
        for category, items in sorted(grouped_tech.items()):
            print(f"  {category}:")
            for item in sorted(items):
                print(f"    - {item}")
                
    except Exception as e:
        print(f"  Tech stack analysis error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for target_url in sys.argv[1:]:
            analyze_website(target_url.strip())
    else:
        target_url = input("Enter website URL (e.g., https://example.com): ").strip()
        if target_url:
            analyze_website(target_url)
