# Flask Notes Application 🗒️  

A full-featured **Notes Web Application** built with Flask, featuring **user authentication, profile management, image uploads, password reset via email, and CRUD operations for notes**.  

This project is deployed on **Render** with **Supabase Postgres** as the database, and integrates **SendGrid** for email services and **Cloudinary** for media storage.  

---

## 🚀 Features  

- **User Authentication**  
  - Register, Login, Logout  
  - Secure password hashing with Flask-Bcrypt  

- **Profile Management**  
  - Update username, email  

- **Password Reset via Email**  
  - SendGrid integration for secure password reset links  

- **Notes Management (CRUD)**  
  - Create, Read, Update, and Delete notes  
  - Attach images to notes (Cloudinary integration)  

- **Database & Storage**  
  - Supabase Postgres as the primary database  
  - Cloudinary for image storage and management  

- **Other Highlights**  
  - Modular structure with Flask Blueprints  
  - Database migrations with Flask-Migrate  
  - Responsive UI with Bootstrap  

---

## 🛠 Tech Stack  

- **Backend:** Flask (Python)  
- **Database:** Supabase Postgres (PostgreSQL)  
- **ORM:** SQLAlchemy  
- **Authentication:** Flask-Login  
- **Migrations:** Alembic (via Flask-Migrate)  
- **Mail Service:** SendGrid (REST API with Python SDK)  
- **Cloud Storage:** Cloudinary (Python SDK)  
- **Deployment:** Render  

---

## 🔑 Environment Variables  

Configure the following in your `.env` file or system environment:  

```python
SECRET_KEY = your_secret_key
SQLALCHEMY_DATABASE_URI = your_supabase_postgres_url

SENDGRID_API_KEY = your_sendgrid_api_key
VERIFIED_SENDER_EMAIL = your_verified_sender_email

CLOUDINARY_CLOUD_NAME = your_cloudinary_cloud_name
CLOUDINARY_API_KEY = your_cloudinary_api_key
CLOUDINARY_API_SECRET = your_cloudinary_api_secret
```

👉 [Flask Notes App on Render](https://flasknotes-render-deployment.onrender.com)

## 📸 Screenshots
![Landing Page Screenshot]<img width="1920" height="1269" alt="screencapture-flasknotes-render-deployment-onrender-webpage-2025-10-01-17_08_26" src="https://github.com/user-attachments/assets/baefeea9-29ae-4ddb-8cd3-09f99fba05a1" />

![Login Page Screenshot]<img width="1920" height="997" alt="screencapture-flasknotes-render-deployment-onrender-login-2025-10-01-17_09_01" src="https://github.com/user-attachments/assets/ab0b270e-9f3a-4c30-8603-8e761af1c435" />

![Home Page Screenshot]<img width="1920" height="997" alt="screencapture-flasknotes-render-deployment-onrender-home-2025-10-01-17_11_04" src="https://github.com/user-attachments/assets/b661bd72-3fac-443e-afca-a5af10592e29" />

![Create Note Page Screenshot]<img width="1920" height="1072" alt="screencapture-flasknotes-render-deployment-onrender-new-note-2025-10-01-17_12_23" src="https://github.com/user-attachments/assets/7f20cbcf-0d53-44a8-bcd6-9a09a0b29be6" />

![view Note Page Screenshot]<img width="1920" height="997" alt="screencapture-flasknotes-render-deployment-onrender-view-note-4-2025-10-01-17_13_27" src="https://github.com/user-attachments/assets/db44ab28-22b7-433f-be4e-c565e6d02506" />

![Update Note Page Screenshot]<img width="1920" height="2015" alt="screencapture-flasknotes-render-deployment-onrender-view-note-4-update-note-2025-10-01-17_13_55" src="https://github.com/user-attachments/assets/776e50c0-9fdc-4c3d-ad6b-134f6aee654a" />

![Settings Page Screenshot]<img width="1920" height="997" alt="screencapture-flasknotes-render-deployment-onrender-settings-2025-10-01-17_21_45" src="https://github.com/user-attachments/assets/05939f24-d230-4b28-8714-45d7a1cf18f3" />

![Profile Page Screenshot]<img width="1920" height="997" alt="screencapture-flasknotes-render-deployment-onrender-settings-1-profile-2025-10-01-17_21_58" src="https://github.com/user-attachments/assets/cde8fd12-533b-4fc3-9c8a-aa698398ef10" />
