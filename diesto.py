import unirest

# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards",
  headers={
    "X-Mashape-Key": "b5Sb4BFuQumsh47tlzgnTPA17gJjp1X1SJrjsnHzxsIGs7igHc"
  }
)
 
f = open('response.txt', 'w')
f.write(response.raw_body)
