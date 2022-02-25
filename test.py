
import requests

project_key = 'RS_P_1495608305106685963'
token = 'v5sRS_P_1495608305106685963s1496806325613631987'
api_key = 'RS5:4b3a13283a9bb7d262d8b3fae525b34e'

# Authentication API
# url = "https://api.sports.roanuz.com/v5/core/{}/auth/".format(project_key)
# payload = {
#     'api_key': api_key
# }
# response = requests.post(url, json=payload)

# print(response.json())

# Association List
# print("Association List API")
# url = "https://api.sports.roanuz.com/v5/cricket/{}/association/list/".format(
#     project_key)
# headers = {
#     'rs-token': token
# }
# response = requests.get(url, headers=headers)

# print(response.json())

# Country List
# print("Country List API")
# url = "https://api.sports.roanuz.com/v5/cricket/{}/country/list/".format(
#     project_key)
# headers = {
#     'rs-token': token
# }
# response = requests.get(url, headers=headers)

# print(response.json())


# Featured List
# url = "https://api.sports.roanuz.com/v5/cricket/{}/featured-tournaments/".format(
#     project_key)
# headers = {
#     'rs-token': token
# }
# response = requests.get(url, headers=headers)

# print(response.json())


# Featured Matches
tournament_key = "nzwindw_2022"
url = "https://api.sports.roanuz.com/v5/cricket/{}/tournament/{}/featured-matches/".format(
    project_key, tournament_key)
headers = {
    'rs-token': token
}
response = requests.get(url, headers=headers)

print(response.json())
