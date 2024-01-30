FROM python:3.9


RUN apt-get update && \
    apt-get install -y \
    ca-certificates 

RUN curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
RUN chmod a+r /etc/apt/keyrings/docker.asc

RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \ 
  tee /etc/apt/sources.list.d/docker.list > /dev/null

RUN apt-get update

RUN apt-get install -y docker-ce=23.0.1 docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

WORKDIR /usr/src/app



COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./discordbot.py"]

