FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y gcc wget git make
RUN apt-get install -y sudo

CMD /bin/bash

COPY --from=golang:1.17.8-buster /usr/local/go/ /usr/local/go/
ENV PATH="/usr/local/go/bin:${PATH}"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD ["python3", "lioscan.py", "-i"]