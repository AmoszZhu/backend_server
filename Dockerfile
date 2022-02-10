FROM python:3.8.12

WORKDIR /server
ADD . /server
# RUN apt-get update && apt-get install -y vim
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt