from  fastapi import FastAPI
from  bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get('/')
def Home():
    return {"message":"welcome"}

@app.get('/query/{text}')
def IpsumSearchView(text: str):
    req = requests.get(f"https://en.wikipedia.org/wiki/{text}")
    req_decode = req.content.decode()
    soup  = BeautifulSoup(req_decode, "html.parser")
    p_tags = soup.find_all('p')
    response = ''
    counter = 0
    for item in p_tags:
        if counter < 5:
            if len(item.text) > 100:
                response += item.text
                counter += 1
        else:
            break
    return {"succeeded": True, "result": response}