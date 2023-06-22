from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/Apple-MacBook-Laptop-12%E2%80%91core-30%E2%80%91core/dp/B0BSHFCF13/ref=sr_1_3?keywords=macbook+pro+2022+laptop&sr=8-3"
headers = {
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}

response = requests.get(
    url,
    headers=headers,
).text

soup = BeautifulSoup(response, "html.parser")
product = soup.select_one("#titleSection #title #productTitle")
product_image = soup.select_one("#imgTagWrapperId img")
price = soup.select_one(".a-price")

print(product.text.strip())
print(product_image.get("src"))
print(f"Current price is ${price.text.split('$')[1]}")
