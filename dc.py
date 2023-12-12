import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/jobs/"

req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser") 

job_posts = soup.find_all('h2', class_='listing-company')

for job_post in job_posts:
    title = job_post.a.text
    print(title)