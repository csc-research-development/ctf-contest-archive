FROM python:3.11.8

RUN useradd -U -m -s /bin/bash ctf

RUN apt-get update && apt-get upgrade -y
RUN apt install -y python3 socat
WORKDIR /home/ctf
COPY flashtime.py ./ 
COPY run_in_pty.sh ./ 

RUN chmod 500 /home/ctf/flashtime.py
RUN chmod +x /home/ctf/run_in_pty.sh
RUN chown -R ctf:root /home/ctf

USER ctf

RUN pip install --upgrade pip
RUN pip install timedinput
RUN pip install sympy

CMD socat TCP-L:13339,fork EXEC:"/home/ctf/run_in_pty.sh",reuseaddr,stderr
