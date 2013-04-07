## flask modules
from flask import Flask
from flask import request, Response
from flask import render_template
from flask import make_response
from flask import g
from flask import redirect
from flask import session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import *
from flask.ext.security.datastore.sqlalchemy import SQLAlchemyUserDatastore

## python modules
import os
from boto.s3.connection import S3Connection
from zipfile import *


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '908u23r@32r2&//adfeofi21002'


@app.route('/', methods=['GET'])
def main_page():
    conn = S3Connection('AKIAI6WMUYBUBJ2T3GMQ', 'hz0evOhGQTHgAeUeEZaJ0XIBv+wVU1C6iKyafe5b')    
    bucket = conn.get_bucket('photo-collective')
    ## TODO: read bucket contents

    return render_template('view_album.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


