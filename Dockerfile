FROM python:3.12-slim
RUN apt-get update && apt-get install -y openssl openssh-client
RUN openssl genrsa -out /tmp/parcel.key 1024
RUN ssh-keygen -t dsa -N '' -f /tmp/parcel_dsa
COPY services /app
