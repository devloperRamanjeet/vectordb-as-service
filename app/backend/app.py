from flask import Flask
from flask_restx import Api

from config.settings import load_env
from routes.provision import provision_bp
from routes.token import token_bp
from routes.embed import embed_bp
from routes.search import search_bp
from routes.delete import delete_bp
from routes.delete_instance import delete_instance_bp
from routes.launch_instance import launch_instance_bp

app = Flask(__name__)
app.config.update(load_env())

api = Api(app, title="VectorDB SaaS API", version="v2", doc="/docs")

# Register Blueprints
app.register_blueprint(provision_bp, url_prefix="/api")
app.register_blueprint(token_bp, url_prefix="/api")
app.register_blueprint(embed_bp, url_prefix="/api")
app.register_blueprint(search_bp, url_prefix="/api")
app.register_blueprint(delete_bp, url_prefix="/api")
app.register_blueprint(launch_instance_bp, url_prefix="/api")
app.register_blueprint(delete_instance_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
