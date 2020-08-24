FROM python:3.8.3-slim
COPY requirements.txt /
ADD ./*.py  /scripts/
RUN chmod +x /scripts/*.py \
&& pip install -r /requirements.txt
WORKDIR /scripts
ENTRYPOINT [ "/bin/bash" ]