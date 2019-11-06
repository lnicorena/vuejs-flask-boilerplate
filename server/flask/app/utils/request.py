from .. import app
from flask import jsonify



# Prepare a json with an error message
MSG_ERROR = -1
# Prepare a json with an success message
MSG_SUCCESS = 1

# prepare the api response and save to DB if so

def prepare_response(status, data):

    result = {}

    code = 200
    if status in [MSG_SUCCESS]:
        result['status'] = 'OK'
        result['result'] = data

    if status in [MSG_ERROR]:
        result['status'] = 'error'
        result['errors'] = data
        code = 400

    return jsonify(result), code
