from bs4 import BeautifulSoup
import lxml

with open("Day45/bs4-start/website.html", encoding='utf-8') as file:
	content = file.read()
	# print(content)

soup = BeautifulSoup(content, "lxml")

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())


all_list_elements = soup.find_all("li") #find all list elements
print("List of elements ")
print("=================")
for list_el in all_list_elements:
	print(list_el.getText())

print()
print("Anchor tags")
print("=================")
anchor_tags = soup.find_all("a") #find all anchor tags
for anchor_tag in anchor_tags:
	print(anchor_tag.get("href"))


print()
print("Search by element and id")
print("=================")
h1 = soup.find(name="h1", id="name")
print(h1)

print()
print("Search by class attribute")
print("=================")
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)


print()
print("Search by using selectors nested")
print("=================")
company_url = soup.select_one(selector="p a") #css selector
print(company_url)

print()
print("Search by using selector id")
print("=================")
name = soup.select_one(selector="#name") #css selector
print(name)

print()
print("Search by using selector class")
print("=================")
headings = soup.select(selector=".heading") #css selector
print(headings)