import requests
from bs4 import BeautifulSoup


def page_info(page_url, index):
    
    page_data = requests.get(page_url)
    
    soup = BeautifulSoup(page_data.content, "html.parser")

    title = soup.find(class_="postingtitle")

    posting_body = soup.find("section", {"id" : "postingbody"})


    with open(f"./dataset/{index}.txt", 'w', encoding='utf-8') as f:
        print(title.text.strip(), file=f)
        print(posting_body.text.strip(), file=f)
        f.close()



def field_search(page_url, count):
    
    page = requests.get(page_url)

    soup = BeautifulSoup(page.content, "html.parser")

    all_links = soup.find_all(class_="result-row")

    index = count

    for link in all_links:
        index = index + 1
        anchor = link.find('a')['href']
        page_info(anchor, index=index)

    return index
    

FIELDS_DICT = {
    # "communities" : "ccc",
    "events" : "eee",
    "sale" : "sss",
    "gigs" : "ggg",
    "housing" : "hhh",
    "jobs" : "jjj",
    "resumes" : "rrr",
    "services" : "bbb"
}


count  = 0

for field in FIELDS_DICT.items() :
    
    _ , val = field

    page_url = f"https://bangalore.craigslist.org/search/{val}?"
    
    count = field_search(page_url, count=count)
    


