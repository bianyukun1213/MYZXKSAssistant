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
git clone https://github.com/bianyukun1213/MYZXKSAssistant.git ${homedir}

if [ ${HTTP_PROXY} ]; then
   pip install --proxy ${HTTP_PROXY} -r ${homedir}/requirements.txt
else
	pip install -r ${homedir}/requirements.txt
fi

python ${homedir}/myzxks_assistant.py --container
