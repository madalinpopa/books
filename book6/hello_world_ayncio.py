#!/usr/bin/env python3
"""
This is just a simple hello world example of using asyncio. 
In this example I'm using asyncio.run() which is the simples way to run an async function. 
"""
import asyncio, time

async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')

asyncio.run(main())