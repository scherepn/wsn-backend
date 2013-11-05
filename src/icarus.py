################################################################################
# Overview or purpose of file                                                  #
#   included components                                                        #
#                                                                              #
# Copyright AGPLv3 by Phil Scherer                                             #
################################################################################

# Imports
import sys
from flask import Flask

# Globals
app = Flask(__name__)

# Classes


# Functions
@app.route("/")
def hello():
    return "Hello World " + str(sys.version_info[0:3])


# Main
if __name__ == "__main__":
    app.debug = True
    app.run()

