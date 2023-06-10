# pwn_init
Initializing everything you need to solve the pwn challenge

Usage:
```
$ ./pwn_init.py -h                                          
usage: pwn_init.py [-h] [-b BINARY] [-l LIBC] [-r]

Initializing everything you need to solve the pwn challenge.

options:
  -h, --help            show this help message and exit
  -b BINARY, --binary BINARY
                        Path to the binary file.
  -l LIBC, --libc LIBC  Path to the libc file.
  -r, --remove          Remove ./solve.py if exists
  ```
  
  Example:
  ```
  $ ./pwn_init.py -r -b chall -l libc.so.6 
/home/kali/Desktop/pwn_init/chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=8fe1cb6cb20bb7fe6b118857afb6ba7233345a41, for GNU/Linux 3.2.0, not stripped
[*] '/home/kali/Desktop/pwn_init/chall'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
Good luck, have fun!
```
