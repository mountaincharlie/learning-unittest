import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        # creating an instance of the class inorder to test it
        student = Student('Charlie', 'Harland')

        self.assertEqual(student.full_name, 'Charlie Harland')


if __name__ == '__main__':
    unittest.main()
