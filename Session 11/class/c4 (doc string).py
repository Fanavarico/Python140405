samad = 1
class Student:
    pass
class Enrollment:
    pass
SQLAlchemyError = 1


# V1
class StudentManager:
    @staticmethod
    def commit_session():
        try:
            samad.commit()
            return True, "Operation successful!"
        except SQLAlchemyError as e:
            samad.rollback()
            return False, f"Database error: {e}"

    def add_student(self, name, last_name, age):
        std_data = Student(name=name, last_name=last_name, age=age)
        samad.add(std_data)
        success, msg = self.commit_session()
        if success:
            return f"Student {name} {last_name} saved successfully!"
        return msg

    def update_student(self, key_, name, last_name, age):
        student_db = samad.query(Student).filter(Student.id == key_).first()
        if not student_db:
            return f"Student with ID {key_} not found!"

        student_db.name = name
        student_db.last_name = last_name
        student_db.age = age
        success, msg = self.commit_session()
        if success:
            return f"Student ID {key_} updated successfully!"
        return msg

    def delete_student(self, key_):
        student_db = samad.query(Student).filter(Student.id == key_).first()
        if not student_db:
            return f"Student with ID {key_} not found!"

        samad.delete(student_db)
        success, msg = self.commit_session()
        if success:
            return f"Student ID {key_} deleted successfully!"
        return msg

    def show_all_students(self):
        return samad.query(Student).all()

    def show_student_courses(self, student_id):
        student = samad.query(Student).filter(Student.id == student_id).first()
        return student.enrollments if student else []




# V2
from typing import Union
class StudentManager:
    """Manager class to handle CRUD operations for Student table."""

    # Commit session safely
    @staticmethod
    def commit_session() -> tuple[bool, str]:
        """Helper to commit the session safely."""
        try:
            samad.commit()
            return True, "Operation successful!"
        except SQLAlchemyError as e:
            samad.rollback()
            return False, f"Database error: {e}"

    # ➕ Add student
    def add_student(self, name: str, last_name: str, age: int) -> str:
        """Add a new student to the database."""
        std_data = Student(name=name, last_name=last_name, age=age)
        samad.add(std_data)
        success, msg = self.commit_session()
        if success:
            return f"Student {name} {last_name} saved successfully!"
        return msg

    # 🔁 Update student
    def update_student(self, key_: int, name: str, last_name: str, age: int) -> str:
        """Update an existing student's data by ID."""
        student_db = samad.query(Student).filter(Student.id == key_).first()
        if not student_db:
            return f"Student with ID {key_} not found!"

        student_db.name = name
        student_db.last_name = last_name
        student_db.age = age
        success, msg = self.commit_session()
        if success:
            return f"Student ID {key_} updated successfully!"
        return msg

    # ❌ Delete student
    def delete_student(self, key_: int) -> str:
        """Delete a student from the database by ID."""
        student_db = samad.query(Student).filter(Student.id == key_).first()
        if not student_db:
            return f"Student with ID {key_} not found!"

        samad.delete(student_db)
        success, msg = self.commit_session()
        if success:
            return f"Student ID {key_} deleted successfully!"
        return msg

    # 📋 Show all students
    def show_all_students(self) -> list[Student]:
        """Return a list of all students."""
        return samad.query(Student).all()

    # 📚 Show student’s enrolled courses
    def show_student_courses(self, student_id: int) -> Union[list[Enrollment], list]:
        """Return all courses (enrollments) for a given student."""
        student = samad.query(Student).filter(Student.id == student_id).first()
        return student.enrollments if student else []

print(StudentManager.show_student_courses.__doc__)