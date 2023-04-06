from flask import Flask, jsonify
import mysql.connector;
  
app = Flask(__name__)
  
# Pass the required route to the decorator.
@app.route("/cube")
def cube():
    i = int(request.args.get('i'))
    cube = i*i*i
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="docker",
    password="secret",
    database="MathCalc"
        )
    mycursor = mydb.cursor()

    mycursor.execute("INSERT INTO cube_metric (cube_metric) VALUES (?)",(cube))

    mydb.commit()

    
    return jsonify({'result': cube})
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
