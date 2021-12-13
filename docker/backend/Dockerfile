FROM python:3

ENV GOSU_VERSION 1.10
RUN curl -sS -Lo /usr/bin/gosu https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64
RUN chmod +x /usr/bin/gosu

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV GIST_URL https://gist.githubusercontent.com/LucasVmigotto/850418a9b47757fb3006cdd9be2c29cb/raw/87d1c9e5e416171dc7f2f8178bed2e70d9c78e7c/entrypoint-python.sh
RUN curl -sS $GIST_URL > /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

VOLUME /app
WORKDIR /app

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]
CMD [ python ]