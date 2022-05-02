## Signals

- Signals are one of the oldest methods of Inter-Process Communication (IPC) and are used to notify processes about asynchronous events (or exceptions).
- Signals canonly be sent between processes owned by the same user or from a process owned by the superuser to any process.
- To see a list of the signals in Linux, along with their numbers, do kill -l
- When a process receives a signal, what it does will depend on the way the program is written. It can take specific actions, coded into the program, to handle the signal or it can just respond according to system defaults.
- Since a process cannot send a signal directly to another process, it must ask the kernel to send the signal
- Users (including the superuser) can send signals to other processes (programs) by using kill.

# RPM

- All rpm inquiries include the -q option, which can be combined with numerous other query options:
- -f: allows you to determine which package a file came from
- -l: lists the contents of a specific package
- -a: all the packages installed on the system
- -i: information about the package
- -p: run the query against a package file instead of the package database
- The -V option to rpm allows you to verify whether the files from a particular package are consistent with the system’s RPM database
- RPM performs dependency checks. This is necessary because some packages will not operate properly unless some other package is also installed.
- RPM performs conflict checks, including attempts to install an already-installed package or to install an older version over a newer version.
- The developer building a package can specify that certain tasks be performed before or after the install.
- RPM performs any post-install tasks required for setup or initialization.
- Every time RPM installs a package, it updates information in the system database. It uses this information when checking for conflicts.
- The -i option is not designed for upgrades; attempting to install a new RPM package over an older one fails with error messages, because it tries to overwrite existing system files.
- If you want to downgrade with rpm -U (that is, to replace the current version with an earlier version), you must add the --oldpackage option to the command line.
- rpm2archive is used to convert RPM package files to tar archives. If - is given as an argument, input and output will be on stdin and stdout.

## Process and Load Monitoring Utilities

top - Process activity, dynamically updated
uptime - How long the system is running and the average Load
ps - Detailed information about processes
pstree - A tree of processes and their connections
mpstat - Multiple procesor usage
iostat - CPU utilization and I/O statistics
sar - Display and collect information about system activity
numastat - information about NUMA (Non-Uniform Memory Architecture)
strace - Information about all system calls and a process makes

## Memory monitoring utilitites
free - Brief summary of memory usage
vmstat - Detailed virtual memory statistics and block I/O dynamically updated
pmap - Process memory map

## I/O Monitoring utilitites
iostat - CPU utilization and I/O statistics
sar - Display and collect information about system activity
vmstat - Detailed virtual memory statistics and block I/O, dynamically updated

## Network Monitoring utilitites
netstat - Detailed networking statistics
iptraf - Ghather information on network interfaces
tcpdump - Detailed analusis of network packets and traffic
wireshark - Detailed network traffic analysis

## Process Monitoring Tools
top - Process activity, dynamically updated
uptime - How long the system is running and the average Load
ps - Detailed information about processes
pstree - A tree of processes and their connections
mpstat - Multiple processor usage
iostat - CPU utilization and I/O statistics
sar - Display and collect information about system activity
numstat - Information about NUMA
strace - Information about all system calls a process makes

