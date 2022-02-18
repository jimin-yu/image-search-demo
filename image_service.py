import requests
import uuid
import os

class ImageService:

    def download_img(self, image_url):
        image_path = f'tmp/image-{uuid.uuid3(uuid.NAMESPACE_URL, image_url)}.jpeg'
        image_data = requests.get(image_url).content
        try:
            with open(image_path, 'wb') as handler:
                handler.write(image_data)
        except IOError as e:
            print(e)
            return False

        return image_path    


    def delete_img(self, image_path):
        os.unlink(image_path)    







