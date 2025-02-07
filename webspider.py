import requests
import threading
import time
import argparse
from urllib.parse import urlparse, urljoin
from colorama import Fore, Style, init
from tqdm import tqdm  # For progress bar

# Initialize Colorama
init(autoreset=True)

def banner():
    print(Fore.BLUE + """
  _   _                             _       
 | | | |_   _ _ __   ___ _ __ _   _| |_ ____
 | |_| | | | | '_ \ / _ \ '__| | | | __|_  /
 |  _  | |_| | |_) |  __/ |  | |_| | |_ / /   
 |_| |_|\__, | .__/ \___|_|   \__,_|\__/___|
        |___/|_|                            

          Advanced Open Redirection Scanner (webSpider)
                   By: Hyperutz 
    """ + Style.RESET_ALL)

# Argument Parsing
def get_args():
    parser = argparse.ArgumentParser(description="Enhanced Open Redirection Scanner")
    parser.add_argument('-u', '--url', required=True, help="Target URL")
    parser.add_argument('-p', '--payloads', required=True, help="Payload file path")
    parser.add_argument('-t', '--threads', type=int, default=50, help="Number of threads (Default: 50)")
    parser.add_argument('-w', '--whitelist', help="Whitelisted domain")
    parser.add_argument('-c', '--cookies', help="Cookies (Format: key1=value1; key2=value2)")
    parser.add_argument('--proxy', help="Proxy (Format: http://127.0.0.1:8080)")
    parser.add_argument('--output', help="Output file to save results")
    return parser.parse_args()

def load_payloads(file_path, whitelist=None):
    with open(file_path, 'r') as f:
        payloads = [line.strip().replace('%whitelist%', whitelist) if whitelist else line.strip() for line in f]
    print(Fore.GREEN + f"[+] Loaded {len(payloads)} payloads")
    return payloads

def parse_cookies(cookie_str):
    if not cookie_str:
        return None
    cookies = {}
    for pair in cookie_str.split(';'):
        try:
            key, value = pair.strip().split('=', 1)
            cookies[key] = value
        except ValueError:
            continue
    return cookies

def test_payload(url, payload, cookies=None, proxy=None):
    full_url = urljoin(url, f'?{urlparse(url).query.split("=")[0]}={payload}')
    proxies = {'http': proxy, 'https': proxy} if proxy else None
    try:
        response = requests.get(full_url, allow_redirects=False, cookies=cookies, proxies=proxies, timeout=5)
        if 'Location' in response.headers:
            redirected_domain = urlparse(response.headers['Location']).netloc
            if redirected_domain and redirected_domain != urlparse(url).netloc:
                print(Fore.RED + f"[!] VULNERABLE: {full_url} -> {response.headers['Location']}")
                return full_url
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"[-] Error: {e}")
    return None

def worker(url, payloads, cookies, proxy, results, progress_bar):
    for payload in payloads:
        result = test_payload(url, payload, cookies, proxy)
        if result:
            results.append(result)
        progress_bar.update(1)

def main():
    banner()
    args = get_args()
    payloads = load_payloads(args.payloads, args.whitelist)
    cookies = parse_cookies(args.cookies)
    
    results = []
    threads = []
    chunk_size = len(payloads) // args.threads or 1
    
    with tqdm(total=len(payloads), desc="Scanning", unit="payload") as progress_bar:
        for i in range(0, len(payloads), chunk_size):
            chunk = payloads[i:i + chunk_size]
            thread = threading.Thread(target=worker, args=(args.url, chunk, cookies, args.proxy, results, progress_bar))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
    
    if args.output and results:
        with open(args.output, 'w') as f:
            for line in results:
                f.write(line + '\n')
        print(Fore.CYAN + f"[+] Results saved to {args.output}")
    
if __name__ == "__main__":
    main()

