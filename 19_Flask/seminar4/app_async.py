import asyncio

import aiofiles
import aiohttp

from utils import logger, timer


@timer
async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
    return data


async def write_data(data, filename):
    async with aiofiles.open(filename, "wb") as f:
        await f.write(data)


async def process(url, filename_prefix):
    data = await download_image(url)
    filename = f"{filename_prefix}.png"
    await write_data(data, filename)


async def runner(urls):
    tasks = [
        asyncio.create_task(process(url, filename_prefix))
        for filename_prefix, url in enumerate(urls)
    ]
    await asyncio.gather(*tasks)
    logger.info("All async processes exited")


@timer
def main_async(urls):
    asyncio.run(runner(urls))
