import asyncio
import time
import datetime


async def hello_func(name: str):
    print('Hello,', name)
    await asyncio.sleep(3)


async def main():
    number_of_names = int(input('Enter number of names \n'))
    coros = []
    for _ in range(number_of_names):
        coros.append(hello_func(input('Enter name \n')))

    started = datetime.datetime.now()
    print('started', started)
    await asyncio.gather(*coros)
    ended = datetime.datetime.now()
    print('ended', ended)
    print('diff', ended - started)


asyncio.run(main())
