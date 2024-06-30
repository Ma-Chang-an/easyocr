FROM python:3.10.9-slim as download_models

RUN apt update && apt install -y aria2

RUN  --dir "/" --out

FROM python:3.10.9-slim as server

WORKDIR /EasyOCR

COPY ./requirements.txt ./requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install numpy==1.26.4
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cu118

RUN chown 1003:1003 /EasyOCR
COPY --chown=1003:1003 ./app.py ./app.py
COPY --chown=1003:1003 ./examples/ /examples
COPY --chown=1003:1003 ./models ./models
RUN mkdir /flagged && chown 1003:1003 /flagged

WORKDIR /
EXPOSE 8000
CMD ["python", "/EasyOCR/app.py"]
