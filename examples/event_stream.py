import asyncio

from nomad import Client


async def main():
    async with Client("http://localhost:4646") as cli:
        async for events in cli.event_stream():
            print(events)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
