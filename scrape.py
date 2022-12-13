from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
              'Accept-Language': 'en-US'})

url = "https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf&hl=en&gl=US"

webpage = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "lxml")

links = soup.find_all("a", attrs={'class':'Fd93Bb ynrBgc xwcR9d'})
try:
    title_string = soup.find("h1", attrs={"class": 'Fd93Bb ynrBgc xwcR9d'}).string.strip()
except Exception as e:
    title_string = " "


print(title_string)





URL=input()

webpage1 = requests.get(URL, headers=HEADERS)
soup1 = BeautifulSoup(webpage1.content, "lxml")


links1 = soup1.find_all("a", attrs={'class':'Si6A0c Gy4nib'})


links_list=[]
max=0.0
maxtitle=" "
for link in links1:
    links_list.append(link['href'])
    print(link['href'])

for link in links_list:
    new_webpage = requests.get("https://play.google.com" + link,headers=HEADERS)

    new_soup = BeautifulSoup(new_webpage.content, "lxml")

    try:

        title_string = new_soup.find("h1", attrs={"itemprop":'name'}).string.strip()

    except:
        title_string = ""
    try:
        rating=new_soup.find("div", attrs={"class":'jILTFe'}).string.strip()


    except :
        rating="0"
    if float(max)<float(rating):
        max=rating
        maxtitle=title_string

    print(title_string)
    print(rating)
print(maxtitle)
print(max)
