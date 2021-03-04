import json
from dataclasses import dataclass, field
from typing import AsyncGenerator, Optional

import aiohttp
from nomad.models import event_stream
from nomad.models.job import Job
from serde.json import from_json


@dataclass
class Config:
    """ Nomad Client Config """

    timeout: int = 3600  # Timeout for HTTP client.
    token: str = ""  # Nomad API token.


@dataclass
class Client:
    """ Nomad API Async Client """

    addr: str  # Nomad Address.
    cfg: Optional[Config] = None
    cli: Optional[aiohttp.ClientSession] = field(init=False, default=None)

    async def __aenter__(self):
        opts = {}
        if self.cfg:
            opts["timeout"] = aiohttp.ClientTimeout(total=self.cfg.timeout)

        headers = {}
        if self.cfg and self.cfg.token:
            headers["X-Nomad-Token"] = self.cfg.token
        self.cli = aiohttp.ClientSession(headers=headers, **opts)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.cli.close()

    async def event_stream(self) -> AsyncGenerator[event_stream.Events, None]:
        """ Subscribe event_stream """
        if not self.cli:
            raise Exception("Client session isn't started")

        async with self.cli.get(self.addr + "/v1/event/stream") as reader:
            async for raw in reader.content:
                line = raw.strip().decode()
                if not line or not json.loads(line):
                    continue
                events = from_json(event_stream.Events, line)
                yield events

    async def job(self, name: str) -> Job:
        """ Get job """
        if not self.cli:
            raise Exception("Client session isn't started")

        async with self.cli.get(self.addr + f"/v1/job/{name}") as res:
            text = await res.text()
            status = res.status
            if status != 200:
                raise Exception(text)
            return from_json(Job, text)

    async def jobs(self) -> list[Job]:
        """ Get job """
        if not self.cli:
            raise Exception("Client session isn't started")

        async with self.cli.get(self.addr + "/v1/jobs") as res:
            text = await res.text()
            status = res.status
            if status != 200:
                raise Exception(text)
            return from_json(list[Job], text)
