import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://example-blog.com'  # Replace with the target URL

# Send a request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article titles and links (customize the tag and class based on the webpage structure)
    articles = soup.find_all('article')  # Adjust the tag name as per your target website

    for article in articles:
        # Assuming the title is within an <h2> tag and the link within an <a> tag
        title_tag = article.find('h2')
        link_tag = article.find('a')

        if title_tag and link_tag:
            title = title_tag.text.strip()
            link = link_tag['href']
            print(f'Title: {title}')
            print(f'Link: {link}')
            print('-' * 40)
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
