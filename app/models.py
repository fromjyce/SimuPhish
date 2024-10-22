from app import db

class UserInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    email_opened = db.Column(db.Boolean, default=False)
    link_clicked = db.Column(db.Boolean, default=False)
    credentials_submitted = db.Column(db.Boolean, default=False)