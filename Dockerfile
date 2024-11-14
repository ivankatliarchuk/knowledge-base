FROM python:3.13-slim

# Set build directory
WORKDIR /tmp

LABEL org.opencontainers.image.authors="cloudkats@gmail.com" \
  org.opencontainers.image.vendor="https://github.com/cloudkats"

COPY requirements.txt requirements.txt
# COPY setup.py setup.py

# hadolint ignore=DL3018,DL3008
RUN apt-get update -y --no-install-recommends \
  && apt-get install -y --no-install-recommends bash \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN pip install --no-cache-dir --user -r requirements.txt  \
  && rm -rf /tmp/*

ENV PATH=$PATH:/root/.local/bin
# Set working directory

WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# ENTRYPOINT [ "/bin/bash", "-c" ]
# CMD ["/bin/bash"]

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
