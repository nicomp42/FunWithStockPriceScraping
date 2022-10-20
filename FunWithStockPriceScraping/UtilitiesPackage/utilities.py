# utilities.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu
# Study these functions and you can use them in your projects. 

from bs4 import BeautifulSoup
import sys
import requests

def get_stock_price(symbol):
    # We can paste the URL below into our browser to examine the web page. 
    page = requests.get("https://finance.yahoo.com/quote/" + symbol)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("fin-streamer", {"data-symbol":symbol})  # Note the dictionary
    #print(price)
    #print (price.get_text())
    return price.get_text()   # get_text() provides the value attribute

def get_stock_current_market_cap(symbol):
    # We may have to randomly edit the the request headers so the web server will respond to us
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.147 Safari/537.34','Accept-Language': 'en-US, en;q=0.5'})
    
    '''
    The URL is correct but when we submit it through requests.get() we get a 404 error unless we edit the headers periodically.
    '''
    market_cap = 0
    # We can paste the URL below into our browser to examine the web page. 
    # <td class="Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor)">264.35B</td>
    url = "https://finance.yahoo.com/quote/" + symbol + "/key-statistics?p=" + symbol
    #print (url)
    page = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    tds = soup.find_all("td", class_="Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor)")
    #for td in tds:
    #    print("td", td.get_text())
    market_cap = tds[0]
    #print (open.get_text())
    return market_cap.get_text()   # get_text() provides the value attribute

def demo():
    '''
    Test our functions
    '''
    price = get_stock_price("GOOGL")
    print("nicholdw: GOOGL Price", price)
    market_cap = get_stock_current_market_cap("GOOGL")
    print("nicholdw: GOOGL Market Cap", market_cap)
    
    
    price = get_stock_price("LUCY")
    print("Jundisa: LUCY Price", price)
    market_cap = get_stock_current_market_cap("LUCY")
    print("Jundisa: LUCY Market Cap", market_cap)
    
def buildPortfolio():
    # Build a Portfolio and scrape that
    myPortfolio = {"Google":"GOOGL", "Coke":"KO","Procter and Gamble":"PG","Home Depot":"HD"}
#    for i in range(0,100000000):
    for key in myPortfolio:
        print(myPortfolio[key] + "...")
        price = get_stock_price(myPortfolio[key])
        print(key + ":" + price)
