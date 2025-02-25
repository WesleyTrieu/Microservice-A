import zmq
import json
from datetime import datetime

# ZMQ Client to send logs and retrieve logs
def zmq_client(request):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    # Connect to the same port as the microservice
    socket.connect("tcp://localhost:5556")  # Connect to server
    
    socket.send_json(request)
    response = socket.recv_json()
    return response

# Function to send a log entry
def send_log(user_id, action):
    log_entry = {
        "type": "log",
        "user_id": user_id,
        "action": action,
        "timestamp": datetime.now().isoformat()
    }
    response = zmq_client(log_entry)
    print("Response:", response)

# Function to retrieve logs
def get_logs(user_id=None):
    request = {"type": "retrieve"}
    if user_id:
        request["user_id"] = user_id
    
    logs = zmq_client(request)
    print("Retrieved Logs:", json.dumps(logs, indent=4))

# Test program
if __name__ == "__main__":
    # Sending logs
    send_log("user123", "created task")
    send_log("user123", "completed task")

    send_log("user456", "deleted task")
    # Retrieving logs
    get_logs("user123")