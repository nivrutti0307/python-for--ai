import requests
from bs4 import BeautifulSoup
# Download a web page
response = requests.get("https://python.datalumina.com/getting-started/packages-and-pip")
print(response.status_code)  # Should print 200

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)