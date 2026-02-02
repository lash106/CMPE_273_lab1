import logging
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger('ServiceA')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/echo', methods=['GET'])
def echo():
    start_time = time.time()
    msg = request.args.get('msg', 'no message')
    
    # Simulate processing
    response_data = {"echo": msg}
    
    # Calculate latency
    latency_ms = (time.time() - start_time) * 1000
    logger.info(f"Endpoint: /echo | Msg: {msg} | Status: 200 | Latency: {latency_ms:.2f}ms")
    
    return jsonify(response_data)

if __name__ == '__main__':
    # Run on port 8080
    app.run(host='0.0.0.0', port=8080)