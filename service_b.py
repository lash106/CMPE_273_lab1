import logging
import time
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger('ServiceB')

SERVICE_A_URL = "http://localhost:8080/echo"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/call-echo', methods=['GET'])
def call_echo():
    start_time = time.time()
    msg = request.args.get('msg', 'hello')
    
    try:
        # Call Service A with a strict timeout (e.g., 2 seconds)
        logger.info(f"Calling Service A with msg='{msg}'...")
        response = requests.get(SERVICE_A_URL, params={'msg': msg}, timeout=2)
        
        # If the response was successful (200 OK), parse it
        response.raise_for_status() 
        data = response.json()
        
        result = {
            "service_b_message": "Service B called A successfully",
            "service_a_response": data
        }
        
        latency_ms = (time.time() - start_time) * 1000
        logger.info(f"Endpoint: /call-echo | Status: 200 | Latency: {latency_ms:.2f}ms")
        return jsonify(result)

    except requests.exceptions.RequestException as e:
        # Handle failure (Timeout, Connection Refused, etc.)
        latency_ms = (time.time() - start_time) * 1000
        logger.error(f"Service A call failed: {e}")
        logger.info(f"Endpoint: /call-echo | Status: 503 | Latency: {latency_ms:.2f}ms")
        
        return jsonify({"error": "Service A is unavailable", "details": str(e)}), 503

if __name__ == '__main__':
    # Run on port 8081
    app.run(host='0.0.0.0', port=8081)