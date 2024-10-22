from flask import render_template, request, send_file
from app import app, mail, db
from app.models import UserInteraction
from flask_mail import Message

@app.route('/send_phishing_email/<recipient>')
def send_email(recipient):
    msg = Message('Security Update Required', sender='your-email@gmail.com', recipients=[recipient])
    msg.html = render_template('email.html', user=recipient)
    mail.send(msg)
    return 'Email sent to ' + recipient

@app.route('/track_open')
def track_open():
    user = request.args.get('user')
    user_interaction = UserInteraction.query.filter_by(user_email=user).first()
    user_interaction.email_opened = True
    db.session.commit()
    return send_file('static/tracking.png', mimetype='image/png')

@app.route('/verify')
def verify():
    user = request.args.get('user')
    user_interaction = UserInteraction.query.filter_by(user_email=user).first()
    user_interaction.link_clicked = True
    db.session.commit()
    return render_template('verify.html', user=user)

@app.route('/submit_credentials', methods=['POST'])
def submit_credentials():
    user = request.args.get('user')
    user_interaction = UserInteraction.query.filter_by(user_email=user).first()
    user_interaction.credentials_submitted = True
    db.session.commit()
    return 'Credentials submitted. This was a phishing simulation.'

@app.route('/report')
def report():
    users = UserInteraction.query.all()
    return render_template('report.html', users=users)
