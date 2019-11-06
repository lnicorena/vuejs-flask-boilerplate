from app import app
from app import cache
from app.database import SampleTable
from app.utils import request as REQ
from flask import jsonify
from datetime import datetime

# sanity check route
@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify('It works!')

# caching test
@app.route('/test', methods=['GET'])
def cache_test():
    if cache.get('test') is None:
        cache.set('test', datetime.utcnow(), timeout=10)

    return REQ.prepare_response(REQ.MSG_SUCCESS, cache.get('test'))
