# CS361HW8
This microservice uses ZMQ to request and receive data. 

To use ZMQ please run the command to install it.
``` python
pip install zmq
```

Make sure that you are connecting to the same port that the microservices in your main program.
``` python
socket.connect("tcp://localhost:5556")
```

Create a function that connects to the port in your main to allow you to send and retrieve logs. You will be calling this function inside of your log and retrieve functions. 


## Logging an action
Send a JSON object with the following structure:
``` json
{
  "type": "log",
  "user_id": "<user_id>",
  "action": "<action_description>",
  "timestamp": "<ISO format timestamp>"
}
```

Make sure to include "type", this is used to determine if you are logging and entry or retrieving a log. Your logging function should only take 2 parameters which are user_id and action. Include timestamp in order to display and track the time for each log entry. 

To use timestamp, include this at the top of your main program.
``` python
from datetime import datetime
```

You can use this format for timestamp.
``` python
datetime.now().isoformat()
```

You can call this function using the following code example.
``` python
log_action(user_id, action)
```


## Retrieving logs
Send a JSON object with the following structure:
``` json
{
  "type": "retrieve",
  "user_id": "<user_id>"  // Optional
}
```
You can choose not to include the user_id if you want to retrieve all logs or you can make an if statement to filter out based on user_id.
  
Make sure to include a print statement after to retrieve the audit log and display them.

You can call this function using the following code example.
``` python
get_logs(user_id)
```

## UML Sequence Diagram

![Untitled drawing](https://github.com/user-attachments/assets/131893b0-944c-4f78-a455-d99c60589c4f)
