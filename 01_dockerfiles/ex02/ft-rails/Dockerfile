FROM ruby

MAINTAINER tkatolik <tigrankatolikyan@gmail.com>

RUN gem update --system && \
	gem install rails
ONBUILD ARG DIR=./app/
ONBUILD WORKDIR /opt/app/
ONBUILD COPY $DIR .
ONBUILD RUN bundle install && \
		rake db:migrate && \
		rake db:seed

#RUN apt-get update -y && \
#	apt-get install -y build-essential libpq-dev nodejs sqlite3 gem && \
#	gem install bundler --no-document && \
#	gem install rails --no-document && \
#	gem install rake -v 12.3.2 --no-document
#
#ONBUILD COPY app /opt/app
#ONBUILD WORKDIR /opt/app
#
#ONBUILD EXPOSE 3000
#ONBUILD RUN bundle install
#ONBUILD RUN rake db:migrate
#ONBUILD RUN rake db:seed
#
# docker build -t ft-rails:on-build .
