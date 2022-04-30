# Functionality for uploading a file to the HTTP server
import os

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)

    open(fn, 'wb').write(fileitem.file.read())




