from flask import Flask, render_template, request
from flask import Blueprint
from flask import current_app as app
import os
import werkzeug
import pandas as pd
from helpers import helper

routes_bp = Blueprint('report', __name__)

@routes_bp.route('/crime/status', methods=['GET', 'POST'])
def status():
	if request.method == 'GET':
		return render_template('status.html')

@routes_bp.route('/crime', methods = ['GET'])
def upload():
	return render_template('upload.html')

@routes_bp.route('/crime', methods=['POST'])
def addCrime():
	csv = request.files['file']

	filename = werkzeug.secure_filename(csv.filename)
	csv.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return uploadCrimeRecord(filename)

@routes_bp.route('/map/<city>',  methods=['GET'])
def show_crime_map(city):
    print(city)
    if city is None or city == 'chicago':
        return render_template(city + '.html')


def uploadCrimeRecord(filename):
    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    fields = app.config['DATA_COLS']
    if sorted(fields) == sorted(list(df.columns)):
        print('Uploading to Kafka topic:', app.config['KAFKA_TOPIC'])
        df.apply(lambda x: app.config['KAFKA_PRODUCER'].send(app.config['KAFKA_TOPIC'] , value = x.to_dict()), axis=1)
    else:
        helper.remove_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Incorrect Columns in the uploaded csv. The data fields of {} must match: {}'.format(filename, fields), 401
    
    return 'File uploaded successfully!'