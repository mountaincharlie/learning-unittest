import unittest
from student import Student

# refactored test class
class TestStudent(unittest.TestCase):

    # # to run a piece of code once at the start for all (e.g db setup)
    # @classmethod
    # def setUpClass(cls):
    #     print('setUpClass')

    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')


    # unittest setup method
    def setUp(self):
        print('setUp')
        # creating an instance of the Student class
        self.student = Student('Charlie', 'Harland')
    
    # unittest tearDown method (not needed in this example)
    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'Charlie Harland')

    def test_alert_santa(self):
        print('test_alert_santa')
        # non-read only methods need to be called
        self.student.alert_santa()

        # checking if naughty_list == True
        self.assertTrue(self.student.naughty_list)

    def test_student_email(self):
        print('test_student_email')
        self.assertEqual(self.student.student_email, 'charlie.harland@email.com')


# # un-refactored test class
# class TestStudent(unittest.TestCase):

#     def test_full_name(self):
#         # creating an instance of the class inorder to test it
#         student = Student('Charlie', 'Harland')

#         self.assertEqual(student.full_name, 'Charlie Harland')

#     def test_alert_santa(self):
#         student = Student('Charlie', 'Harland')
#         # non-read only methods need to be called
#         student.alert_santa()

#         # checking if naughty_list == True
#         self.assertTrue(student.naughty_list)

#     def test_student_email(self):
#         student = Student('Charlie', 'Harland')

#         self.assertEqual(student.student_email, 'charlie.harland@email.com')


if __name__ == '__main__':
    unittest.main()
