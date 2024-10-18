from flask import Blueprint, request, jsonify, current_app
from . import db
from .models import User, Student, Teacher, Admin, Class, Subject, Attendance, Result
import datetime
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return 'Welcome to School Management System!';

### ---------------- Authentication Endpoints ---------------- ###

'''
@main.route('/api/auth/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],  # Note: Hash the password in production
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201
'''

@main.route('/api/auth/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Hash the password before storing it
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    # Create a new user with the hashed password
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password,  # Store the hashed password
        role=data['role']
    )

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201


'''
@main.route('/api/auth/login', methods=['POST'])i
def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:  # In production, use password hashing
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401
'''

@main.route('/api/auth/login', methods=['POST'])
def login_user():
    data = request.get_json()
    
    # Fetch the user by username
    user = User.query.filter_by(username=data['username']).first()
    
    # Check if the user exists and if the password is correct (use hashed passwords in production)
    if user and check_password_hash(user.password, data['password']):
        
        # Generate the JWT token with expiration
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiration time
        }, current_app.config['SECRET_KEY'], algorithm='HS256')

        # Return the token in the response
        return jsonify({'token': token}), 200
    
    # If credentials are invalid, return an error
    return jsonify({'message': 'Invalid credentials!'}), 401

@main.route('/api/auth/logout', methods=['POST'])
def logout_user():
    return jsonify({'message': 'User logged out successfully!'}), 200


### ---------------- User Management Endpoints ---------------- ###

@main.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        }
        output.append(user_data)
    return jsonify(output)

@main.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    }
    return jsonify(user_data)

@main.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.username = data['username']
    user.email = data['email']
    user.role = data['role']
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

@main.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})


### ---------------- Student CRUD Operations ---------------- ###

