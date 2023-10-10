#!/usr/bin/env python3
import os
import argparse


SOLVE_TEMPLATE = """#!/usr/bin/env python3
from pwn import *


elf = context.binary = ELF('BINARY_PATH')
context.log_level = "DEBUG"
rop = ROP(elf)
#LIBC libc = ELF('LIBC_PATH')
#LIBC rop_libc = ROP(libc)

#BIN p = process('BINARY_PATH')
#LIBC p = process('BINARY_PATH', env={"LD_PRELOAD":"LIBC_PATH"})
gdb.attach(p, gdbscript='b *FUNC+NUM')
# p = remote('IP', PORT)

payload = cyclic(200)
payload += p64(0xdeadbeef)

print(p.recv().decode(errors='ignore'))
p.sendline(payload)

p.interactive()


# TOOLS

# p = process(['/chall/ld-linux-x86-64.so.2', '/chall/binary'], env={"LD_LIBRARY_PATH":"/chall"})
# context(log_level='debug',arch='amd64',terminal=['tmux','splitw','-h'])
# context.terminal = ["tmux", "splitw", "-h"]

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

# one_gadget LIBC_PATH
# ROPgadget --binary BINARY_PATH
"""


def parse_args():
    parser = argparse.ArgumentParser(
        description='Initializing everything you need to solve the pwn challenge.'
        )
    parser.add_argument('-b', '--binary', help='Path to the binary file.')
    parser.add_argument('-l', '--libc', help='Path to the libc file.')
    parser.add_argument('-r', '--remove', action='store_true', help='Remove ./solve.py if exists')
    args = parser.parse_args()
    binary_path = args.binary
    libc_path = args.libc
    remove_solve_py = args.remove

    if binary_path is None:
        parser.print_help()
        exit()
    
    return binary_path, libc_path, remove_solve_py


if __name__ == "__main__":
    binary, libc, remove_solve = parse_args()
    binary = os.path.abspath(binary)

    if remove_solve:
        try:
            os.remove('./solve.py')
        except FileNotFoundError:
            pass

    if not os.path.exists(binary):
        print(f"File {binary} doesn't exists")
        exit()

    if os.path.exists('./solve.py'):
        print('File ./solve.py already exists!')
        exit()

    SOLVE_TEMPLATE = SOLVE_TEMPLATE.replace('BINARY_PATH', binary)
    if libc is not None:
        libc = os.path.abspath(libc)
        SOLVE_TEMPLATE = SOLVE_TEMPLATE.replace('LIBC_PATH', libc)
        if not os.path.exists(libc):
            print(f"File {libc} doesn't exists")
            exit()
    with open('solve.py', 'a') as f:
        for i in SOLVE_TEMPLATE.split('\n'):
            if libc is None:
                if '#BIN ' in i:
                    f.write(i.replace('#BIN ', '') + '\n')
                elif '#LIBC ' not in i:
                    f.write(i + '\n')
            else:
                if '#LIBC ' in i:
                    f.write(i.replace('#LIBC ', '') + '\n')
                elif '#BIN ' not in i:
                    f.write(i + '\n')

    os.system(f"chmod +x {binary} solve.py")
    os.system(f"file {binary}")
    os.system(f"pwn checksec {binary}")
    print("Good luck, have fun!")
