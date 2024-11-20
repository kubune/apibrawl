import aiohttp
import asyncio

from ..Brawlify.cdn.bindings import Bindings

class Event:
    def __init__(self, data):
        self.startTime = data['startTime']
        self.endTime = data['endTime']
        self.slotId = data['slotId']
        self.mode = data['event']['mode']
        self.id = data['event']['id']
        self.map = data['event']['map']
        self.image = Bindings().image(self.id)


class Events:
    def format(self, data):
        returnData = []
        for event in data:
            returnData.append(Event(event))

        return returnData