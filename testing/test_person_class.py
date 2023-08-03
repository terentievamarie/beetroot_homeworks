import unittest
import person_class


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = person_class.Person(
            'Maria', 'Terentieva', 20, "Ukraine", "Kiyv")

    def test_age_difference(self):
        self.assertEqual(self.person.age_difference(23),
                         "You're 3 years older than me.")
        self.assertEqual(self.person.age_difference(18),
                         "I'm 2 years older than you.")
        self.assertEqual(self.person.age_difference(20),
                         "We're the same age.")


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = person_class.Student(
            'Maria', 'Terentieva', 20, "Ukraine", "Kiyv", 1234, "KNU", "engineering")

    def test_return_student_ID(self):
        student_ID = self.student.return_student_ID("KNU", 'Maria')
        self.assertEqual(student_ID, 1234)
        self.assertNotEqual(student_ID, "1234")
        self.assertNotEqual(student_ID, 2345)


class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.teacher = person_class.Teacher(
            'Maria', 'Terentieva', 20, 'Ukraine', 'Kiyv', 'KNU', "english teacher", 12000)

    def test_salary_supplement(self):

        self.assertEqual(self.teacher.salary_supplement(50), 18000)
        self.assertNotEqual(self.teacher.salary_supplement(50), 12000)

    def test_threat(self):
        self.assertEqual(self.teacher.threat("Inna"),
                         "Did you leave your head at home? I'll call your parents, Inna.")


unittest.main()
