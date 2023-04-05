from flask import Flask, jsonify
  
app = Flask(__name__)
  
# Pass the required route to the decorator.
@app.route("/cube")
def cube():
    i = int(request.args.get('i'))
    square = i*i*i
    return jsonify({'result': cube})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    