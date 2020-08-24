# Using flask to make an api 

from flask import Flask, jsonify, request 
from flask_healthz import healthz

from healthcheck import HealthCheck
  
# creating a Flask app 
app = Flask(__name__) 
app.register_blueprint(healthz, url_prefix="/healthz")

#health = HealthCheck()

# wrap the flask app and give a heathcheck url
health = HealthCheck(app, "/healthcheck")
  
# on the terminal type: curl http://127.0.0.1:8080/ 
# returns hello world when we use GET. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        #return jsonify({'data': data}) 
        return data 

def site_available():
    return True, "UP"

health.add_check(site_available)
app.add_url_rule("/healthcheck", "healthcheck", health.run())

# driver function 
if __name__ == '__main__': 
  
    app.run(host='127.0.0.1', port=8080, debug = True) 


