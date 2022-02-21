from email.mime import image
import requests
import uuid
import os
import aiohttp
import aiofiles

class ImageService:

    # def download_img(self, image_url):
    #     image_path = f'tmp/image-{uuid.uuid3(uuid.NAMESPACE_URL, image_url)}.jpeg'
    #     response = requests.get(image_url, stream=True)
    #     if response.status_code == 200:
    #         with open(image_path, 'wb') as f:
    #             for chunk in response.iter_content(1024):
    #                 f.write(chunk)

    #     return image_path    

    async def download_img(self, image_url):
        image_path = f'tmp/image-{uuid.uuid3(uuid.NAMESPACE_URL, image_url)}.jpeg'
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status == 200:
                    with open(image_path, 'wb') as f:
                        async for chunk in resp.content.iter_chunked(1024):
                            f.write(chunk)

        return image_path                    
                      


    def delete_img(self, image_path):
        os.unlink(image_path)    

    


    




