from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes,models
#to je pa zato na koncu skripte, ker routes modul importa app spremenljivko,ki je definirana v tej skripti, torej gre za recipročno importanje in če je to definirano na dnu skripte se izognemo errorju


