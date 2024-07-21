"""
This module defines constants used throughout the application
"""
DATA = {"records": [
    {'username': 'kumar123', 'name': 'kumar.M', 'dept': 'DEV', 'dob': '2001-2-2', 'gender': 'M',
     'password': 'Kumar@123', 'isadmin': False},
    {'username': 'dinesh2003', 'name': 'dinesh.A', 'dept': 'APP', 'dob': '2001-2-3', 'gender': 'M',
     'password': 'Dinesh&2003', 'isadmin': False},
    {'username': 'donlee1970', 'name': 'Donlee.L', 'dept': 'APP', 'dob': '2002-8-7', 'gender': 'M',
     'password': 'Donlee@1970', 'isadmin': True}
]}
VALID_GENDER = ["MALE", "FEMALE", "OTHERS", "M", "F"]
USERS = ["kumar.M", "dinesh.A"]
ADMINS = ["Donlee.L"]
ALL_USERS = ["kumar.M", "dinesh.A", "Donlee.L"]

# create_user constant values
ADMIN = "admin"
NORMAL = "normal"
SUCCESS = "success"
FAILED = "failed"

# emails configurations
SMTP_PORT = 587
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "dineshsai14211@gmail.com"
RECEIVER_EMAIL = ["dineshsai14211@gmail.com", "danepaku@gitam.in"]
PASSWORD = "izdlrkcuyzrlwxec"

DELETE_MESSAGE = """
Hlo Team,\n
Admin has deleted user {} Record in DATA
Thank you 
"""
UPDATE_MESSAGE = """
Hlo Team,\n
Admin has updated user={} record.
Record = {}\n
Thank You
"""
GET_ALL_MESSAGE = """
Hlo Team,\n
User, is checking all users information from the table.\n
Thank You
"""
PARTIAL_UPDATE = """
Hlo Team\n
Admin has partially updated the user={} records in DATA.\n
Partially updated user record = {}\n
Thank you
"""
UNAUTHENTICATED_MESSAGE = """
Hlo team\n
ALERT:-Unauthenticated user={}, trying to access the application
check logs\n
Thank You
"""
UPDATE_USER_RECORD = """
Hlo team\n
''User={} has updated his profile''
Updated Record = {}
\nThank you
"""
RECORD_ADDED = """
Hlo Team,\n 
Admin={} added the user={} record = {}.\n
Thank You
"""
RESET_PASSWORD = """
Hlo Team\n
Admin has reseted the user={} password\n
Thank You
"""
CHECK_USER_INFO = """
Hlo Team,\n
Admin checking user={} information.\n
Thank You
"""
USER_INFO = """
Hlo Team,\n
User={} checking his information.\n
Thank You
"""
