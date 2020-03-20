from flask import render_template
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import CalendarCreateForm


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    form = CalendarCreateForm()
    return render_template('index.html', title='Calendar Site', form=form)


@app.route('/create_cal', methods=['POST'])
def create_calendar():
    form = CalendarCreateForm()
    if form.validate_on_submit():
        return 'yay {}'.format(form.calendar_title.data)
    return 'nay:'


@app.route('/about')
def about():
    return 'about page'


@app.route('/contact')
def contact():
    return 'contact page'
