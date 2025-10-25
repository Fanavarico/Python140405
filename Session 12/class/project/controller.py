from model import Student, samad
from sqlalchemy.exc import SQLAlchemyError  # more specific exception


class Manager:

    def add_std(self, name, last_name, age, score):
        try:
            std = Student(name=name, last_name=last_name, age=age, score=score)
            samad.add(std)
            samad.commit()
            return True
        except SQLAlchemyError as e:
            # + rollback -> mige har amaliati ke ta inja anjam dade bodi ro be halate
            # aval bargardoneshon
            samad.rollback()
            return False

    def delete_std(self, key_):
        try:
            student = samad.query(Student).filter(Student.id == key_).first()
            if student:
                samad.delete(student)
                samad.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            samad.rollback()
            return False

    def update_std(self, key_, name, last_name, age, score):
        try:
            student = samad.query(Student).filter(Student.id == key_).first()
            if student:
                student.name = name
                student.last_name = last_name
                student.age = age
                student.score = score
                samad.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            samad.rollback()
            return False

    def show_all_stds(self):
        # Only reads from DB → no need for try/except unless you want extra safety
        try:
            return samad.query(Student).all()
        except SQLAlchemyError as e:
            return []