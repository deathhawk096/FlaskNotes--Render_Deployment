from flask import Blueprint
from flask import flash,render_template,redirect,abort,request,url_for
from flask_login import login_user,logout_user,current_user,login_required
from app.models import User,Notes,Images
from app.users.users_forms import Registration_form,Login_form,Request_Reset_Form,Reset_Password_Form,Profile_form
from app import db,bcrypt
from app.users.users_utils import send_mail

users = Blueprint('users',__name__)

@users.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        flash("You're currently signed in. Please sign out before creating a new account.",'info')
        return redirect(url_for('main.home'))
    form = Registration_form()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.confirm_password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Sign Up Successfull','success')
        return redirect(url_for('users.login'))
    return render_template('register.html',title='Sign Ip',form=form)



@users.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        flash("You're already signed in. Please log out to continue.",'info')
        return redirect(url_for('main.home'))
    form=Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            next_url = request.args.get('next')
            login_user(user,remember=form.remember.data)
            flash(f"Logged in as {current_user.username}",'success')
            return  redirect(next_url) if next_url else redirect(url_for('main.home'))
        flash("Login Unsuccessfull! Please Re-Check You're Password And Email",'danger')
    return render_template('login.html',title="Login",form=form)



@users.route('/reset_password',methods=['POST','GET'])
def reset_request():
    if current_user.is_authenticated:
        flash('Please log out before making this request','info')
        return redirect(url_for('main.home'))
    form = Request_Reset_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        send_mail(user)
        flash('Password Reset link sent!Please check your inbox or spam folder','success')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html',title='Reset Request',form=form)

@users.route('/reset_password/<token>',methods=['POST','GET'])
def reset_password(token):
    if current_user.is_authenticated:
        abort(404)
    user = User.verify_token(token)
    if user is None:
        flash('The reset link is expired or invalid','info')
        return redirect(url_for('users.reset_request'))
    form = Reset_Password_Form()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.confirm_password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Password Reset Successful','success')
        return redirect(url_for('users.login'))
    return render_template('reset_password.html',title='Reset Password',form=form)



@users.route('/settings')
@login_required
def settings():
    return render_template('settings.html',title='Settings')


@users.route('/settings/<int:user_id>/profile',methods=["POST","GET"])
@login_required
def profile(user_id):
    user=User.query.get(user_id)
    if current_user != user:
        abort(403)
    form = Profile_form()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        db.session.commit()
        flash('Profile Updated Successfully!','success')
        return redirect(request.url)
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('profile.html',title='Profile',user=user,form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out Successfully!','success')
    return redirect(url_for('main.webpage'))