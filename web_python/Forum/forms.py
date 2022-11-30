from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from Models import User

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

class CreateForumForm(FlaskForm):
    title = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Title"})

    description = StringField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Description"})
    
    submit = SubmitField('Create Forum')


class CreateMessageInForumForm(FlaskForm):
    message = StringField(validators=[
                           InputRequired(), Length(min=1, max=200)], render_kw={"placeholder": "Message"})

    submit = SubmitField('Create Message')
