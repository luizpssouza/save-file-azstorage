# Import requests, shutil python module.
import requests
import shutil


def download(image_url: str):
    resp = requests.get(image_url, stream=True)
    blob = resp.content
    
    #save_file(resp.raw)

    del resp

    return blob

def save_file(raw):
    local_file = open('image.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(raw, local_file)