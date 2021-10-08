from flask import Flask, flash, render_template, request, session, redirect, url_for, current_app
import os
from jinja2 import Markup
from datetime import datetime
import secrets
from models import *

app = Flask(__name__)

db = SQLAlchemy()
app.config['WTF_CSRF_SECRET_KEY'] = "b'f83l\x19\xad\x84\x08\xaa\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://admin:12345678@localhost:3306/fayaz"
app.config['SECRET_KEY'] = "b'f\xfa\x8b{X\x8b84\x08\\x19\xad\x84\x08\xaa"
app.config['UPLOAD_FOLDER'] = '/home/wali/PycharmProjects/resume/static/img/profile/'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize 
db.init_app(app)


def save_images(photo):
    hash_photo= secrets.token_urlsafe(20)
    _, file_extension = os.path.splitext(photo.filename)
    photo_name= hash_photo + file_extension
    file_path= os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], photo_name)
    photo.save(file_path)
    return photo_name

@app.route("/hello")
def hello():
        me = db.session.query(Users, AboutMe).filter(Users.username == session.get('username')).filter(
            AboutMe.uid == Users.id).first()
        return render_template("index.html", me=me)

@app.route("/")
def home():
    if session.get('username'):
        me = db.session.query(Users, AboutMe).filter(Users.username == session.get('username')).filter(
            AboutMe.uid == Users.id).first()
        return render_template("user/index.html", me=me)
    else:
        return redirect(url_for('login'))


@app.route("/register" , methods=['POST','GET'])
def register():
    if session.get('username'):
        return redirect(url_for('home'))
    if request.method=="POST":
        name= request.form.get("name")
        username = request.form.get("username").lower().replace(" ","")
        password = request.form.get("password")
        email= request.form.get("email")
        phone = request.form.get("phone")
        already= Users.query.filter_by(username=username).first()
        if already:
            return redirect(url_for('login'))
        else:
            new = Users(name=name, phone=phone, email=email, username=username,password=password)
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('login'))
    else:
        return render_template("user/auth-register.html")

@app.route("/login" , methods=['POST','GET'])
def login():
    if session.get('username'):
        return redirect(url_for('home'))
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        std = Users.query.filter_by(username=username, password=password).first()
        if std:
            session['username'] = username
            session['id'] = std.id
            # session['password'] = User.password
            return redirect(url_for('home'))
        else:
            error = "Incorrect Username or Password"
            return render_template("user/auth-login.html", error=error)
    else:
        return render_template("user/auth-login.html")

@app.route("/logout")
def logout():
        session.clear()
        return redirect(url_for('login'))

@app.route("/manage-education")
def education():
    if session.get('username'):
        edu = db.session.query(Users, Education) \
            .filter(Users.username == session.get('username')) \
            .filter(Education.uid == Users.id).all()
        return render_template("user/mg-education.html", edu=edu)
    else:
        return redirect(url_for('login'))

@app.route("/add-education", methods=['POST', 'GET'])
def add_degree():
    if session.get('username'):
        if request.method=='POST':
            degree= request.form.get('degree')
            inst= request.form.get('institute')
            s_date=request.form.get('s_date')
            e_date= request.form.get('e_date')
            abt=request.form.get('about')
            new= Education(uid=session.get('id'), certificate_name=degree, institute=inst, about=abt, s_date=s_date,e_date=e_date)
            db.session.add(new)
            db.session.commit()
            flash('ADDED SUCCESSFULLY')
            return render_template("user/add_education.html")
        else:
            return render_template("user/add_education.html")
    else:
        return redirect(url_for('login'))

@app.route("/edit-education/edit_id=<id>", methods=['POST', 'GET'])
def edit_degree(id):
    req = db.session.query(Education, Users).filter(Education.id == id).filter(Users.id == session.get('id')).first()
    edit = db.session.query(Education, Users).filter(Education.id == id).filter(Users.id == session.get('id')).first()
    if edit:
        if session.get('username'):
            if request.method == 'POST':
                degree = request.form.get('degree')
                inst = request.form.get('institute')
                s_date = request.form.get('s_date')
                e_date = request.form.get('e_date')
                abt = request.form.get('about')
                edit.Education.certificate_name = degree
                edit.Education.institute = inst
                edit.Education.s_date = s_date
                edit.Education.e_date = e_date
                edit.Education.about = abt
                db.session.commit()
                flash('UPDATED SUCCESSFULLY')
                return render_template("user/edit_education.html", req=req)
            else:
                return render_template("user/edit_education.html", req=req)
        else:
            return render_template("404.html", req=req)
    else:
        return redirect(url_for('login'))


@app.route("/delete-degree/id=<id>")
def delete_education(id):
    if session.get('username'):
            rem= db.session.query(Education).filter(Education.id==id).first()
            db.session.delete(rem)
            db.session.commit()
            return redirect(url_for('education'))
    else:
        return redirect(url_for('login'))

