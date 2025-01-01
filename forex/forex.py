# app/blueprints/forex/__init__.py
from flask import Blueprint
from flask import render_template, jsonify
from . import forex


forex = Blueprint('forex', __name__, 
                template_folder='templates',
                static_folder='static',
                static_url_path='/forex/static')

@forex.route('/')
def index():
    return render_template('forex_index.html')

@forex.route('/api/rates')
def get_rates():
    # Add your forex rate fetching logic here
    return jsonify({'status': 'success'})

