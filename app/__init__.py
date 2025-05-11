from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt  # Add this import
from config import Config
import os

# Create extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()  # Now this will work correctly

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)  # Initialize bcrypt
    
    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Register API blueprint
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Route to serve the frontend
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_frontend(path):
        if path and os.path.exists(os.path.join(app.static_folder, path)):
            # Serve static files directly if they exist
            return send_from_directory(app.static_folder, path)
        else:
            # Otherwise serve the index.html for SPA behavior
            return send_from_directory(app.static_folder, 'index.html')
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        # In API routes, return JSON error
        if request.path.startswith('/api/'):
            return jsonify(error="Not found"), 404
        # For non-API routes, serve the SPA
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.errorhandler(500)
    def server_error(e):
        return jsonify(error="Internal server error"), 500
    
    # Shell context processor for Flask CLI
    @app.shell_context_processor
    def make_shell_context():
        # Import models here to avoid circular imports
        from app.models import (
            User, OpenDay, Event, Building, SubjectArea, 
            Registration, UserAgenda, Feedback, Course
        )
        
        return {
            'db': db, 
            'User': User,
            'OpenDay': OpenDay,
            'Event': Event,
            'Building': Building,
            'SubjectArea': SubjectArea,
            'Registration': Registration,
            'UserAgenda': UserAgenda,
            'Feedback': Feedback,
            'Course': Course
        }
    
    # Log to stdout in production if configured
    if app.config.get('LOG_TO_STDOUT'):
        import logging
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('University of Wolverhampton Open Day App startup')
    
    return app