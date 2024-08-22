import requests


url = "https://74668b02-6282-4d4c-a82a-1a91ab19ea71-00-3ouz6bb3q97zz.janeway.replit.dev/get_users"


prms = {"user_id": "4321"}

res = requests.get(url, params=prms)


print(res.json())
