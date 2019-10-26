import asyncio

objects = []
fields = []


async def main():
    await asyncio.gather(*[object.update() for object in objects])


def tick():
    """Call a physics update.

    Should be implemented in an application loop.
    """
    asyncio.run(main())
