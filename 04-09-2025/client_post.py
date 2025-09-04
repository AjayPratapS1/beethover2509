#pip install requests

import requests
BASE_URL = 'https://jsonplaceholder.typicode.com'

#Fetch all post : GET
posts_response = requests.get(f'{BASE_URL}/posts')
posts = posts_response.json()
print("Resopone of API's: ")
print(posts) 

# read by id : GET /posts/1
print('Consuming : Read Post By Id == 1...')
response = requests.get(f'{BASE_URL}/posts/1')
post = response.json()
print(post)

# create post : POST /posts {"userId":1, "title":"Some Title", "body" : "Some Body"}
print('Consuming : create post...')
post = {"userId":1, "title":"Some Title", "body" : "Some Body"}
response = requests.post(f'{BASE_URL}/posts', data = post)
createdPost = response.json()
print(createdPost)

# update post : PUT /posts/1 {"userId":1, "title":"Some Title", "body" : "Some Body"}
print('Consuming : update post...')
new_post = {"userId":1, "title":"Some Title", "body" : "Some Body"}
response = requests.put(f'{baseUrl}/posts/1', data = new_post)
updatedPost = response.json()
print(updatedPost)

# delete post : DELETE /posts/1
print('Consuming : delete post...')
response = requests.delete(f'{baseUrl}/posts/1')
if response.status_code == 200:
    print('Post Deleted Successfully')
else:
    print('Error in deletiing the post')