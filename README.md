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

Result (solve.py):
```
#!/usr/bin/env python3
from pwn import *


elf = ELF('/home/kali/Desktop/pwn_init/chall')
rop = ROP(elf)
libc = ELF('/home/kali/Desktop/pwn_init/libc.so.6')
rop_libc = ROP(libc)
context.arch = elf.arch

p = process('/home/kali/Desktop/pwn_init/chall', env={"LD_PRELOAD":"/home/kali/Desktop/pwn_init/libc.so.6"})
gdb.attach(p, gdbscript='b *FUNC+NUM')
# p = remote('IP', PORT)

payload = cyclic(200)
payload += p64(0xdeadbeef)

print(p.recv().decode(errors='ignore'))
p.sendline(payload)

p.interactive()


# TOOLS

# bin_sh = next(libc.search(b'/bin/sh')) + libc_addr
# pop_xxx = rop_libc.find_gadget(['pop xxx', 'ret']).address + libc_addr
# function_addr = elf.sym['function']
# function_got = elf.got['function']
# function_plt = elf.plt['function']
# bss = elf.bss()
# payload = fmtstr_payload(offset, {target_addr: format_string_payload})

# frame = SigreturnFrame()
# frame.rip = syscall
# frame.rax = 0x3b
# frame.rdi = bin_sh
# frame.rsi = 0  
# frame.rdx = 0

# one_gadget /home/kali/Desktop/pwn_init/libc.so.6
# ROPgadget --binary /home/kali/Desktop/pwn_init/chall
```
