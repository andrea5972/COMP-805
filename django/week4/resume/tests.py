from django.test import TestCase
from resume.models import Resume, Experience, Education


class ResumeTestCase(TestCase):

    def setUp(self):
        """
        Setup is ran before every test case
        For each Model create objects for test database
        """
        Resume.objects.create(First_name="Andrea", Last_name ="Murphy")
        Experience.objects.create(
                                                    company="Three Owl Design",
                                                    title="Owner",
                                                    location= "New Boston"
                                                    )
        Education.objects.create(
                                                    institution_name="UNH",
                                                    location="Manchester",
                                                    major="MSIT",
                                                    degree="Master",
                                                    gpa= "4.0"
                                                    )

    def test_db(self):
        """
        Testing the setUp for our test DB
        """
        resume = Resume.objects.get(First_name="Andrea")
        self.assertIsInstance(resume, Resume)


    def test_get_full_name(self):
        """
        Testing the method get_full_name
        """
        resume = Resume.objects.get( First_name= 'Andrea')
        expected = 'Andrea Murphy'
        actual = resume.get_full_name()

        self.assertEqual( expected, actual)

    def test_get_experience(self):
        """
        Testing the method get_experience
        """
        resume = Resume.objects.first()
        expected = list(resume.experience_set.all())
        actual = list(resume.get_experience())

        self.assertEqual( expected, actual )

    def test_get_education(self):
        """
        Testing the method get_education
        """
        resume = Resume.objects.first()
        expected = list(resume.education_set.all())
        actual = list(resume.get_education())

        self.assertEqual( expected, actual )
