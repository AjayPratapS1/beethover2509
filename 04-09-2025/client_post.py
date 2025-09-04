#pip install requests

import requests
BASE_URL = 'https://jsonplaceholder.typicode.com'

posts_response = requests.get(f'{BASE_URL}/posts')
posts = posts_response.json()
print("Resopone of API's: ")
# print(posts) 
print(posts[1])

