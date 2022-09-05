#!/usr/bin/python3

import sys
from Application import Application

if __name__ == "__main__":
    app = Application( sys.argv )
    app.aboutToQuit.connect( app.close )
    sys.exit( app.exec() )
