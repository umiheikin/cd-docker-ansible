FROM yurok909/todobackend-base:latest
MAINTAINER Yuriy Miheikin <umiheikin@yandex.ru>

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse