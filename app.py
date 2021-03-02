from flask import Flask, request, jsonify
from predict import predict_price

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to the Spare Parts Verifier app backend !'


@app.route('/prediction/bike/price', methods=['POST'])
def get_prob():
    print('method invoked/ndata retriving')
    user_input = {'Bike_company': int(request.form['Bike_company']),
                  'Manufactured_year': int(request.form['Manufactured_year']),
                  'Engine_warranty': int(request.form['Engine_warranty']),
                  'CC(Cubic capacity)': int(request.form['CC(Cubic capacity)']),
                  'Fuel_Capacity': int(request.form['Fuel_Capacity']),
                  'Engine_type': (request.form['Engine_type']),
                  'Fuel_type': (request.form['Fuel_type']),
                  'Speedometer': (request.form['Speedometer']),
                  'Electric_Start': (request.form['Electric_Start']),
                  'Number_of_Gears': (request.form['Number_of_Gears']),
                  }

    predicted_price = predict_price(user_input)

    return jsonify({'Price': round(predicted_price, 2)})


if __name__ == '__main__':
    app.run(debug=any)
