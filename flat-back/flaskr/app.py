from flask import Flask
import branches

# Create the application instance
app = Flask(__name__)
app.register_blueprint(branches.bp)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
  app.run(debug=True)