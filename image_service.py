import requests
import uuid
import os

class ImageService:

    def download_img(self, image_url):
        image_path = f'tmp/image-{uuid.uuid3(uuid.NAMESPACE_URL, image_url)}.jpeg'
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

        return image_path    


    def delete_img(self, image_path):
        os.unlink(image_path)    

    


    




