import requests
from bs4 import BeautifulSoup


def page_info(page_url, category, index):
    
    page_data = requests.get(page_url)
    
    soup = BeautifulSoup(page_data.content, "html.parser")

    title = soup.find(class_="postingtitle")

    posting_body = soup.find("section", {"id" : "postingbody"})


    with open(f"./dataset/{category}{index}.txt", 'w', encoding='utf-8') as f:
        print(title.text.strip(), file=f)
        print(posting_body.text.strip(), file=f)
        f.close()



def field_search(page_url, category):
    
    page = requests.get(page_url)

    soup = BeautifulSoup(page.content, "html.parser")

    all_links = soup.find_all(class_="result-row")

    count = 0

    for link in all_links:
        count = count + 1
        anchor = link.find('a')['href']
        page_info(anchor, category=category, index=count)

FIELDS_DICT = {
    "communities" : "ccc",
    "events" : "eee",
    "sale" : "sss",
    "gigs" : "ggg",
    "housing" : "hhh",
    "jobs" : "jjj",
    "resumes" : "rrr",
    "services" : "bbb"
}

for field in FIELDS_DICT.items() :
    
    category, val = field

    page_url = f"https://bangalore.craigslist.org/search/{val}?"
    
    field_search(page_url, category=category)
    


