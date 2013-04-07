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
   
    structure = {}
    photo_list = {} 
    keys = bucket.list()
    for key in keys:
        photo_path = key.name
        splitpath = photo_path.split('/')[0:-1]
        photo_path = []

        sub_structure = structure
        for dir0 in splitpath:
            dir = str(dir0)
            if not dir == 'image.jpg' and not dir == 'caption.txt':
                photo_path.append(dir)
                photo_path_str = str('/'.join(photo_path))
                if not dir in photo_list:
                    photo_list[dir] = photo_path_str

                if not dir in sub_structure:
                    sub_structure[dir] = {}
                sub_structure = sub_structure[dir]

    print structure, photo_list

    session['data_tree'] = structure
    return render_template('view_album.html', structure=structure, photo_list=photo_list)


@app.route('/photo/', methods=['GET'])
def get_photo():
    photo_path = request.args.get('path')
    splitpath = photo_path.split('/')

    sub_structure = session['data_tree']
    for dir in splitpath:
        sub_structure = sub_structure[dir]

    if 'image' in substructure:
        return substructure['image']
    return None


@app.route('/caption/', methods=['GET'])
def get_caption():
    photo_path = request.args.get('path')
    splitpath = photo_path.split('/')

    sub_structure = session['data_tree']
    for dir in splitpath:
        sub_structure = sub_structure[dir]

    if 'caption' in substructure:
        return substructure['caption']
    return None


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


