#!/bin/bash
groupmod -o -g "${PGID}" ma
usermod -u "${PUID}" ma
homedir="/home/ma"
if [ ! -d ${homedir} ]; then
   mkdir -p ${homedir}
fi
git clone https://github.com/bianyukun1213/MYZXKSAssistant.git ${homedir}
pip install -r ${homedir}/requirements.txt
chown ${PUID}:${PGID} -R ${homedir}
chown ${PUID}:${PGID} -R /ma_data
umask ${UMASK}
su - ma -c "python myzxks_assistant.py"
