FROM debian

MAINTAINER tkaolik <tigrankatolikyan@.gmail.com>

#RUN apt-get -y update && apt-get -y upgrade && apt-get install -y \
#	bzip2 \
#	mariadb-client \
#	mariadb-server \
#	systemd \
#	wget \
#	&& rm -rf /var/lib/apt/lists/* \
#	&& /etc/init.d/mysql start && sleep 5 && mysqladmin password "mariadb-password" \
#	&& echo "create database teamspeak3; \
#	GRANT ALL PRIVILEGES ON teamspeak3.* TO 'teamspeak3'@'localhost' IDENTIFIED BY 'teamspeak3password'; \
#	flush privileges;" > create_db.sql \
#	&& mysql -u root -pmariadb-password < create_db.sql && rm create_db.sql \
#	&& useradd -d /opt/teamspeak3-server -m teamspeak3-user \
#	&& cd /tmp \
#	&& wget https://files.teamspeak-services.com/releases/server/3.6.1/teamspeak3-server_linux_amd64-3.6.1.tar.bz2 \
#	&& tar -vxjf teamspeak3-server_linux_amd64-3.6.1.tar.bz2 \
#	&& mv teamspeak3-server_linux_amd64/* /opt/teamspeak3-server/ \
#	&& chown teamspeak3-user:teamspeak3-user /opt/teamspeak3-server -R \
#	&& rm -rf teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2 teamspeak3-server_linux_amd64/ \
#	&& ln -s /opt/teamspeak3-server/redist/libmariadb.so.2 /opt/teamspeak3-server/libmariadb.so.2 \
#	&& touch /opt/teamspeak3-server/query_ip_blacklist.txt \
#	&& echo "127.0.0.1" > /opt/teamspeak3-server/query_ip_whitelist.txt \
#	&& echo "machine_id=\
#default_voice_port=9987\
#voice_ip=0.0.0.0\
#licensepath=\
#filetransfer_port=30033\
#filetransfer_ip=0.0.0.0\
#query_port=10011\
#query_ip=0.0.0.0\
#query_ip_whitelist=query_ip_whitelist.txt\
#query_ip_blacklist=query_ip_blacklist.txt\
#dbsqlpath=sql/\
#dbplugin=ts3db_mariadb\
#dbsqlcreatepath=create_mariadb/\
#dbpluginparameter=ts3db_mariadb.ini\
#dbconnections=10\
#logpath=logs\
#logquerycommands=0\
#dbclientkeepdays=30\
#logappend=0\
#query_skipbruteforcecheck=0" > /opt/teamspeak3-server/ts3server.ini \
#	&& echo "[config]\
#host=127.0.0.1\
#port=3306\
#username=teamspeak3\
#password=teamspeak3password\
#database=teamspeak3\
#socket=" > /opt/teamspeak3-server/ts3db_mariadb.ini \
#	&& chown teamspeak3-user:teamspeak3-user /opt/teamspeak3-server -R
#EXPOSE 9987/udp 30033 10011
#ENV TS3SERVER_LICENSE=accept
#CMD ["sh", "/opt/teamspeak3-server/ts3server_minimal_runscript.sh"]

ENV TS3SERVER_LICENSE=accept

WORKDIR /home/teamspeak

EXPOSE 9987/udp 10011 30033

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y wget bzip2 && \
	wget http://dl.4players.de/ts/releases/3.0.13.8/teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2 && \
 	tar xfv teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2

WORKDIR teamspeak3-server_linux_amd64

ENTRYPOINT sh ts3server_minimal_runscript.sh

# docker run --rm -p 9987:9987/udp -p 10011:10011 -p 30033:30033 ex01
# https://www.vultr.com/docs/how-to-install-teamspeak-3-server-on-ubuntu-16-04-64-bit
