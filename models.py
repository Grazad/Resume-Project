from flask_sqlalchemy import SQLAlchemy
from main import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    username = db.Column(db.String(120), unique=True)
    email   = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    password    = db.Column(db.String(120), nullable=True)


class AboutMe(db.Model):
    __tablename__ = "aboutme"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(300), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    zip = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.String, nullable=True)
    skill = db.Column(db.String(200), nullable=True)

class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=True)
    design = db.Column(db.String(120), nullable=True)
    organization  = db.Column(db.String(300), nullable=True)
    about = db.Column(db.String, nullable=True)
    s_date   = db.Column(db.String(120), nullable=True)
    e_date = db.Column(db.String(120), nullable=True)

class Education(db.Model):
    __tablename__ = "education"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=True)
    certificate_name = db.Column(db.String(300), nullable=True)
    institute = db.Column(db.String(300), nullable=True)
    about = db.Column(db.String(300), nullable=True)
    s_date    = db.Column(db.String(120), nullable=True)
    e_date= db.Column(db.String(120), nullable=True)

class Interest(db.Model):
    __tablename__ = "interest"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=True)
    int_name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(500), nullable=True)

class Social(db.Model):
    __tablename__ = "social"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=True)
    facebook = db.Column(db.String(100), nullable=True)
    twitter = db.Column(db.String(300), nullable=True)
    instagram = db.Column(db.String(300), nullable=True)
    github   = db.Column(db.String(120), nullable=True)
    youtube= db.Column(db.String(120), nullable=True)


class Expertise(db.Model):
    __tablename__ = "expertise"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=True)
    exp_name = db.Column(db.String(300), nullable=True)
    exp_info = db.Column(db.String(300), nullable=True)

class Skills(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=True)
    skill_name = db.Column(db.String(300), nullable=True)
    percentage = db.Column(db.Integer, nullable=True)
