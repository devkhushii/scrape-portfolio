import requests
from bs4 import BeautifulSoup
url ="https://devkhushii.github.io/my-portfolio/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())
name=soup.find(class_="leftsection")
print(name.string)

image=soup.find("img")
print(image)
