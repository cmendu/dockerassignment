from flask import Flask, jsonify, request
import mysql.connector
  
app = Flask(__name__)
  
# Pass the required route to the decorator.
@app.route('/cube/<int:num>', methods=['GET'])
def cube(num):
    
    cube = num**3
   

    
    return jsonify({'result': cube})
    
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    