# FROM python:3.10.12-slim

# # Install build tools and dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     gcc-11 \
#     g++-11 \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# # Set environment variables for compiler
# ENV CC=gcc-11
# ENV CXX=g++-11

# WORKDIR /code

# COPY . .

# COPY ./backend/requirements.txt ./

# RUN pip install --no-cache-dir --upgrade -r requirements.txt &&\
#     cp ./config2.yaml ./MAS/MetaGPT/config/config2.yaml 
    
# RUN pip install --no-cache-dir --upgrade -e ./MAS/MetaGPT/.
# # RUN pip install --no-cache-dir --upgrade -e .[rag]

# # Clean up build tools
# RUN apt-get purge -y --auto-remove \
#     build-essential \
#     gcc-11 \
#     g++-11 \
#     && rm -rf /var/lib/apt/lists/*

# CMD ["python", "backend/src/main.py"]

FROM python:3.10.12-slim

# Install build tools and dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc-11 \
    g++-11 \
    git \
    # Install Node.js and npm
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for compiler
ENV CC=gcc-11
ENV CXX=g++-11

WORKDIR /code

COPY . .

COPY ./backend/requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt &&\
    cp ./config2.yaml ./MAS/MetaGPT/config/config2.yaml 
    
RUN pip install --no-cache-dir --upgrade -e ./MAS/MetaGPT/.
# RUN pip install --no-cache-dir --upgrade -e .[rag]

# Clean up build tools
RUN apt-get purge -y --auto-remove \
    build-essential \
    gcc-11 \
    g++-11 \
    && rm -rf /var/lib/apt/lists/*

CMD ["python", "backend/src/main.py"]