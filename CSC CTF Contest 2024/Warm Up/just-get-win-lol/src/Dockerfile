FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN useradd -U -m -s /bin/bash ctf

COPY ./win /home/ctf/win
COPY ./flag.txt /home/ctf/flag.txt
COPY ./run.sh /home/ctf/run

RUN chown -R root:ctf /home/ctf && chmod -R 550 /home/ctf

CMD socat TCP-L:1439,fork EXEC:"/home/ctf/run",reuseaddr,stderr