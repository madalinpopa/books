#!/usr/bin/env python3
"""
This is an exemple of Hello World with asyncio but creating or getting manually a loop.
The asyncio.run() method does this automatically for you and this example it shows
the operations that are done by asyncio.run() method.
"""
import asyncio
import time

async def main():
    print(f"{time.ctime()} Hello!")
    # await token indicates the context switching when the taks are running in loop.
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


# main thread

# This will create a new loop instance or it will return the running one if it
# is alrady created. As long as you are using only a single thread (main), it will
# return the same loop instance each time.
# If you are inside an async def function, you should call asyncio.get_running_loop() instead. 
loop = asyncio.get_event_loop()

# This creates a task. Your coroutine function will not be executed until
# you do this. We say that create_task() schedules your coroutine to be run on the loop.
task = loop.create_task(main())  

# This call will block the current thread, which is the main thread.
# The run_until_complete() will keep the loop running only until the give coro completes.
# Internally, asyncio.run() calls run_until_complete() for you and therefore blocks the main 
# thread in the same way.
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)

for task in pending:
    task.cancel()

# When the main thread is unblocked, either due to a process signal being received or 
# the loop being stopped by some code calling loop.stop(), it will run the code after
# run_until_complete().
# The standard idiom here, to get all the still-pending tasks, cancel them, and then
# use loop.run_until_complete() again until those tasks are done.
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)

# loop.close() is usually the final action: it must be called on stopped loop
# and it will clear all queues and shut down the executor. 
# A stopped loop can be restarted but a closed loop is gone for good.
# asyncio.run() will close the loop before returning. run() will create a new event
# loop everytime you call it.
loop.close()