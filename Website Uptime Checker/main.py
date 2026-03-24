import requests
import time

# List of websites to monitor
websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://example.com"
]

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {url} is UP")
        else:
            print(f"⚠️ {url} returned status {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"❌ {url} is DOWN")

def monitor():
    while True:
        print("\n--- Checking Websites ---")
        for site in websites:
            check_website(site)
        
        time.sleep(10)  # check every 10 seconds

if __name__ == "__main__":
    monitor()