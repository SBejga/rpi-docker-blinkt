FROM arm64v8/python:3.11-bookworm

WORKDIR /app

RUN pip install --no-cache-dir blinkt
RUN pip install --no-cache-dir psutil

COPY config.py cpu_load.py mem_load.py ./

CMD ["python3", "/app/cpu_load.py"]