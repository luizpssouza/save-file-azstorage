import io
from PIL import Image
from resizeimage import resizeimage

from azure.storage.blob import BlockBlobService, ContentSettings

from environment import Env


def resize(blob, size=[50, 50]):
    img = Image.open(io.BytesIO(blob))
    img = resizeimage.resize_thumbnail(img, size)
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='jpeg')
    return imgByteArr.getvalue()


def save_blob(blob):
    blob = resize(blob, size=[50,50])

    block_blob_service = get_blob_service()
    
    env = Env()
    block_blob_service.create_blob_from_bytes(
        env.AZURE_STORAGE_CONTAINER,
        f'{env.AZURE_STORAGE_SUBFOLDER}/local_image1.jpg',
        blob=blob,
        content_settings=ContentSettings(content_type='image/png')
    )


def save_file_image():
    block_blob_service = get_blob_service()

    env = Env()
    block_blob_service.create_blob_from_path(
        env.AZURE_STORAGE_CONTAINER,
        f'{env.AZURE_STORAGE_SUBFOLDER}/image.jpg',
        'image.jpg',
        content_settings=ContentSettings(content_type='image/png')
    )


def get_blob_service():
    env = Env()
    block_blob_service = BlockBlobService(
        connection_string=env.AZURE_STORAGE_CONNECTIONSTRING
    )

    return block_blob_service