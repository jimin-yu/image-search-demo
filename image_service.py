import uuid
import os
import aiohttp
import aiofiles

class ImageService:
    async def download_img(self, image_url):
        image_path = f'tmp/image-{uuid.uuid3(uuid.NAMESPACE_URL, image_url)}.jpeg'
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status == 200:
                    async with aiofiles.open(image_path, mode='wb') as f:
                        async for chunk in resp.content.iter_chunked(1024):
                            await f.write(chunk)

        return image_path                    
                      

    def delete_img(self, image_path):
        os.remove(image_path)    







