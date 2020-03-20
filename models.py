from datetime import datetime

from cal import db


class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calendar_hash = db.Column(db.String(256), index=True, unique=True)
    calendar_title = db.Column(db.String(256))
    calendar_events = db.relationship('CalendarEvent', backref='calendar', lazy='dynamic')

    def __repr__(self):
        return '<Calendar {} - {}>'.format(self.calendar_hash, self.calendar_title)


class CalendarEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(256))
    event_description = db.Column(db.String(16384))
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, default=datetime.now)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.id'))
