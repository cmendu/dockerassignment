from flask import Flask, jsonify, request
from datetime import datetime
import time
import mysql.connector
  
app = Flask(__name__)
  
# Calculate cube.
@app.route('/cube/<int:num>', methods=['GET'])
def cube(num):
    metric_start = time.time()
    cube = num**3
    metric_end = time.time()
    metrics = metric_end - metric_start

    
    return jsonify({'cube': cube, 'metrics': metrics })
    
@app.route('/square/<int:num>', methods=['GET'])
def square(num):
    metric_start = time.time()
    square = num**2
    metric_end = time.time()
    metrics = metric_end - metric_start

    
    return jsonify({'square': square, 'metrics': metrics })
    

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    