FROM thehiveproject/cortex:3.1.7

RUN apt update && \
    apt install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    ssdeep \
    libfuzzy-dev \
    libfuzzy2 \
    libimage-exiftool-perl \
    libmagic1 \
    build-essential \
    git \
    libssl-dev

COPY entrypoint.sh /opt/cortex/crowdsec-entrypoint.sh
RUN chmod +x /opt/cortex/crowdsec-entrypoint.sh

ENTRYPOINT ["/opt/cortex/crowdsec-entrypoint.sh"]