# Real-Time EC2 State Change Integration with ServiceNow

This project demonstrates a real-time, event-driven ServiceNow inbound integration where **EC2 instance state changes in AWS** are sent to **ServiceNow** and recorded in a custom table via a Scripted REST API.
When an EC2 instance is started, stopped, or terminated, AWS EventBridge triggers a Lambda function, which then sends the instance state (and ID) to ServiceNow. 
This helps in maintaining real-time visibility of infrastructure changes inside the platform for use cases like.
- Logging all EC2 state changes into ServiceNow in real-time
- Alerting IT teams when critical instances are stopped or terminated
- Notifying region-specific users based on subscriptions
- Sending alerts during scheduled or unexpected maintenance
- Powering automation or CMDB sync workflows
## Tech stack used

###->AWS
- **EC2**: Source of state change events
- **EventBridge**: Triggers events on EC2 state changes
- **Lambda**: Processes the event and sends it to ServiceNow
- **IAM**: Roles for Lambda and EventBridge

###->ServiceNow
- **Custom Table**: Stores EC2 state changes (e.g., `u_ec2_instance_state`)
- **Scripted REST API**: Secure endpoint to receive data
- **Basic Authentication**: For API access

---

### Steps for Setup:

### 1. ServiceNow Setup
- Create a **custom table** (`u_ec2_instance_state`) with fields:
  - `Instance ID` (String)
  - `State` (Choice/String)
  - `Region` (String)
  - `Time Received` (Auto-populated)
  <img width="1585" height="241" alt="image" src="https://github.com/user-attachments/assets/f7960923-6774-4055-8394-bd2ddb2d6481" />

- Create a **Scripted REST API**:
  - API path: `/api/ec2_state_api/state`
  - Accepts POST requests with JSON payload
  - paste JS code in this repo
<img width="1858" height="933" alt="image" src="https://github.com/user-attachments/assets/19c0ab27-582d-4030-b836-16cda1c8f593" />
<img width="1914" height="940" alt="image" src="https://github.com/user-attachments/assets/d58fced2-d313-4d8e-85e4-6823057c3ed3" />

### 2. AWS Lambda Setup
- Create a new execution role adding permission:AWSLambdaBasicExecutionRole to enable CLoudWatch Logging
- Create a Lambda function in Python 3.x
- Add the following environment variables:
  - `SN_URL`: Scripted REST API endpoint (e.g. `https://<instance>.service-now.com/api/ec2_state_api/state`)
  - `SN_USER`: Basic auth username
  - `SN_PASS`: Basic auth password
<img width="487" height="375" alt="image" src="https://github.com/user-attachments/assets/c50a95c5-c512-4928-b964-a92749339e09" />
- Paste the Python code in this repo:

### 3. EventBridge Setup
- Create a new EventBridge rule
- Add the json and set the target to the lambda function
  <img width="554" height="309" alt="image" src="https://github.com/user-attachments/assets/1c982858-7dc3-47ab-81ab-1e3e5ce7793e" />

Finally you can see the EC2 state changes updating in ServiceNow in real-time yay
<img width="1919" height="520" alt="image" src="https://github.com/user-attachments/assets/e5eab321-7dab-4455-986c-2597d25ad825" />

<img width="1919" height="486" alt="image" src="https://github.com/user-attachments/assets/1a6e2118-0e80-4061-9d80-57e83ca64708" />




