import requests
from PIL import Image
from io import BytesIO
import passkey

def background_remover(api_key, image_path):
    api_url = "https://api.remove.bg/v1.0/removebg"

    original_image = Image.open(image_path)
    original_image.show(title="Original Image")

    image_bytes = BytesIO()
    original_image = original_image.convert("RGB")
    original_image.save(image_bytes, format="JPEG")


    headers = {
        "X-Api-Key": api_key,
    }

    response = requests.post(api_url, headers=headers, files={"image_file": image_bytes.getvalue()})

    if response.status_code == 200:
        result_image = Image.open(BytesIO(response.content))
        result_image.show(title="Image with Removed Background")
    else:
        print(f"Error: {response.status_code} - {response.text}")

api_key = passkey.api_key
image_path = "img-path"

background_remover(api_key, image_path)
