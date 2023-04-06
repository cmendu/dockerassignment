from flask import Flask, jsonify
import mysql.connector;
  
app = Flask(__name__)
  
# Pass the required route to the decorator.
@app.route("/cube")
def cube():
    i = int(request.args.get('i'))
    cube = i*i*i
    
    mydb = mysql.connector.connect(
    host="172.19.0.3",
    user="docker",
    password="secret",
    database="MathCalc"
        )
    mycursor = mydb.cursor()

    sql = "INSERT INTO cube_metric (cube_metric) VALUES (%s)"
    val = (cube)
    mycursor.execute(sql, val)

    mydb.commit()

    
    return jsonify({'result': cube})
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    