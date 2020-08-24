# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
from flask_healthz import healthz

from healthcheck import HealthCheck
  
# creating a Flask app 
app = Flask(__name__) 
app.register_blueprint(healthz, url_prefix="/healthz")

#health = HealthCheck()

# wrap the flask app and give a heathcheck url
health = HealthCheck(app, "/healthcheck")
  
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        #return jsonify({'data': data}) 
        return data 

# This is how you register a controller, it accepts OPTIONS and GET methods by default
# @root_blueprint.route('/health/')
#def healthz():
    #return {'message': 'Healthy'}  # This will return as JSON by default with a 200 status code


def redis_available():
    return True, "UP"

health.add_check(redis_available)
app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
#app.add_url_rule("/healthcheck", "healthcheck", health.run())





# driver function 
if __name__ == '__main__': 
  
    app.run(host='127.0.0.1', port=8080, debug = True) 


