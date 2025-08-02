import requests
import re

def is_valid_subdomain(sub, domain):
    if "*" in sub:  
        return False
    if "@" in sub:  
        return False
    if not sub.endswith(domain):
        return False
    if re.search(r"\s", sub):
        return False
    return True

def from_crtsh(domain):
    print("[*] Querying crt.sh ...")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        subdomains = set()
        for entry in data:
            for sub in entry['name_value'].split('\n'):
                cleaned = sub.strip().lower()
                if is_valid_subdomain(cleaned, domain):
                    subdomains.add(cleaned)
        return subdomains
    except Exception as e:
        print(f"[-] crt.sh failed: {e}")
        return set()

def from_hackertarget(domain):
    print("[*] Querying hackertarget ...")
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    try:
        r = requests.get(url, timeout=10)
        lines = r.text.strip().split("\n")
        return set([line.split(",")[0] for line in lines if domain in line])
    except:
        print("[-] hackertarget failed.")
        return set()