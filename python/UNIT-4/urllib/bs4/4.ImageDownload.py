import requests

response = requests.get("https://cdn.pixabay.com/photo/2021/12/19/03/51/tree-6880117_960_720.jpg")
file = open("./images/tree.jpg", "wb")
file.write(response.content)
file.close()
