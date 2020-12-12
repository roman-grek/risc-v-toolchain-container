FROM ubuntu:20.04 AS builder

# The install-prefix for executable files
ENV RISCV="/opt/riscv"

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir -p "${RISCV}"

# Install system packages
RUN apt-get update; \
    apt-get upgrade --assume-yes; \
# for dependencies
    apt-get install --assume-yes \
        autoconf \
        automake \
        autotools-dev \
        curl \
        libmpc-dev \
        libmpfr-dev \
        libgmp-dev \
        gawk \
        build-essential \
        bison \
        flex \
        texinfo \
        gperf \
        libtool \
        patchutils \
        bc \
        zlib1g-dev \
        libexpat-dev \
        git \
        ca-certificates

WORKDIR ${RISCV}
RUN git clone --recursive https://github.com/riscv/riscv-gnu-toolchain ; \
    git checkout "${RISCV_COMMIT}"

# Compile
RUN cd riscv-gnu-toolchain ; \
    ./configure --prefix="${RISCV}" --with-arch="${RISCV_ARCH}" "${RISCV_ARGS}"; \
    make

# Delete source code
RUN rm -rf riscv-gnu-toolchain


FROM ubuntu:20.04

ENV RISCV="/opt/riscv"
COPY --from=builder "${RISCV}" "${RISCV}"

ENV PATH="${PATH}:${RISCV}/bin"

ARG DEBIAN_FRONTEND=noninteractive

# Install system packages
RUN apt-get update; \
    apt-get upgrade --assume-yes; \
# for dependencies
    apt-get install --assume-yes \
        autoconf \
        automake \
        autotools-dev \
        curl \
        libmpc-dev \
        libmpfr-dev \
        libgmp-dev \
        gawk \
        build-essential \
        bison \
        flex \
        texinfo \
        gperf \
        libtool \
        patchutils \
        bc \
        zlib1g-dev \
        libexpat-dev \
        git

WORKDIR /

RUN git clone --recursive https://github.com/riscv/riscv-tests

RUN cd riscv-tests ; autoconf && ./configure --prefix="${RISCV}/target"

# Patch and build tests
COPY patch.txt /riscv-tests
RUN cd riscv-tests ; git apply patch.txt && make && make install

# Copy tests binaries to volume
RUN cp -r /riscv-tests/benchmarks /tests && cp -r /riscv-tests/isa /tests

CMD ["riscv64-unknown-elf-gcc", "--version"]