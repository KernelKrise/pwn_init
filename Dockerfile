FROM ubuntu:latest

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y curl wget git neovim tmux strace ltrace gdb python3 net-tools binutils file gcc

RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py
RUN python3 /tmp/get-pip.py
RUN pip3 install pwntools
RUN bash -c "$(curl -fsSL https://gef.blah.cat/sh)"
RUN echo 'export LC_CTYPE=C.UTF-8' >> /root/.bashrc

WORKDIR /app
COPY . /app
