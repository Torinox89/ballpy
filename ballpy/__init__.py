from flask import Flask, redirect
from flask_migrate import Migrate

#Aplication Factory:
def create_app(): 
    app = Flask(__name__)

#Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tundrass@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index(): 
        return redirect('/reptiles')

    # register "reptiles" blueprint 
    from . import reptile
    app.register_blueprint(reptile.bp)

    return app
