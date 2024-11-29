FROM arm64v8/python:3.11-bookworm

WORKDIR /app
STOPSIGNAL SIGINT

RUN pip install --no-cache-dir blinkt --no-deps
RUN pip install --no-cache-dir psutil
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir rpi-lgpio

COPY src ./
CMD ["python3", "app.py"]