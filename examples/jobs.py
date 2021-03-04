import asyncio

from nomad import Client


async def main():
    print("Get all jobs.")
    async with Client("http://localhost:4646") as cli:
        for job in await cli.jobs():
            print(job)
    print("\nGet job by name. Enter job name:")
    name = input()
    async with Client("http://localhost:4646") as cli:
        print(await cli.job(name))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
