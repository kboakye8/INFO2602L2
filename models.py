from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
from app import app

db = SQLAlchemy(app)


class Graduate(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  firstname= db.Column(db.String(80), nullable=False)
  lastname=db.Column(db.String(80),nullable=False)
  email= db.Column(db.String(120), unique=True, nullable=False)
  password= db.Column(db.String(120), nullable=False)
  
  def __init__(self,firstname,last,email,password):
    self.firstname=firstname
    self.lastname=lastname
    self.email=email
    self.password=generate_password_hash(password)

class Employer(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  name= db.Column(db.String(80), nullable=False)
  email= db.Column(db.String(120), unique=True, nullable=False)
  password= db.Column(db.String(120), nullable=False)

  def __init__(self,name,email,password):
    self.name=name
    self.email=email
    self.password=generate_password_hash(password)

class Job(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  title= db.Column(db.String(80), nullable=False)
  description= db.Column(db.String(120), unique=True, nullable=False)
  salary = db.Column(db.Integer, nullable=False)
  employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
  employer= db.relationship('Employer', backref=db.backref('jobs', lazy=True))
  type=db.Column(db.String(80),nullable=False, default='full-time')

  def __init__(self,title,description,salary,employer_id,type):
    self.title=title
    self.description=description
    self.salary=salary
    self.employer_id=employer_id
    self.type=type

class Application(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  job_id=db.Column(db.Integer,db.ForeignKey('job.id'), nullable=False)
  graduate_id= db.Column(db.Integer,db.ForeignKey('graduate.id'), nullable=False)
  status=db.Column(db.String(80), nullable=False, default='pending')  
  job= db.relationship('Job', backref=db.backref('applications',lazy=True))
  graduate= db.relationship('Graduate', backref=db.backref('applications',lazy=True))
  applicants=db.relationship('Applicant',secondary="applicants", backref=db.backref('job'))

  def __init__(self,job_id,graduate_id,status):
    self.job_id=job_id
    self.graduate_id=graduate_id
    self_status=status