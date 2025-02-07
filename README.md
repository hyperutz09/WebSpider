# WEB SPIDER

## 📌 Overview
**WEB SPIDER** is an advanced open redirection scanner designed to test URLs for open redirection vulnerabilities efficiently. It can handle authenticated endpoints, use proxies, and test custom payloads at high speed. This tool is ideal for penetration testers, security researchers, and bug bounty hunters looking to automate open redirection testing across multiple endpoints. With its robust multi-threaded scanning capabilities, it can test thousands of payloads in a matter of seconds, ensuring comprehensive coverage of potential vulnerabilities.

## 🚀 Features
- **Fast Scanning**: Supports multi-threaded execution for quick results.
- **Authenticated Testing**: Provides cookie-based authentication.
- **Custom Payload Injection**: Dynamically generates and injects payloads.
- **Proxy Support**: Routes requests through an external proxy.
- **Progress Tracking**: Displays real-time scanning progress with `tqdm`.
- **Logging and Output Saving**: Allows saving results to a file.

## 🔧 Installation
Ensure you have Python **3.7 or later** installed. Then, install dependencies:
```bash
pip install requests colorama tqdm
```

## 📂 Usage
### Basic Scan:
```bash
python webspider.py -u <TARGET_URL> -p payloads.txt
```
### Multi-threaded Scan:
```bash
python webspider.py -u <TARGET_URL> -p payloads.txt -t 50
```
### Using Authentication (Cookies):
```bash
python webspider.py -u <TARGET_URL> -p payloads.txt -c "SESSIONID=xyz"
```
### Using a Proxy:
```bash
python webspider.py -u <TARGET_URL> -p payloads.txt --proxy http://127.0.0.1:8080
```
### Saving Results to a File:
```bash
python webspider.py -u <TARGET_URL> -p payloads.txt --output results.txt
```

## ⚡ Options
| Flag | Description |
|------|-------------|
| `-u, --url` | Target URL to scan |
| `-p, --payloads` | File containing payloads |
| `-t, --threads` | Number of threads (default: 50) |
| `-w, --whitelist` | Specify a whitelist domain |
| `-c, --cookies` | Set authentication cookies |
| `--proxy` | Use an HTTP proxy for requests |
| `--output` | Save results to a file |

## 🛠 Dependencies
- `requests`
- `colorama`
- `tqdm`

## 📜 License
This tool is for educational and security testing purposes only. Use responsibly.

---
**Author: Hyperutz**


