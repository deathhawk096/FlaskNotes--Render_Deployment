from flask import Blueprint
from flask import redirect,render_template,url_for,flash,abort,request
from flask_login import login_required,current_user
from app.notes.notes_forms import Note_form
from app.notes.notes_utils import save_pic,erase_img
from app import db
from app.models import Notes,Images

notes = Blueprint('notes',__name__)

@notes.route('/new_note',methods=['POST','GET'])
@login_required
def New_note():
    form = Note_form()
    if form.validate_on_submit():
        note = Notes(title=form.title.data,content=form.content.data,user_id=current_user.id)
        db.session.add(note)
        db.session.flush()
        if form.images.data:
            files = save_pic(form.images.data)
            for url,id in files.items():
                image = Images(image_url = url,public_id=id,notes_id = note.id)
                db.session.add(image)
        db.session.commit()
        flash('Note Saved!','success')
        return redirect(url_for('main.home'))
    return render_template('new_note.html',title='New Note',form=form)

@notes.route('/view_note/<int:note_id>')
@login_required
def view_note(note_id):
    note = Notes.query.filter_by(id = note_id).first()
    if current_user != note.author:
        abort(403)
    return render_template('view_note.html',note=note)


@notes.route('/view_note/<int:note_id>/update_note',methods=['POST',"GET"])
@login_required
def update_note(note_id):
    form = Note_form()
    Note = Notes.query.get(note_id)
    image = Images.query.filter_by(notes_id=Note.id)
    if Note.author != current_user:
        abort(403)
    if request.method == 'GET':
        form.title.data = Note.title
        form.content.data = Note.content
        form.images.data = Note.images
    if form.validate_on_submit():
        if form.images.data:
            files = save_pic(form.images.data)
            for url,id in files.items():
                img = Images(image_url=url,public_id=id,notes_id=Note.id)
                db.session.add(img)
        Note.title = form.title.data
        Note.content = form.content.data 
        db.session.commit() 
        return redirect(url_for('notes.view_note',note_id=note_id))
    return render_template('new_note.html',form=form,note=Note)

@notes.route('/update_note/<int:image_id>/delete')
@login_required
def delete_image(image_id):
    img = Images.query.get_or_404(image_id)
    if img.note.author != current_user:
        abort(403)
    erase_img(img.public_id)
    db.session.delete(img)
    db.session.commit()
    return redirect(url_for('notes.update_note',note_id=img.notes_id))

@notes.route('/view_note/<int:note_id>/delete',methods=['POST','GET'])
@login_required
def delete_note(note_id):
    note = Notes.query.get_or_404(note_id)
    image = Images.query.filter_by(notes_id=note.id)
    if note.author != current_user:
        abort(403)

    for img in image:
        db.session.delete(img)
        erase_img(img.public_id)
    db.session.delete(note)
    db.session.commit()
    flash('Note Deleted successfully!','success')
    return redirect(url_for('main.home'))
