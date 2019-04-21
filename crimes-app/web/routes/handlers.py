from flask import Flask, render_template
from flask import Blueprint

routes_bp = Blueprint('report', __name__)

@routes_bp.route('/crime/status')
def status():
	return render_template("status.html")