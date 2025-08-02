import argparse
from modules import passive, active
from datetime import datetime

def save_results(domain, subdomains):
    filename = f"results_{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        for sub in sorted(subdomains):
            f.write(sub + "\n")
    print(f"[+] Results saved to: {filename}")

def main():
    parser = argparse.ArgumentParser(description="SubScope - Subdomain Scanner")
    parser.add_argument("domain", help="Target domain (example.com)")
    parser.add_argument("-p","--passive", action="store_true", help="Run passive recon")
    parser.add_argument("-a","--active", action="store_true", help="Run DNS bruteforce")
    parser.add_argument("--all", action="store_true", help="Run both passive and active")
    parser.add_argument("-w","--wordlist", help="Path to wordlist for bruteforce")
    args = parser.parse_args()

    all_subdomains = set()

    if args.passive or args.all:
        all_subdomains.update(passive.from_crtsh(args.domain))
        all_subdomains.update(passive.from_hackertarget(args.domain))

    if args.active or args.all:
        if not args.wordlist:
            print("[-] --wordlist required for active scan.")
        else:
            all_subdomains.update(active.brute_dns(args.domain, args.wordlist))

    if all_subdomains:
        for sub in sorted(all_subdomains):
            print(f"[+] {sub}")
        save_results(args.domain, all_subdomains)
    else:
        print("[-] No subdomains found.")

if __name__ == "__main__":
    main()