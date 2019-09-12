from download import download

def image_process():
    image_url = "https://www.dev2qa.com/demo/images/green_button.jpg"
    download(image_url)


if __name__ == "__main__":
    image_process()