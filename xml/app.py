import io
import json
from flask import Flask
app = Flask(__name__)

@app.route('/meal_item/<ndbno>')
def meal_item(ndbno):

  # Dummy code do simulate getting a report from USDA NAL NDB
    try:
        data = json.load(io.open('banana_report.json'))
        meal_item_name = data['report']['food']['name']
        ref_unit = data['report']['food']['ru']
        data_source = data['report']['food']['ds']
        return meal_item_name
    except FileNotFoundError as fnf:
        return (fnf.errno, '')
  