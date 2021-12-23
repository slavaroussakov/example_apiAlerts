FROM alpine:edge
COPY . /app
RUN apk update && \
    apk -v --no-cache add \
    python3 \
    py3-pip &&\
    cd /app && \
    pip3 install -r ./requirements.txt
ENTRYPOINT ["/app/apiAlerts.py"]
