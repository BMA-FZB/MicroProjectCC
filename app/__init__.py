#__init__.py
from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask import render_template

def create_app():
    app = Flask(__name__)
    api = Api(app)




    from app.routes import create_embedded_pdf, extract_embedded_pdf

    api.add_resource(create_embedded_pdf, '/create_embedded_pdf')
    api.add_resource(extract_embedded_pdf, '/extract_embedded_pdf')


    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/<path:path>')
    def catch_all(path):
        return render_template('index.html')


    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Cloud Computing Micro-Project"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
