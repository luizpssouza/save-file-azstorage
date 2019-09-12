import os

from azstorage import save_blob
from download import download
from environment import setEnvironmentVariables

setEnvironmentVariables()
 
def process():
    image_url = "https://www.dev2qa.com/demo/images/green_button.jpg"
    blob = download(image_url)
    save_blob(blob)

if __name__ == "__main__":
    process()