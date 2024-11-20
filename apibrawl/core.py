import asyncio
import aiohttp
from sys import version_info
import json
from traceback import format_exc

from .Official.events import Events
from .Official.api import API
from .Official.errors import *

class Official:
    def __init__(self, token: str) -> None:
        self.token = token
        self.headers = {
            "Authorization": "Bearer " + token,
            "User-Agent":  "apibrawl/0.1 (Python " + str(version_info[0]) + "." + str(version_info[1]) + ")",
            "Accept-Encoding": "gzip"
        }
        self.API = API()
        self.session = aiohttp.ClientSession()

    def _checkForErrors(self, resp, text):
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = text

        code = getattr(resp, 'status', None) or getattr(resp, 'status_code')
        url = resp.url

        if 300 > code >= 200:
            return data
        if code == 403:
            raise Forbidden(code, url, data['message'])
        if code == 404:
            raise NotFoundError(code, reason='Resource not found.')
        if code == 429:
            raise RateLimitError(code, url)
        if code == 500:
            raise UnexpectedError(code, url, data)
        if code == 503:
            raise ServerError(code, url)

    async def get_events(self):
        try:
            async with self.session.get(url=self.API.EVENTS, headers=self.headers) as resp:
                data = self._checkForErrors(resp, await resp.text())

            return Events().format(data)

        except:
            print(format_exc())
