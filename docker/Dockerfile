FROM nvidia/cuda:9.0-cudnn7-devel

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python3-dev \
    python3-pip \
    python3-wheel \
    python3-setuptools \
    git \
    cmake \
    libblas3 \
    libblas-dev \
    libglib2.0 \
    libsm-dev \
    libxrender-dev \
    libxext-dev \
    wget \
    && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN CHAINER_BUILD_CHAINERX=1 CHAINERX_BUILD_CUDA=1 pip3 install --no-cache-dir \
	cupy-cuda90==6.0.0b2 \
	opencv-python \
	scikit-learn \
	Pillow \
	keras \
	pydot \
	pandas


RUN pip3 install --no-cache-dir \
	matplotlib \
	torch torchvision
RUN wget http://johnvansickle.com/ffmpeg/old-releases/ffmpeg-3.3.4-64bit-static.tar.xz \
    && tar xvf ffmpeg-3.3.4-64bit-static.tar.xz \
    && cd ./ffmpeg-3.3.4-64bit-static/ \
    && cp ffmpeg ffprobe /usr/local/bin
WORKDIR /3D-ResNets-PyTorch
