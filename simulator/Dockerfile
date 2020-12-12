FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update; \
    apt-get install --assume-yes \
    ninja-build \
    build-essential \
    cmake \
    libboost-all-dev \
    gcc-10 \
    g++-10 \
    git

RUN git clone --recursive https://github.com/MIPT-ILab/mipt-mips.git

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 --slave /usr/bin/g++ g++ /usr/bin/g++-10 --slave /usr/bin/gcov gcov /usr/bin/gcov-10

RUN mkdir build
WORKDIR /build
RUN cmake /mipt-mips/simulator -G "Ninja" ; \
    ninja

COPY "test.sh" "/build"
CMD [ "/bin/bash", "test.sh" ]