@app.route("/about-me", methods=['POST', 'GET'])
def about():
    if session.get('username'):
        abt= db.session.query(Users, AboutMe) \
            .filter(Users.username == session.get('username')) \
            .filter(AboutMe.uid == Users.id).first()
        if request.method == 'POST':
            skill= request.form.get("skill")
            bio= request.form.get("bio")
            pic = request.files.get('image')
            country= request.form.get("country")
            address=request.form.get("address")
            city= request.form.get("city")
            zip= request.form.get("zip")
            _, file_extension = os.path.splitext(pic.filename)
            if ('.jpg' or '.jpeg' or '.png') in file_extension:
                if abt is None:
                    abt = AboutMe(skill=skill, image= save_images(pic), bio=bio, uid=session.get('id'), country=country, address=address,city=city, zip=zip)
                    db.session.add(abt)
                    db.session.commit()
                else:
                    abt.AboutMe.skill = skill
                    abt.AboutMe.bio = bio
                    abt.AboutMe.image= save_images(pic)
                    abt.AboutMe.country = country
                    abt.AboutMe.address = address
                    abt.AboutMe.ciy = city
                    abt.AboutMe.zip = zip
                    db.session.commit()
                return render_template("user/mg-about.html")
            else:
                abt.AboutMe.skill = skill
                abt.AboutMe.bio = bio
                abt.AboutMe.country = country
                abt.AboutMe.address = address
                abt.AboutMe.ciy = city
                abt.AboutMe.zip = zip
                db.session.commit()
                return render_template("user/mg-about.html",abt=abt)
        else:
            return render_template("user/mg-about.html",abt=abt)
    else:
        return render_template("user/auth-login.html")

@app.route("/profile", methods=['POST', 'GET'])
def account():
    if session.get('username'):
        b = db.session.query(Users).filter_by(username=session.get('username')).first()
        if request.method == 'POST':
            name= request.form.get("name")
            email= request.form.get("email")
            phone= request.form.get("phone")
            b.name=name
            b.email=email
            b.phone=phone
            db.session.commit()
            return render_template("user/profile.html",b=b)
        else:
            return render_template("user/profile.html",b=b)
    else:
        return render_template("user/auth-login.html")


@app.route("/work-details")
def work():
    if session.get('username'):
        work = db.session.query(Users, WorkExperience) \
            .filter(Users.username == session.get('username')) \
            .filter(WorkExperience.uid == Users.id).all()
        return render_template("user/mg-experience.html", work=work)
    else:
        return redirect(url_for('login'))

@app.route("/add-work", methods=['POST', 'GET'])
def add_work():
    if session.get('username'):
        if request.method=='POST':
            design= request.form.get('design')
            org= request.form.get('org')
            s_date=request.form.get('s_date')
            e_date= request.form.get('e_date')
            abt=request.form.get('about')
            new= WorkExperience(uid=session.get('id'), design=design,organization=org, about=abt, s_date=s_date,e_date=e_date)
            db.session.add(new)
            db.session.commit()
            flash('ADDED SUCCESSFULLY')
            return render_template("user/add_work.html")
        else:
            return render_template("user/add_work.html")
    else:
        return redirect(url_for('login'))

@app.route("/edit-Work/edit_id=<id>", methods=['POST', 'GET'])
def edit_work(id):
    if session.get('username'):
        req = db.session.query(WorkExperience, Users).filter(WorkExperience.id == id).filter(Users.id == session.get('id')).first()
        edit = db.session.query(WorkExperience, Users).filter(WorkExperience.id == id).filter(
            Users.id == session.get('id')).first()
        if edit:
            if request.method == 'POST':
                design = request.form.get('design')
                org = request.form.get('org')
                s_date = request.form.get('s_date')
                e_date = request.form.get('e_date')
                abt = request.form.get('about')
                edit.WorkExperience.design = design
                edit.WorkExperience.organization = org
                edit.WorkExperience.s_date = s_date
                edit.WorkExperience.e_date = e_date
                edit.WorkExperience.about = abt
                db.session.commit()
                flash('UPDATED SUCCESSFULLY')
                return render_template("user/edit_work.html", req=req)
            else:
               return render_template("user/edit_work.html", req=req)
        else:
            return render_template("404.html")
    else:
        return redirect(url_for('login'))


@app.route("/delete-work_experience/id=<id>", methods=['POST', 'GET'])
def delete_work(id):
    if session.get('username'):
            rem= db.session.query(WorkExperience).filter(WorkExperience.id==id).first()
            db.session.delete(rem)
            db.session.commit()
            return redirect(url_for('work'))
    else:
        return redirect(url_for('login'))

@app.route("/manage-expertise")
def expertise():
    if session.get('username'):
        expert = db.session.query(Users, Expertise) \
            .filter(Users.username == session.get('username')) \
            .filter(Expertise.uid == Users.id).all()
        return render_template("user/mg-expertise.html", expert=expert)
    else:
        return redirect(url_for('login'))

