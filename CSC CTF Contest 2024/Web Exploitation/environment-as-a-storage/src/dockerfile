FROM php:8.3.7-cli-alpine

WORKDIR /home/ctf

COPY index.php ./

COPY function.php ./

COPY Inject.php ./

COPY checkCOOKIE.php ./

COPY Cookied.php ./

COPY flag.txt ../../../../../../../../../

RUN mkdir -p Controller Router Views

COPY Controller ./Controller

COPY Router ./Router

COPY Views ./Views

RUN chmod 555 /home/ctf/

EXPOSE 7777 

CMD ["php", "-S", "0.0.0.0:7777"]