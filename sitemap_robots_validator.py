import requests
from urllib.parse import urljoin

def check_url_status(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"✅ Found: {url}")
            print(f"   ➤ Status Code: {response.status_code}")
            print(f"   ➤ Content Type: {response.headers.get('Content-Type', 'Unknown')}\n")
        else:
            print(f"⚠️ {url} returned status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"❌ Error accessing {url}: {e}")

def main():
    base_url = input("Enter the website URL (include https://): ").strip().rstrip('/')
    
    sitemap_url = urljoin(base_url, '/sitemap.xml')
    robots_url = urljoin(base_url, '/robots.txt')

    print("\n🔎 Validating SEO files...\n")
    
    print("🗺️ Checking sitemap.xml:")
    check_url_status(sitemap_url)

    print("🤖 Checking robots.txt:")
    check_url_status(robots_url)

if __name__ == "__main__":
    main()
