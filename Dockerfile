FROM python:3.10.9-slim

WORKDIR /EasyOCR

COPY  . .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 7860
CMD ["python", "app.py"]