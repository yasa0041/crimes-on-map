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
	return helper.uploadCrimeRecord(filename)

@routes_bp.route('/map/<city>',  methods=['GET'])
def show_crime_map(city):
    print(city)
    if city is None or city == 'chicago':
        return render_template(city + '.html')

@routes_bp.route('/report', methods=['POST'])
def report_single_crime():
    print("Reported new Crime: " + str(request.form))
    return helper.reportCrime(request.form.to_dict(flat=False))

@routes_bp.route('/report', methods=['GET'])
def report_form():
    return render_template('report.html')