from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import csv

Links_csv = "Links.csv"
f=open(Links_csv,'w')
headers = "Links found\n"
f.write(headers)

nxt_link= ""
url = input("Link : ")

uclient = ureq(url)
page_html=uclient.read()
uclient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.find_all("div" , {"class" : "product-wrapper"})

x=int(len(containers))
y=x
for i in range(x):
    container = containers[i]
    link = container.find("div" , {"class" : "content"})
    links_found = link.h2.a["href"]
    f.write(links_found + "\n")

track = 1
print("Done")
nxt = page_soup.find("li" , {"rel" : "next"})
if nxt is None:
    nxt = "none"


while len(nxt) == 3:
    nxt_link = "https:" + str(nxt.a["href"].strip())
    uclient1 = ureq(nxt_link)
    page_html = uclient1.read()
    uclient1.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div", {"class": "product-wrapper"})

    x = int(len(containers))
    y=y+x
    for i in range(x):
        container = containers[i]
        link = container.find("div", {"class": "content"})
        links_found = link.h2.a["href"]
        f.write(links_found + "\n")

    track=track+1
    print("Done")
    nxt = page_soup.find("li", {"rel": "next"})
    if nxt is None:
        nxt="none"
f.close()
print(str(track) + " Pages scanned")
print(str(y) + " Links found")

