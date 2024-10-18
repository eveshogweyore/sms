import os
import secrets

class Config:
    SECRET_KEY = os.urandom(24)  # For session management and security
    SQLALCHEMY_DATABASE_URI = 'mysql://alx_final_project:Alonso_22@localhost/school_management_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(32)
