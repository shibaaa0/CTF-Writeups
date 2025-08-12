FROM ubuntu@sha256:c664f8f86ed5a386b0a340d981b8f81714e21a8b9c73f658c4bea56aa179d54a

# install packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata
RUN apt install -y gcc gcc-multilib apache2 curl wget
RUN a2enmod cgi

# challenge files and config
COPY ./apache2/000-default.conf /etc/apache2/sites-available/000-default.conf
RUN chown -R root:root /etc/apache2/sites-available/000-default.conf
RUN chmod 600 /etc/apache2/sites-available/000-default.conf

COPY ./apache2/index.html /var/www/html/index.html
RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 500 /var/www/html

COPY src/main.cgi /usr/lib/cgi-bin/main.cgi
RUN chown -R root:root /usr/lib/cgi-bin/main.cgi
RUN chmod 755 /usr/lib/cgi-bin/main.cgi

RUN mkdir /app
COPY src/templates /app/templates
COPY src/posts /app/posts
RUN chown -R www-data:www-data /app
RUN chmod -R 500 /app/templates
RUN chmod 700 /app/posts
RUN chmod 600 /app/posts/author/*.author
RUN chmod 600 /app/posts/content/*.content
RUN chmod 600 /app/posts/tag/*.tag
RUN chmod 600 /app/posts/title/*.title

RUN mkdir /app/session
RUN chown -R www-data:www-data /app/session
RUN chmod -R 700 /app/session

COPY readflag/readflag /readflag
RUN chown root:root /readflag
RUN chmod 755 /readflag
RUN chmod u+s /readflag

COPY readflag/flag /flag
RUN chown root:root /flag
RUN chmod 400 /flag

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
