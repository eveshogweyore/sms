# School Management System (Python-Flask) API

This is a **School Management System** API built with **Python-Flask** and **MySQL**. The system is designed to manage the activities of a Nigerian Primary/Secondary School, providing basic features such as user registration and login, CRUD operations for students, teachers, and admins, student grade/result management, and attendance tracking.

## Table of Contents

- Project Overview
- Project Features
- Technologies Used
- Folder Structure
- Database Schema
    + Prerequisites
    + Installation
    + Running the App
- API Endpoints
- Testing with Postman
- Contributing
- License

***

## Project Overview

The **School Management System** API is a web-based backend system built using Flask to manage various school-related operations. It includes features for user authentication, managing students, teachers, administrators, class schedules, results, and attendance tracking.

This project is designed to serve as a **Minimum Viable Product (MVP)** for school management, focusing on core features, and providing flexibility for future expansion.

***

## Project Features

- **User Authentication**: Role-based access for Admin, Teachers, and Students (JWT).
- **CRUD Operations**: Manage Students, Teachers, Admins, Classes, Subjects.
- **Result/Grade Management**: Teachers can manage student grades.
- **Attendance Management**: Track student attendance.
- **RESTful API** design, suitable for integration with any frontend.

***

## Technologies Used

- **Backend Framework**: Flask
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: JSON Web Token (JWT)
- **Development Tools**: Postman (API Testing), Git, python-venv


## Folder Structure

```bash
school-management-system/
│
├── app/
│   ├── __init__.py          # Initialize Flask app and SQLAlchemy
│   ├── models.py            # Database models for users, students, teachers, etc.
│   ├── routes.py            # All API route definitions (CRUD for users, students, etc.)
│   ├── config.py            # App configuration (DB connection, JWT secret, etc.)
│
├── migrations/              # Database migrations
├── run.py                   # Main script to run the app
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
├── .gitignore               # Files/folders to ignore in Git
```

***

## Database Schema

- **Users Table**: Handles authentication (admins, teachers, students).
- **Students Table**: Stores student data (first name, last name, class, email, etc.).
- **Teachers Table**: Stores teacher data.
- **Results Table**: Stores student grades.
- **Attendance Table**: Tracks student attendance.

```sql

-- Example SQL to create users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL
);

-- Similar queries for students, teachers, results, attendance, etc.
```

***

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine.
- Git installed for version control.
- Python venv module to create isolated Python environments.
- Postman for API testing (optional but recommended).

### Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/school-management-system.git
    cd school-management-system
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the SQLite database:** The SQLite database file will be automatically created the first time you run the app.  Alternatively, you can manually create the database and apply migrations if needed.

***

## Running the App

1. **Start the Flask development server:**  `python run.py`

2. The API should now be accessible at http://127.0.0.1:5000/.

***

## API Endpoints

Here is a list of the available API endpoints for the School Management System.

**Authentication:**
- `POST /api/auth/register` - Register a new user.
- `POST /api/auth/login` - Login and retrieve a JWT token.

**Student Management:**
- `GET /api/students` - Retrieve all students.
- `GET /api/students/<id>` - Retrieve a specific student by ID.
- `POST /api/students` - Add a new student.
- `PUT /api/students/<id>` - Update student information.
- `DELETE /api/students/<id>` - Delete a student.

**Teacher Management:**
- `GET /api/teachers` - Retrieve all teachers.
- `POST /api/teachers` - Add a new teacher.
- `PUT /api/teachers/<id>` - Update teacher information.
- `DELETE /api/teachers/<id>` - Delete a teacher.

**Attendance Management:**
- `GET /api/attendance` - Retrieve attendance records.
- `POST /api/attendance` - Record attendance for a student.

**Results/Grade Management:**
- `GET /api/results/<student_id>` - Retrieve grades for a student.
- `POST /api/results` - Add or update a student's grades.

Refer to the Postman collection (provided in this repo) for detailed request and response formats.

***

## Testing with Postman

1. Open **Postman** and import the provided Postman collection from this repository (school_management_system.postman_collection.json).
2. Make sure to set up **environment variables** (like the base URL) in Postman for convenience.
3. Test the API by hitting the defined endpoints with appropriate request payloads (JSON format).

***

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request. Contributions are welcome, whether it's bug fixes, new features, or improvements to existing code.

### Steps to contribute:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

***

## License
This project is licensed under the MIT [License](#). See the LICENSE file for more information.

***

## Conclusion
The **School Management System** API is a versatile project designed to handle a school's core administrative needs. While this MVP provides basic features, it can be expanded with additional functionalities such as timetable management, parent-teacher communication, and more. We hope this project serves as a valuable foundation for school management systems.

