FROM python:3.7

ADD requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /app/

# COPY entrypoint.sh /usr/local/bin/entrypoint.sh
# RUN chmod 755 /usr/local/bin/entrypoint.sh \
#     && ln -s /usr/local/bin/entrypoint.sh /

COPY  . /app/

EXPOSE 8000

# ENTRYPOINT [ "entrypoint.sh" ]