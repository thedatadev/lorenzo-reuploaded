from flask_sqlalchemy import SQLAlchemy

# Not initialized as SQLAlchemy(app) since it needs to be shared by multiple files.
# It is initialized in modules.__init__.py using db.init_app(app)
db = SQLAlchemy()