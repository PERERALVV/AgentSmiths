FROM python:3.10.12-slim

# Install build tools and dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc-11 \
    g++-11 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for compiler
ENV CC=gcc-11
ENV CXX=g++-11

WORKDIR /code

COPY . .

COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

    # Clean up build tools
RUN apt-get purge -y --auto-remove \
    build-essential \
    gcc-11 \
    g++-11 \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/PERERALVV/MetaGPT.git ./MAS/MetaGPT && \
    cp ./config2.yaml ./MAS/MetaGPT/config/config2.yaml

CMD ["python", "backend/src/main.py"]