
`pip install line_profiler`
a `@decorator` is used to mark the chosen function
the `kernprof` script is used to execute your code and the CPU time and other statistics for each line of the chosen function are recorded.

`pip install memory profiler`
`pip install psutil`

- Tuples are cached by the python runtime, which means that we don't need to talk to the kernel to reserve memory everytime we want to use one
