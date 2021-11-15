from flask import Flask
from flask import jsonify
import numpy as np

application = Flask(__name__)


@application.route('/')
def hello():
    return "Hello Stefan"


@application.route('/random/<n>')
def randomvals(n):

    try:
        nInt = int(n)

        if nInt < 0 or nInt > 20:
            return "n must be between [0,20]", 400

        values = np.random.randint(0, 10, int(n))
        result = {'values': values.tolist()}
        return result, 200
    except ValueError:
        return "please provide a number", 400


if __name__ == "__main__":
    application.run(debug=True)
