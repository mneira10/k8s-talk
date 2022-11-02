from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
import requests


app = FastAPI()

id = random.randint(1, 10000)



@app.get("/", response_class=HTMLResponse)
async def root():
    print('POD ID:', id)
    url = "https://dog.ceo/api/breeds/image/random"

    random_dog_response = x = requests.get(url)
    dog_image_url = random_dog_response.json()['message']



    return f""" <html>
        <head>
            <title>Cool dog pictures</title>
        </head>
        <body>
            <h1>UpCodes K8s talk</h1>
            <h3>POD ID: {id}</h3>
            # TODO: insert special phrase here
            Cool dog pic:
            </br>
            <img src="{dog_image_url}"/>
        </body>
    </html>"""
