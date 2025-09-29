import cloudinary.uploader

def save_pic(image_file):
    image_url = []
    public_id = []#ignore this for now
    for img in image_file:
        result = cloudinary.uploader.upload(img,folder='note_images')
        image_url.append(result['secure_url'])
        public_id.append(result['public_id'])

    return dict(zip(image_url,public_id))

def erase_img(public_id):
    cloudinary.uploader.destroy(public_id=public_id)





# ------------------------uncomment this if you want to save images and erase images locally and use url_for(location of images saved + image name) in html to display the images to the user-----------------------------
#import os
#import secrets
#from app import app,mail
#import cloudinary.uploader
#from app import mail
#from flask_mail import Message
#from flask import url_for
#def save_pic(image_file):
#    file_name=[]
#    for img in image_file:
#        hex_code = secrets.token_hex(16)
#        _,f_ext = os.path.splitext(img.filename)
#        f_name = hex_code + f_ext
#        file_name.append(f_name)
#        picture_path = os.path.join(app.root_path,'static/images',f_name)
#        img.save(picture_path)
#
#    return file_name

#def erase_img(image_url):
#    file_path = os.path.join(app.root_path,'static/images',image_url)
#    if os.path.exists:
#        os.remove(file_path)