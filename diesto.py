import unirest
import json

# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/types/Spell?collectible=1",
  headers={
    "X-Mashape-Key": "b5Sb4BFuQumsh47tlzgnTPA17gJjp1X1SJrjsnHzxsIGs7igHc"
  }
)
 
f = open('response.txt', 'w')
f.write(json.dumps(response.body, sort_keys=True, indent=4, separators=(',', ': ')))


# for collection in response.body.keys():
# 	for card in response.body[collection]:
# 		if card["type"] == "Minion":
# 			print card["name"]

for card in response.body:
	if "$" in card["text"]:
		print card["name"]