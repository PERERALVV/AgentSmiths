FROM python:3.12.3-slim

# Install build tools and dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc-11 \
    g++-11 \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for compiler
ENV CC=gcc-11
ENV CXX=g++-11

WORKDIR /code

COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# Clean up build tools
RUN apt-get purge -y --auto-remove \
    build-essential \
    gcc-11 \
    g++-11 \
    && rm -rf /var/lib/apt/lists/*

CMD ["python", "backend/src/main.py"]