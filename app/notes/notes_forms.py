from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from flask_wtf.file import FileAllowed,MultipleFileField
from wtforms.validators import data_required,length


class Note_form(FlaskForm):

    title = StringField('Title',validators=[data_required(),length(min=2,max=200)])

    content = TextAreaField('Content',validators=[data_required(),length(min=1,max=5000)])

    images = MultipleFileField('Add Image',validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField('Save Note')