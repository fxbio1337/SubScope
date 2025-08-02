# DNS brute force
import socket

def brute_dns(domain, wordlist_path):
    print("[*] Starting DNS brute force...")
    found = set()

    try:
        with open(wordlist_path, "r") as f:
            for line in f:
                sub = line.strip()
                full = f"{sub}.{domain}"
                try:
                    ip = socket.gethostbyname(full)
                    print(f"[+] {full} -> {ip}")
                    found.add(full)
                except socket.gaierror:
                    pass
    except FileNotFoundError:
        print("[-] Wordlist not found.")
    return found