from bs4 import BeautifulSoup
import requests
import urllib.parse
import os
import sys
import threading
import time

def cls():
    os.system("cls" if os.name == "nt" else "clear")

waiting = False
def animate():
    spinnerChars = ["|", "/", "—", "\\"]
    while waiting:
        for i in range(4):
            if not waiting:
                break
            sys.stdout.write("\b" + spinnerChars[i])
            sys.stdout.flush()
            time.sleep(0.65)

def start_animate():
    global waiting
    waiting = True
    sys.stdout.write("Fetching product info. Please wait...  ")
    threading.Thread(target=animate).start()

def scrape_website(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print("\nError fetching page:", e)
        return None

def scrape_amazon():
    global waiting
    searchQuery = input("\nPlease enter a search query: ")
    cls()
    start_animate()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    url = "https://www.amazon.com/s?k=" + urllib.parse.quote_plus(searchQuery)
    html_content = scrape_website(url, headers)
    if not html_content:
        waiting = False
        print("Failed to fetch Amazon search results.")
        return

    soup = BeautifulSoup(html_content, "html.parser")
    prices = []
    names = []
    links = []
    for i in soup.select(".s-result-item"):
        try:
            itmLink = i.select_one('a.a-link-normal.a-text-normal')
            itmPrice = i.select_one('.a-offscreen')
            if itmLink is not None and itmPrice is not None:
                itmId = itmLink['href'].split("/dp/")[1].split("/")[0]
                name = itmLink.text.strip()
                price = float(str(itmPrice.text).replace("$", "").replace(",", ""))
                link = "https://www.amazon.com/dp/" + itmId
                names.append(name)
                prices.append(price)
                links.append(link)
        except:
            continue
    waiting = False
    if len(prices) == 0:
        print("\nNo results found.")
        return
    priceAvg = sum(prices) / len(prices)
    maxPriceIndex = prices.index(max(prices))
    minPriceIndex = prices.index(min(prices))
    cls()
    print("-- RESULTS FOR \"" + searchQuery + "\" --\n")
    print(f'The average price of "{searchQuery}" is: ${priceAvg:.2f}')
    print("\nHighest price found: $" + str(prices[maxPriceIndex]) + f'\nName: "{names[maxPriceIndex]}"\nLink: {links[maxPriceIndex]}')
    print("\nLowest price found: $" + str(prices[minPriceIndex]) + f'\nName: "{names[minPriceIndex]}"\nLink: {links[minPriceIndex]}\n')

def scrape_ebay():
    global waiting
    searchQuery = input("\nPlease enter a search query: ")
    cls()
    start_animate()
    url = "https://www.ebay.com/sch/i.html?_nkw=" + urllib.parse.quote(searchQuery) + "&LH_BIN=1"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    html_content = scrape_website(url, headers)
    if not html_content:
        waiting = False
        print("\nFailed to fetch eBay search results.")
        return

    soup = BeautifulSoup(html_content, "html.parser")
    prices = []
    names = []
    links = []
    for i in soup.find_all(class_="s-item"):
        itmLink = i.findChildren(class_="s-item__link", recursive=True)
        itmPrice = i.findChildren(class_="s-item__price", recursive=True)
        itmName = i.findChildren(class_="s-item__title", recursive=True)
        itmId = itmLink[0].attrs["href"].split("/")[-1].split("?")[0]
        if itmId == "123456":
            continue
        try:
            price = float(str(itmPrice[0]).split("$")[1].split("<")[0].replace(",", ""))
            name = itmName[0].text.strip().replace("New Listing", "")
            link = "https://www.ebay.com/itm/" + itmId 
        except:
            continue
        names.append(name)
        prices.append(price)
        links.append(link)
    waiting = False
    priceAvg = sum(prices) / len(prices) if prices else 0
    maxPriceIndex = prices.index(max(prices))
    minPriceIndex = prices.index(min(prices))
    cls()
    print("-- RESULTS FOR \"" + searchQuery + "\" --\n")
    print(f'The average price of "{searchQuery}" is: ${priceAvg:.2f}')
    print("\nHighest price found: $" + str(prices[maxPriceIndex]) + f'\nName: "{names[maxPriceIndex]}"\nLink: {links[maxPriceIndex]}')
    print("\nLowest price found: $" + str(prices[minPriceIndex]) + f'\nName: "{names[minPriceIndex]}"\nLink: {links[minPriceIndex]}')
    print("\n(Only \"Buy It Now\" listings are processed)\n")

def main():
    cls()
    print("-- WELCOME --")
    print("What store should would you like to scrape?")
    print("Please type an option and press enter:\n")
    print("1 - Amazon")
    print("2 - eBay")
    choice = input("\nChoice: ")
    if choice == "1":
        scrape_amazon()
    elif choice == "2":
        scrape_ebay()
    else:
        cls()
        sys.exit("Invalid input")

if __name__ == "__main__":
    main()