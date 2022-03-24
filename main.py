import requests
from datetime import datetime

# ENTRY DETAILS
username = "davidofamerica"
token = "2348130207733babatundeibukun"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# CREATE A USERNAME AND TOKEN BY YOURSELF
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# CREATE A  CUSTOMIZED GRAPH
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
headers = {
    "X-USER-TOKEN": token
}

graph_id = "graph22"
graph_config = {
    "id": "graph22",
    "name": "codinghours",
    "unit": "hours",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# ADD TO THE HABIT TRACKER

today = datetime.now()

add_to_graph = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many hours did you code today? ")

}
add_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

response = requests.post(url=add_pixel_endpoint, json=add_to_graph, headers=headers)
print(response.text)

# update_pixel = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
#
# response = requests.put(url=update_pixel, json=add_to_graph, headers=headers)
# print(response.text)
