#------------------------Imports-----------------------------
from flask import Flask 

#app variable set up
app = Flask(__name__)


#routes------------------------------------------------------
@app.route('/')
def index():
  return "Hello, World!"


#Main code starts here---------------------------------------
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)