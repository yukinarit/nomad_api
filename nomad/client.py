import json
import logging
from dataclasses import dataclass, field
from typing import AsyncGenerator, Optional

import aiohttp
from nomad.models import WriteOptions, event_stream
from nomad.models.job import Job, RegisterOptions
from serde.json import from_json

log = logging.getLogger("nomad")


@dataclass
class Config:
    """ Nomad Client Config """

    timeout: int = 60 * 60 * 24 * 365 * 10  # Timeout for HTTP client.
    token: str = ""  # Nomad API token.


@dataclass
class Client:
    """
    Nomad API Async Client
    """

    addr: str  # Nomad Address.
    cfg: Optional[Config] = field(default_factory=Config)
    ses: Optional[aiohttp.ClientSession] = field(init=False, default=None)

    async def __aenter__(self):
        opts = {"timeout": aiohttp.ClientTimeout(total=self.cfg.timeout)}

        headers = {}
        if self.cfg.token:
            headers["X-Nomad-Token"] = self.cfg.token

        self.ses = aiohttp.ClientSession(headers=headers, **opts)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.ses.close()

    def _check_session(self) -> aiohttp.ClientSession:
        """
        Check session is established
        """
        if not self.ses:
            raise Exception("Client session isn't started")
        return self.ses

    async def event_stream(self) -> AsyncGenerator[event_stream.Events, None]:
        """
        Subscribe event_stream
        """
        ses = self._check_session()
        async with ses.get(self.addr + "/v1/event/stream") as reader:
            async for raw in reader.content:
                line = raw.strip().decode()
                log.debug(f"Raw response: {line}")

                if not line or not json.loads(line):
                    continue
                yield from_json(event_stream.Events, line)

    async def register_job(
        self, job: Job, opts: Optional[RegisterOptions] = None, wopts: Optional[WriteOptions] = None
    ):
        pass

    async def job(self, name: str) -> Job:
        """
        Get job
        """
        ses = self._check_session()
        async with ses.get(self.addr + f"/v1/job/{name}") as res:
            text = await res.text()
            status = res.status
            if status != 200:
                raise Exception(text)
            return from_json(Job, text)

    async def jobs(self) -> list[Job]:
        """
        Get jobs
        """
        ses = self._check_session()
        async with ses.get(self.addr + "/v1/jobs") as res:
            text = await res.text()
            status = res.status
            if status != 200:
                raise Exception(text)
            return from_json(list[Job], text)
