FROM python:latest

LABEL org.opencontainers.image.authors="HeyHollis" \
    org.opencontainers.image.source="https://github.com/bianyukun1213/MYZXKSAssistant"

ENV PUID=99 \
    PGID=100 \
    UMASK=000 \
    TZ=Asia/Shanghai
EXPOSE 8972
VOLUME /ma_data /ma_log
RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && \
    echo ${TZ} > /etc/timezone && \
    groupadd -g 9981 ma && \
    useradd -u 9981 -g ma -d /home/ma -s /bin/bash ma
ADD /scripts/ /opt/scripts/
ENTRYPOINT ["/opt/scripts/run.sh"]
