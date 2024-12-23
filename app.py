from flask import Flask, request, render_template
import json
import os
import dotenv
from datetime import datetime
from models import db, User

dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Custom Jinja2 filter
@app.template_filter('format_date')
def format_date(value, format='%d %b'):
    return datetime.strptime(value, '%Y-%m-%d').strftime(format)

@app.route('/')
def index():
    with open('events.json', 'r') as file:
        events = json.load(file)
    events = sorted(events, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
    events = [event for event in events if datetime.strptime(event['date'], '%Y-%m-%d') >= datetime.now()]
    events = events[:3]
    return render_template('index.html', events=events)

@app.route('/members')
def members():
    members = User.query.all()
    return render_template('members.html', members=members)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
