FROM ubuntu

MAINTAINER tkatolik <tigrankatolikyan@gmail.com>

RUN apt update && apt install -y cowsay && ln -s /usr/games/cowsay /usr/bin/cowsay

ENTRYPOINT ["cowsay"]
