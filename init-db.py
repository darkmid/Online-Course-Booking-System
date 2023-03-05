from app import create_app
from app.campus.model import Campus
from app.user.model import Admin,Student,Teacher,get_hashed_password

print("Loading...")

create_app()

print("Configuring database")

Campus.objects().delete()

unimelb_campus = Campus(name="unimelb")
unimelb_campus.save()

admin=Admin(
    username="admin",
    display_name="Admin",
    password=get_hashed_password("password"),
    telephone="123",
    permissions=["sys_owner","campus_admin","course_admin"],
    campus=unimelb_campus,
)
admin.save()

student=Student(
    username="student",
    display_name="John Smith",
    password=get_hashed_password("password"),
    telephone="123",
    wx="wx123",
    uni="Unimelb",
    campus=unimelb_campus,
)
student.save()

teacher=Teacher(
    username="teacher_1",
    display_name="Teacher",
    password=get_hashed_password("password"),
    telephone="123",
    abn="123123123123123",
    campus=unimelb_campus,
)
teacher.save()
