from bs4 import BeautifulSoup as soup
import urllib.request
import csv

Links_csv = "Links.csv"
f=open(Links_csv,'w')
headers = "Links found\n"
f.write(headers)

nxt_link= ""
url = input("Link : ")

req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
)
op = urllib.request.urlopen(req)
# uclient = ureq(url)
page_html = op.read().decode('utf-8')
# uclient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.find_all("div", {"data-test": "mms-product-card"})

x = int(len(containers))
y = x
for i in range(x):
    container = containers[i]
    links_found = container.div.div.a["href"]
    f.write(links_found + "\n")

#### The pagination logic is expired as the site included a button #####
# track = 1
# print("Done")
# nxt = page_soup.find("li", {"rel": "next"})
# if nxt is None:
#     nxt = "none"
#
#
# while len(nxt) == 3:
#     nxt_link = "https:" + str(nxt.a["href"].strip())
#     uclient1 = ureq(nxt_link)
#     page_html = uclient1.read()
#     uclient1.close()
#     page_soup = soup(page_html, "html.parser")
#     containers = page_soup.find_all("div", {"class": "product-wrapper"})
#
#     x = int(len(containers))
#     y=y+x
#     for i in range(x):
#         container = containers[i]
#         link = container.find("div", {"class": "content"})
#         links_found = link.h2.a["href"]
#         f.write(links_found + "\n")
#
#     track=track+1
#     print("Done")
#     nxt = page_soup.find("li", {"rel": "next"})
#     if nxt is None:
#         nxt="none"
f.close()
# print(str(track) + " Pages scanned")
# print(str(y) + " Links found")
