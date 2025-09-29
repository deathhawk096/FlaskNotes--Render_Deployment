from flask_mail import Message
from flask import url_for
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail,Email
import os


def send_mail(user):
    token = user.get_reset_token()
    reset_url = url_for('users.reset_password',token=token,_external=True)

    message = Mail(from_email=Email('deathhawk096@gmail.com','Flask Note Reset Password'),
                   to_emails=user.email,
                   subject='Password reset request link',
                   html_content=f'''<p>To reset your password,visit this following link:</p>
                   <p><a href = "{reset_url}">{reset_url}</a></p>
                   <p>If you did not make this request then please ignore this email.</p>'''
                   )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)

    except Exception as e:
        raise e

#from app import mail
#def send_mail(user):
#    token = user.get_reset_token()
#
#    msg = Message('Password Reset Link',recipients=[user.email],sender='noreply@demo.com')
#
#    msg.body = f'''To reset the password click the following link below!:
#{url_for('users.reset_password',token=token,_external=True)}
#If you did not make this request simply ignore this email and no changes will be made!
#'''
#    mail.send(msg) 


#6FyRDPLacHYW6MQX