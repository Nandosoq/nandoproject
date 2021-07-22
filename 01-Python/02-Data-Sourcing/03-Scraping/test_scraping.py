from bs4 import BeautifulSoup

soup = BeautifulSoup(open("pages/chocolate.html"), "html.parser")

for recipe in soup.find_all('p', class_='recipe-name'):
    print(recipe.text)
#recipes > div.row > div:nth-child(2)
