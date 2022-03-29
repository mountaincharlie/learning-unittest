import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        # creating an instance of the class inorder to test it
        student = Student('Charlie', 'Harland')

        self.assertEqual(student.full_name, 'Charlie Harland')

    def test_alert_santa(self):
        student = Student('Charlie', 'Harland')
        # non-read only methods need to be called
        student.alert_santa()

        # checking if naughty_list == True
        self.assertTrue(student.naughty_list)

    def test_student_email(self):
        student = Student('Charlie', 'Harland')

        self.assertEqual(student.student_email, 'charlie.harland@email.com')


if __name__ == '__main__':
    unittest.main()
