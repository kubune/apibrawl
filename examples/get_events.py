# An example on how to get the events rotation data from Official Brawl Stars API

import asyncio
from apibrawl import Official
from apibrawl.Brawlify.cdn.bindings import Bindings

token = ""

async def main():
    OfficialClient = Official(token)
    eventsData = await OfficialClient.get_events()
    for event in eventsData:
        print(
        """
        Event Map: {map}
        Event ID: {id}
        Event Mode: {mode}
        Event Image: {image}
        """
        .format(
            map=event.map,
            id=event.id,
            mode=event.mode,
            image=event.image)
        )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())