from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '{ "nutrient_id" : 208, "value" : 89}'