import requests
from datetime import datetime

USERNAME = "spam93"
TOKEN = "asjhdvasjvasjbak"
GRAPH_ID = "graph193"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph193",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2024, month=5, day=14)
# print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": "20240515",
    "quantity": "20",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "5.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)