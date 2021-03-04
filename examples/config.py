import asyncio

from nomad import Client, Config


async def main():
    cfg = Config(timeout=30, token="<PUT YOUR NOMAD TOKEN")
    async with Client("http://localhost:4646", cfg) as cli:
        print(await cli.jobs())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
