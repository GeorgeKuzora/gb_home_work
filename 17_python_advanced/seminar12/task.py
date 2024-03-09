import csv


class Name:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, "")

    def __set__(self, obj, value: str):
        fio = value.split(sep=" ")
        check = (value.isalpha() and value[0].isupper() for value in fio)
        if all(check):
            obj.__dict__[self.name] = value
        else:
            raise ValueError(
                "ФИО должно состоять только из букв и начинаться с заглавной буквы"
            )


class Student:
    name = Name()

    def __init__(self, name, subjects_file) -> None:
        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def load_subjects(self, file_path):
        subjects = {}
        with open(file_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                for s in row:
                    subjects[s] = {}
        return subjects

    def __str__(self):
        s = []
        for key in self.subjects.keys():
            if self.subjects.get(key):
                s.append(key)
        return f"Студент: {self.name}\nПредметы: {', '.join(s)}"

    def add_grade(self, subject, grade):
        if grade >= 2 and grade <= 5 and isinstance(grade, int):
            if sub_grades := self.subjects[subject].get("grade"):
                sub_grades.append(grade)
            else:
                self.subjects[subject]["grade"] = [grade]
        else:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")

    def add_test_score(self, subject, test_score):
        if test_score >= 0 and test_score <= 100 and isinstance(test_score, int):
            if sub_tests := self.subjects[subject].get("test_score"):
                sub_tests.append(test_score)
            else:
                self.subjects[subject]["test_score"] = [test_score]
        else:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")

    def get_average_grade(self):
        count = 0
        summ = 0
        for subject in self.subjects.values():
            grades = subject.get("grade", [])
            for grade in grades:
                summ += grade
                count += 1
        average = summ / count
        return average

    def get_average_test_score(self, subject):
        if test_scores := self.subjects.get(subject, {}).get("test_score", []):
            return sum(test_scores) / len(test_scores)
        else:
            raise ValueError(f"Предмет {subject} не найден")


if __name__ == "__main__":
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
