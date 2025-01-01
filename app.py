from flask import Flask
from forex.forex import forex


app = Flask(__name__)
app.register_blueprint(forex, url_prefix='/forex')

