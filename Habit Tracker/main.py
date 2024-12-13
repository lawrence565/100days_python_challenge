import datetime

import requests
import dotenv, os

dotenv.load_dotenv()
TOKEN = os.getenv("HABIT_TRACKER_TOKEN")
USER = "lawrence565"
graph_id = "workout"
pixela_endpoint = "https://pixe.la/v1/users"


# Generate user
def create_user(request_url, token, username):
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=request_url, json=user_params)
    print(response.text)

def create_graph():
    endpoint = f"{pixela_endpoint}/{USER}/graphs"

    graph_config = {
        "id": "workout",
        "name": "My workout graph",
        "unit": "Hours",
        "type": "float",
        "color": "sora"
    }

    graph_header = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.post(url=endpoint, json=graph_config, headers=graph_header)
    print(response.text)

def add_pixel():
    endpoint = f"{pixela_endpoint}/{USER}/graphs/{graph_id}"

    today = datetime.datetime.today()
    format_day = today.strftime("%Y%m%d")

    graph_config = {
        "date": format_day,
        "quantity": "2",
    }

    graph_header = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.post(url=endpoint, json=graph_config, headers=graph_header)
    print(response.text)

def update_pixel():
    today = datetime.datetime.today()
    format_day = today.strftime("%Y%m%d")

    endpoint = f"{pixela_endpoint}/{USER}/graphs/{graph_id}/{format_day}"

    graph_config = {
        "quantity": "10",
    }

    graph_header = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.put(url=endpoint, json=graph_config, headers=graph_header)
    print(response.text)

def delete_pixel():
    today = datetime.datetime.today()
    format_day = today.strftime("%Y%m%d")

    endpoint = f"{pixela_endpoint}/{USER}/graphs/{graph_id}/{format_day}"

    graph_header = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.delete(url=endpoint, headers=graph_header)
    print(response.text)