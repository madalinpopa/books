
## Chapter 2
- Benefits of threads
    - Your code can run concurrently, but still be set out in a very simple, top-down linear sequence of commands to the point where—and this is key—you can pretend, within the body of your functions, that no concurrency is happening
    - Your code can exploit multiple CPUs while still having threads share memory. This is important in many workloads where it would be too costly to move large amounts of data between the separate memory spaces of different processes, for example.
    - There is a large body of knowledge and best practices available for writing threaded applications. There is also a huge amount of existing “blocking” code that depends on multithreading for concurrent operation.
- generally speaking, the best practice for using threads is to use the ThreadPoolExecutor class from the concurrent.futures module
- The ThreadPoolExecutor offers an extremely simple interface for running functions in a thread
- Threads require extra operating system resources to create, such as preallocated, per-thread stack space that consumes process virtual memory up front. This is a big problem with 32-bit operating systems, because the address space per process is limited to 3 GB

## Chapter 3
- asyncio provides a run() function to execute an async def function and all other coroutines called from there, like sleep() in the main() function.
- You need a loop instance before you can run any coroutines, and this is how you get one. In fact, anywhere you call it, get_event_loop() will give you the same loop instance each time, as long as you’re using only a single thread
- If you’re inside an async def function, you should call asyncio.get_running_loop() instead, which always gives you what you expect.
