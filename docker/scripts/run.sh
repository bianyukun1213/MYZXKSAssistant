#!/bin/bash
groupmod -o -g ${PGID} ma
usermod -u ${PUID} ma
homedir="/home/ma"
rm -rf ${homedir}
mkdir ${homedir}

chown ${PUID}:${PGID} -R ${homedir}
chown ${PUID}:${PGID} -R /ma_data
umask ${UMASK}

su - ma

if [ ${HTTP_PROXY} ]; then
   echo "HTTP_PROXY=${HTTP_PROXY}"
	git config --global http.proxy ${HTTP_PROXY}
else
	git config --global --unset http.proxy
fi
if [ ${HTTPS_PROXY} ]; then
   echo "HTTPS_PROXY=${HTTPS_PROXY}"
	git config --global https.proxy ${HTTPS_PROXY}
else
	git config --global --unset https.proxy
fi
git clone https://github.com/bianyukun1213/MYZXKSAssistant.git ${homedir}

pipproxy=""
if [ ${HTTP_PROXY} ]; then
   pipproxy="--proxy ${HTTP_PROXY}"
fi
if [ ${HTTPS_PROXY} ]; then
   pipproxy="--proxy ${HTTPS_PROXY}"
fi
pip ${pipproxy} install -r ${homedir}/requirements.txt

python ${homedir}/myzxks_assistant.py --container
