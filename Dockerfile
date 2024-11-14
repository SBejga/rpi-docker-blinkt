FROM arm64v8/python:3.11-bookworm

WORKDIR /app

RUN pip install --no-cache-dir blinkt
RUN pip install --no-cache-dir psutil
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir requests

COPY src ./

CMD ["python3", "cpu_load.py"]