@app.route("/add-expertise", methods=['POST', 'GET'])
def add_expertise():
    if session.get('username'):
        if request.method=='POST':
            name= request.form.get('name')
            abt=request.form.get('about')
            new= Expertise(uid=session.get('id'), exp_name=name,exp_info=abt)
            db.session.add(new)
            db.session.commit()
            flash('ADDED SUCCESSFULLY')
            return render_template("user/add_expertise.html")
        else:
            return render_template("user/add_expertise.html")
    else:
        return redirect(url_for('login'))

@app.route("/edit-experience/edit_id=<id>", methods=['POST', 'GET'])
def edit_expertise(id):
    if session.get('username'):
        req = db.session.query(Expertise, Users).filter(Expertise.id == id).filter(Users.id == session.get('id')).first()
        edit = db.session.query(Expertise, Users).filter(Expertise.id == id).filter(
            Users.id == session.get('id')).first()
        if edit:
            if request.method == 'POST':
                name = request.form.get('name')
                abt = request.form.get('about')
                edit.Expertise.exp_name = name
                edit.Expertise.exp_info = abt
                db.session.commit()
                flash('UPDATED SUCCESSFULLY')
                return render_template("user/edit_expertise.html", req=req)
            else:
               return render_template("user/edit_expertise.html", req=req)
        else:
            return render_template("404.html")
    else:
        return redirect(url_for('login'))


@app.route("/delete-experience/id=<id>", methods=['POST', 'GET'])
def delete_exp(id):
    if session.get('username'):
            rem= db.session.query(Expertise).filter(Expertise.id==id).first()
            db.session.delete(rem)
            db.session.commit()
            return redirect(url_for('expertise'))
    else:
        return redirect(url_for('login'))

@app.route("/manage-skills")
def skills():
    if session.get('username'):
        skill = db.session.query(Users, Skills) \
            .filter(Users.username == session.get('username')) \
            .filter(Skills.uid == Users.id).all()
        return render_template("user/mg-skills.html", skill=skill)
    else:
        return redirect(url_for('login'))

@app.route("/add-skill", methods=['POST', 'GET'])
def add_skill():
    if session.get('username'):
        if request.method=='POST':
            skil= request.form.get('skill')
            percent=request.form.get('percent')
            new= Skills(uid=session.get('id'), skill_name=skil,percentage=percent)
            db.session.add(new)
            db.session.commit()
            flash('ADDED SUCCESSFULLY')
            return render_template("user/add_skill.html")
        else:
            return render_template("user/add_skill.html")
    else:
        return redirect(url_for('login'))

@app.route("/edit-skill/edit_id=<id>", methods=['POST', 'GET'])
def edit_skill(id):
    if session.get('username'):
        req = db.session.query(Skills, Users).filter(Skills.id == id).filter(Users.id == session.get('id')).first()
        edit = db.session.query(Skills, Users).filter(Skills.id == id).filter(
            Users.id == session.get('id')).first()
        if edit:
            if request.method == 'POST':
                name = request.form.get('skill')
                abt = request.form.get('percent')
                edit.Skills.skill_name = name
                edit.Skills.percentage = abt
                db.session.commit()
                flash('UPDATED SUCCESSFULLY')
                return render_template("user/edit_skill.html", req=req)
            else:
               return render_template("user/edit_skill.html", req=req)
        else:
            return render_template("404.html")
    else:
        return redirect(url_for('login'))

@app.route("/delete-skill/id=<id>", methods=['POST', 'GET'])
def delete_skill(id):
    if session.get('username'):
            rem= db.session.query(Skills).filter(Skills.id==id).first()
            db.session.delete(rem)
            db.session.commit()
            flash('Deleted Succesfully')
            return redirect(url_for('skills'))
    else:
        return redirect(url_for('login'))

@app.route("/resume/<user>")
def resume(user):
    verify = Users.query.filter_by(username=user).first()
    if verify is None:
        return render_template("404.html" ,user=user)
    else:
        exp =  db.session.query(Users, Expertise) \
        .filter(Users.username==user) \
        .filter(Expertise.uid==Users.id).all()

        skil = db.session.query(Users, Skills) \
        .filter(Users.username == user) \
        .filter(Skills.uid == Users.id).all()

        work = db.session.query(Users, WorkExperience) \
        .filter(Users.username == user) \
        .filter(WorkExperience.uid == Users.id).all()

        edu = db.session.query(Users, Education) \
            .filter(Users.username == user) \
            .filter(Education.uid == Users.id).all()

        about = db.session.query(Users, AboutMe) \
        .filter(Users.username == user) \
        .filter(AboutMe.uid == Users.id).first()

        soc= db.session.query(Users, Social) \
        .filter(Users.username == user) \
        .filter(Social.uid == Users.id).first()

        interest = db.session.query(Users, Interest) \
            .filter(Users.username == user) \
            .filter(Interest.uid == Users.id).all()

        person = Users.query.filter_by(username=user).first()
        return render_template('index.html', interest=interest,about=about, work=work,edu=edu,soc=soc,skil=skil,
                               user=user,exp=exp, person=person)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")

if __name__ == "__main__":

    app.run(debug=True, port=5001)
