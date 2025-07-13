from flask import Flask
from call_scheduler import call_customers

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Voice call service is running!"

@app.route('/run-calls')
def run_calls():
    call_customers()
    return "📞 Calls started", 200
