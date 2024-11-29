import sys
import signal
import os
import psutil
import blinkt
from flask import Flask, jsonify, request
from show_graph import show_graph
from config import get_config


app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

Config = get_config("BLINKT")
ConfigCPU = get_config("BLINKT_CPU")
ConfigMemory = get_config("BLINKT_MEMORY")

def init_blinkt():
    blinkt.set_clear_on_exit()
    blinkt.set_brightness(Config.brightness)

def getRGB(config):
    r = request.args.get('r', default = config.r, type = int)
    g = request.args.get('g', default = config.g, type = int)
    b = request.args.get('b', default = config.b, type = int)
    return r, g, b

@app.route("/cpu")
def set_cpu():
    interval = request.args.get('i', default = 1.0, type = float)
    cpu_percent = psutil.cpu_percent(interval) / 100.0
    r, g, b = getRGB(ConfigCPU)
    app.logger.info(f"cpu={cpu_percent}% R={r} G={g} B={b}")
    show_graph(cpu_percent, r, g, b)
    return jsonify({"cpu": cpu_percent, "R": r, "G": g, "B": b})

@app.route("/memory")
def set_memory():
    memory_percent = psutil.virtual_memory().percent / 100.0
    r, g, b = getRGB(ConfigMemory)
    app.logger.info(f"memory={memory_percent}% R={r} G={g} B={b}")
    show_graph(memory_percent, r, g, b)
    return jsonify({"memory": memory_percent, "R": r, "G": g, "B": b})

@app.route("/color")
def set_color():
    r, g, b = getRGB(Config)
    app.logger.info(f"color R={r} G={g} B={b}")
    ratio = blinkt.NUM_PIXELS / request.args.get('n', default = 1, type = int)
    show_graph(ratio, r, g, b)
    return jsonify({"R": r, "G": g, "B": b})

def sig_handler(signalnum, frame):
    print("received " + signal.Signals(signalnum).name)
    blinkt.clear()
    print("blinkt.clear() and exit()")
    sys.exit()

signal.signal(signal.SIGTERM, sig_handler)
signal.signal(signal.SIGINT, sig_handler)

if __name__ == "__main__":
    init_blinkt()
    n = int(os.getenv("BLINKT_INIT_LED_COUNT", blinkt.NUM_PIXELS))
    if n < 0 or n > blinkt.NUM_PIXELS:
        n = blinkt.NUM_PIXELS
    show_graph(blinkt.NUM_PIXELS / n, Config.r, Config.g, Config.b)
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=port)
