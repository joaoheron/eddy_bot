FROM python:3.6-slim

# Install required libs for slim image
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

# Install xdotool and wmctrl
RUN apt-get install xautomation wmctrl \
    && apt-get install xdotool

WORKDIR /opt

