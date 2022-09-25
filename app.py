import sys
from flask import Flask
from demo.logger import logging
from demo.exception import DemoException
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception.")
    except Exception as e:
        demon = DemoException(e, sys)
        logging.info(demon.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."



if __name__=="__main__":
    app.run(debug=True)