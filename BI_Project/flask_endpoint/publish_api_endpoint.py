from flask import Flask, jsonify
from tools import generate_fake_vehicle_fleet_usage
app = Flask(__name__)


@app.route('/api/type/vehicule', methods=['GET', 'POST'])
def generate_vehicule():
    num_vehicles=2
    num_months=6
    pre_json  = generate_fake_vehicle_fleet_usage(num_vehicles, num_months)

    json=jsonify(pre_json)
    return json
if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=5001)