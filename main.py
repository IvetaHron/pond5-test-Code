# Import Requests library
import requests
# Beautiful Soup is a Python library for pulling data out of HTML file.
from bs4 import BeautifulSoup

# Creating Response object called r with HTTP request type GET
r = requests.get('https://www.pond5.com/photo/11497188')

# Creating a BeautifulSoup object 
soup = BeautifulSoup(r.text, 'html.parser')

# Extracting image information  
title = soup.find(property="og:title")
description = soup.find(property="og:description")
type_img = soup.find(property="og:image:type")
height = soup.find(property="og:image:height")
width = soup.find(property="og:image:width")
address= soup.find(property="og:image:url")

# Pong to the ping - checking the response status code, should be 200 if there is successful response
print(r.status_code)

# Returns server's response headers with service version and system information 
print (r.headers)

# Returns server name 
print (r.headers['server'])

# Returns content type 
print (r.headers['content-type'])

# Returns image information: title, description, image type, dimensions and url.
print(title)
print(description)
print(type_img)
print(height)
print(width)
print(address)

