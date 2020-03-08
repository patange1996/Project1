from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

url = input("Link : ")

uclient = ureq(url)
page_html=uclient.read()
uclient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.find_all("div" , {"class" : "product-wrapper"})
#print(len(containers))
x=int(len(containers))
#print(soup.prettify(containers[1]))
for i in range(x):
    container = containers[i]
    link = container.find("div" , {"class" : "content"})
    print(link.h2.a["href"])







#print(container.div.meta.a["href"])
#print(container.div.meta["content"])
#print(link.span.img["alt"])
#remove = link.h2.a.text
#print(remove.strip())