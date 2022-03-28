## Signals

- Signals are one of the oldest methods of Inter-Process Communication (IPC) and are used to notify processes about asynchronous events (or exceptions).
- Signals canonly be sent between processes owned by the same user or from a process owned by the superuser to any process.
- To see a list of the signals in Linux, along with their numbers, do kill -l
- When a process receives a signal, what it does will depend on the way the program is written. It can take specific actions, coded into the program, to handle the signal or it can just respond according to system defaults.
- Since a process cannot send a signal directly to another process, it must ask the kernel to send the signal
- Users (including the superuser) can send signals to other processes (programs) by using kill.

## Package Management Systems
