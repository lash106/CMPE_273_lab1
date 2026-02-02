# Tiny Distributed System (Python Track)

This project demonstrates a simple distributed system with two services communicating over HTTP. It includes basic logging, latency tracking, and failure handling (timeouts).

## Project Structure

- **Service A (Echo API):** Listens on port `8080`. Returns a health status and echoes messages.
- **Service B (Client):** Listens on port `8081`. Acts as a proxy/client that calls Service A.

## Prerequisites

- **Python 3.10+**
- **Git**
- **curl** (for testing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lash106/CMPE_273_lab1.git
   cd CMPE_273_lab1

   Install dependencies:

Bash
pip install -r requirements.txt
How to Run Locally
You will need two separate terminal windows to run the services simultaneously.

1. Start Service A (Echo Service)
In the first terminal:

Bash
python service_a.py
# Output: Running on [http://0.0.0.0:8080](http://0.0.0.0:8080)
2. Start Service B (Client Service)
In the second terminal:

Bash
python service_b.py
# Output: Running on [http://0.0.0.0:8081](http://0.0.0.0:8081)
Testing & Verification
1. Success Scenario
Run the following command in a third terminal (or a browser):

Bash
curl "http://localhost:8081/call-echo?msg=HelloDistributed"
Expected Output:

JSON
{
  "service_a_response": {
    "echo": "HelloDistributed"
  },
  "service_b_message": "Service B called A successfully"
}
2. Failure Scenario (Resilience)
Go to the terminal running Service A.

Press Ctrl+C to stop the process.

Run the same curl command again:

Bash
curl -v "http://localhost:8081/call-echo?msg=HelloDistributed"
Expected Output: You should receive an HTTP 503 error.

JSON
{
  "details": "...",
  "error": "Service A is unavailable"
}
Check the Service B terminal logs to see the error message indicating the connection failure.

What makes this distributed?
This system is distributed because it consists of two distinct processes (Service A and Service B) that do not share memory and run independently, potentially on different machines. They communicate strictly over a network protocol (HTTP) via message passing. Crucially, they exhibit partial failure: Service A can fail (crash or network partition) while Service B continues to operate, detect the failure, and handle it gracefully. 
