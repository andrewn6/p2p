# Functionality for uploading a file to the HTTP server
import os
from crypto import *
fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)

    open(fn, 'wb').write(encrypt(fileitem.file.read()))