@main.route('/api/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(
        user_id=data['user_id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        gender=data['gender'],
        class_id=data.get('class_id'),
        parent_contact=data.get('parent_contact'),
        address=data.get('address')
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully!'}), 201

@main.route('/api/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    output = []
    for student in students:
        student_data = {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'age': student.age,
            'gender': student.gender,
            'class_id': student.class_id,
            'parent_contact': student.parent_contact,
            'address': student.address
        }
        output.append(student_data)
    return jsonify(output)

@main.route('/api/students/<id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    student_data = {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age,
        'gender': student.gender,
        'class_id': student.class_id,
        'parent_contact': student.parent_contact,
        'address': student.address
    }
    return jsonify(student_data)

@main.route('/api/students/<id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.first_name = data['first_name']
    student.last_name = data['last_name']
    student.age = data['age']
    student.gender = data['gender']
    student.class_id = data.get('class_id')
    student.parent_contact = data.get('parent_contact')
    student.address = data.get('address')
    db.session.commit()
    return jsonify({'message': 'Student updated successfully!'})

@main.route('/api/students/<id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully!'})


### ---------------- Teacher CRUD Operations ---------------- ###

@main.route('/api/teachers', methods=['POST'])
def add_teacher():
    data = request.get_json()
    new_teacher = Teacher(
        user_id=data['user_id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        subject_specialization=data['subject_specialization'],
        phone=data['phone'],
        email=data['email']
    )
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({'message': 'Teacher added successfully!'}), 201

@main.route('/api/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    output = []
    for teacher in teachers:
        teacher_data = {
            'id': teacher.id,
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'subject_specialization': teacher.subject_specialization,
            'phone': teacher.phone,
            'email': teacher.email
        }
        output.append(teacher_data)
    return jsonify(output)

@main.route('/api/teachers/<id>', methods=['GET'])
def get_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    teacher_data = {
        'id': teacher.id,
        'first_name': teacher.first_name,
        'last_name': teacher.last_name,
        'subject_specialization': teacher.subject_specialization,
        'phone': teacher.phone,
        'email': teacher.email
    }
    return jsonify(teacher_data)

@main.route('/api/teachers/<id>', methods=['PUT'])
def update_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    data = request.get_json()
    teacher.first_name = data['first_name']
    teacher.last_name = data['last_name']
    teacher.subject_specialization = data['subject_specialization']
    teacher.phone = data['phone']
    teacher.email = data['email']
    db.session.commit()
    return jsonify({'message': 'Teacher updated successfully!'})

@main.route('/api/teachers/<id>', methods=['DELETE'])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    return jsonify({'message': 'Teacher deleted successfully!'})


### ---------------- Class CRUD Operations ---------------- ###

@main.route('/api/classes', methods=['POST'])
def add_class():
    data = request.get_json()
    new_class = Class(
        class_name=data['class_name'],
        teacher_id=data['teacher_id']
    )
    db.session.add(new_class)
    db.session.commit()
    return jsonify({'message': 'Class added successfully!'}), 201

@main.route('/api/classes', methods=['GET'])
def get_classes():
    classes = Class.query.all()
    output = []
    for class_item in classes:
        class_data = {
            'id': class_item.id,
            'class_name': class_item.class_name,
            'teacher_id': class_item.teacher_id
        }
        output.append(class_data)
    return jsonify(output)

@main.route('/api/classes/<id>', methods=['GET'])
def get_class(id):
    class_item = Class.query.get_or_404(id)
    class_data = {
        'id': class_item.id,
        'class_name': class_item.class_name,
        'teacher_id': class_item.teacher_id
    }
    return jsonify(class_data)

@main.route('/api/classes/<id>', methods=['PUT'])
def update_class(id):
    class_item = Class.query.get_or_404(id)
    data = request.get_json()
    class_item.class_name = data['class_name']
    class_item.teacher_id = data['teacher_id']
    db.session.commit()
    return jsonify({'message': 'Class updated successfully!'})

@main.route('/api/classes/<id>', methods=['DELETE'])
def delete_class(id):
    class_item = Class.query.get_or_404(id)
    db.session.delete(class_item)
    db.session.commit()
    return jsonify({'message': 'Class deleted successfully!'})


### ---------------- Subject CRUD Operations ---------------- ###

@main.route('/api/subjects', methods=['POST'])
def add_subject():
    data = request.get_json()
    new_subject = Subject(
        subject_name=data['subject_name'],
        teacher_id=data['teacher_id']
    )
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({'message': 'Subject added successfully!'}), 201

@main.route('/api/subjects', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    output = []
    for subject in subjects:
        subject_data = {
            'id': subject.id,
            'subject_name': subject.subject_name,
            'teacher_id': subject.teacher_id
        }
        output.append(subject_data)
    return jsonify(output)

@main.route('/api/subjects/<id>', methods=['GET'])
def get_subject(id):
    subject = Subject.query.get_or_404(id)
    subject_data = {
        'id': subject.id,
        'subject_name': subject.subject_name,
        'teacher_id': subject.teacher_id
    }
    return jsonify(subject_data)

@main.route('/api/subjects/<id>', methods=['PUT'])
def update_subject(id):
    subject = Subject.query.get_or_404(id)
    data = request.get_json()
    subject.subject_name = data['subject_name']
    subject.teacher_id = data['teacher_id']
    db.session.commit()
    return jsonify({'message': 'Subject updated successfully!'})

@main.route('/api/subjects/<id>', methods=['DELETE'])
def delete_subject(id):
    subject = Subject.query.get_or_404(id)
    db.session.delete(subject)
    db.session.commit()
    return jsonify({'message': 'Subject deleted successfully!'})


### ---------------- Attendance CRUD Operations ---------------- ###

@main.route('/api/attendance', methods=['POST'])
def add_attendance():
    data = request.get_json()
    new_attendance = Attendance(
        student_id=data['student_id'],
        date=data['date'],
        status=data['status']
    )
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify({'message': 'Attendance recorded successfully!'}), 201

@main.route('/api/attendance', methods=['GET'])
def get_attendance():
    attendance_records = Attendance.query.all()
    output = []
    for attendance in attendance_records:
        attendance_data = {
            'id': attendance.id,
            'student_id': attendance.student_id,
            'date': attendance.date,
            'status': attendance.status
        }
        output.append(attendance_data)
    return jsonify(output)

@main.route('/api/attendance/<student_id>', methods=['GET'])
def get_student_attendance(student_id):
    attendance_records = Attendance.query.filter_by(student_id=student_id).all()
    output = []
    for attendance in attendance_records:
        attendance_data = {
            'id': attendance.id,
            'student_id': attendance.student_id,
            'date': attendance.date,
            'status': attendance.status
        }
        output.append(attendance_data)
    return jsonify(output)

@main.route('/api/attendance/<id>', methods=['PUT'])
def update_attendance(id):
    attendance = Attendance.query.get_or_404(id)
    data = request.get_json()
    attendance.student_id = data['student_id']
    attendance.date = data['date']
    attendance.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Attendance updated successfully!'})

@main.route('/api/attendance/<id>', methods=['DELETE'])
def delete_attendance(id):
    attendance = Attendance.query.get_or_404(id)
    db.session.delete(attendance)
    db.session.commit()
    return jsonify({'message': 'Attendance deleted successfully!'})


### ---------------- Results CRUD Operations ---------------- ###

@main.route('/api/results', methods=['POST'])
def add_result():
    data = request.get_json()
    new_result = Result(
        student_id=data['student_id'],
        subject_id=data['subject_id'],
        score=data['score'],
        grade=data['grade'],
        term=data['term']
    )
    db.session.add(new_result)
    db.session.commit()
    return jsonify({'message': 'Result added successfully!'}), 201

@main.route('/api/results', methods=['GET'])
def get_results():
    results = Result.query.all()
    output = []
    for result in results:
        result_data = {
            'id': result.id,
            'student_id': result.student_id,
            'subject_id': result.subject_id,
            'score': result.score,
            'grade': result.grade,
            'term': result.term,
            'date_submitted': result.date_submitted
        }
        output.append(result_data)
    return jsonify(output)

@main.route('/api/results/<id>', methods=['GET'])
def get_result(id):
    result = Result.query.get_or_404(id)
    result_data = {
        'id': result.id,
        'student_id': result.student_id,
        'subject_id': result.subject_id,
        'score': result.score,
        'grade': result.grade,
        'term': result.term,
        'date_submitted': result.date_submitted
    }
    return jsonify(result_data)

@main.route('/api/results/<id>', methods=['PUT'])
def update_result(id):
    result = Result.query.get_or_404(id)
    data = request.get_json()
    result.student_id = data['student_id']
    result.subject_id = data['subject_id']
    result.score = data['score']
    result.grade = data['grade']
    result.term = data['term']
    db.session.commit()
    return jsonify({'message': 'Result updated successfully!'})

@main.route('/api/results/<id>', methods=['DELETE'])
def delete_result(id):
    result = Result.query.get_or_404(id)
    db.session.delete(result)
    db.session.commit()
    return jsonify({'message': 'Result deleted successfully!'})

