FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Setup Debian linux
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install build-essential curl

RUN mkdir /app

RUN pip install --upgrade pip
ADD /root/requirements.txt /app/
# ADD /frontend/package.json /app/

WORKDIR /app/
ADD . /app/

# RUN chmod a+x ./frontend/node_modules/.bin/react-scripts

RUN pip install -r requirements.txt
#     && groupadd -r django \
#     && useradd -r -g django django
#     # && npm install -g npm@latest && npm run build --prefix frontend/

# RUN chown -R django /app

# RUN chmod +x ./backend/root/production/start.sh \
#     && chown django ./backend/root/production/start.sh

EXPOSE 8000