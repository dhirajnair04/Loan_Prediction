# Loan Prediction Model

This is a **Flask-based Loan Prediction Model** that predicts loan rejection probability based on user inputs.

## Features
- **Web Interface**: HTML form (`main_v2.html`) for user inputs.
- **Machine Learning Model**: Model is loaded from a `.tar` file.
- **Deployment**: Can be run locally or on a **Docker container**.
- **AWS EC2 Deployment**: The model is also pushed to AWS EC2.

## Installation & Setup

### Clone the Repository
```
git clone https://github.com/dhirajnair04/Loan_Prediction.git
cd Loan_Prediction
```
#### Install Dependencies
```
pip install -r requirements.txt
```
(Ensure you have Flask, pandas, sklearn, etc.)

##### Run the Flask App
```
python appv2.py
```
Visit http://127.0.0.1:5000/ in your browser.

###### Docker Deployment
To run the application inside a Docker container:
```
docker build -t loan-prediction .
docker run -p 5000:5000 loan-prediction
```

###### AWS EC2 Deployment
1. Transfer the .tar model file to EC2:
```
scp model.tar ubuntu@your-ec2-ip:/home/ubuntu/
```

2. SSH into EC2:
```
ssh ubuntu@your-ec2-ip
```
3. Run the model inside EC2.

Author
Your Name - https://github.com/dhirajnair04
