import requests
from bs4 import BeautifulSoup
import json
import sys
from termcolor import colored

def get_subdomains(domain):
    subdomains = set()
    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            for item in data:
                subdomains.add(item['name_value'])
            return list(subdomains)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def check_subdomain_takeover(subdomain):
    try:
        response = requests.get(f"http://{subdomain}", timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def subdomain_takeover_scan(domain):
    subdomains = get_subdomains(domain)
    if subdomains:
        print("\n[+]",colored("Subdomains found: ",'green'))
        for subdomain in subdomains:
            print("[-]",colored(subdomain,'blue'))
            if check_subdomain_takeover(subdomain):
                print(colored(f"[+] {subdomain} may be vulnerable to subdomain takeover.",'red'))
            else:
                print(colored(f"[-] {subdomain} does not appear to be vulnerable to subdomain takeover.",'green'))
    else:
        print(colored("[-] No subdomains found",'red'))

if len(sys.argv) != 2:
    print(colored("Usage: python3 script.py domain.com",'red'))
    sys.exit()

domain = sys.argv[1]
subdomain_takeover_scan(domain)