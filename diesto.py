import unirest
import json

# These code snippets use an open-source library. http://unirest.io/python
# API Call to get JSON of all collectible spells
response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/types/Spell?collectible=1",
  headers={
    "X-Mashape-Key": "b5Sb4BFuQumsh47tlzgnTPA17gJjp1X1SJrjsnHzxsIGs7igHc"
  }
)
 
#Parse through response and write out to response.txt
f = open('response.txt', 'w')
f.write(json.dumps(response.body, sort_keys=True, indent=4, separators=(',', ': ')))

#Parse through collectible spells and find all that deal damage, store in damage_spells list
damage_spells = []
for card in response.body:
	if "$" in card["text"]:
		# print card["name"]
		damage_spells.append(card)

#Write out damage_spells list to damage_spells.txt
with open('damage_spells.json', 'w') as outfile:
	json.dump(damage_spells, outfile, sort_keys=True, indent=4, separators=(',', ': '))

#Read in fixed file of damage spells
with open('damage_spells_expanded.txt') as data_file:    
    data = json.load(data_file)

print data