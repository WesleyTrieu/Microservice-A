import zmq
import json

# Logs are stored in a list
logs = []

# Function to add a log entry
def insert_log(user_id, action, timestamp):
    logs.append({"user_id": user_id, "action": action, "timestamp": timestamp})

# Function to retrieve logs
def get_logs(user_id=None):
    if user_id:
        return [log for log in logs if log["user_id"] == user_id]
    return logs  # Return all logs if no user_id is specified

# ZMQ Server
def zmq_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)

    # Change ports if you run into issues with the port number
    socket.bind("tcp://*:5556")  # Listening on port 5556 

    print("ZMQ Log Server Started... Waiting for requests.")
    while True:
        message = socket.recv_json()
        if message["type"] == "log":
            insert_log(message["user_id"], message["action"], message["timestamp"])
            socket.send_json({"status": "Log saved"})
        elif message["type"] == "retrieve":
            logs_data = get_logs(message.get("user_id"))
            socket.send_json(logs_data)

if __name__ == "__main__":
    zmq_server()