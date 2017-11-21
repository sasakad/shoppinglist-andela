import unittest
from flaskapp import accounts
class UserTest(unittest.Testcase):

    # Ensure user can register
    def user_test_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='Metah', email='metah@gmail.com',
                password='python', confirm='python'
            ), follow_redirects=True)
            

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='Metah', email='metah',
                password='python', confirm='python'
            ), follow_redirects=True)
            

    # Ensure id is correct for the current/logged in user
    def test_get_by_id(self):
        with self.client:
            self.client.post('/login', data=dict(
                username="admin", password='kuku'
            ), follow_redirects=True)
           

    # Ensure given password is correct after unhashing
    def test_check_password(self):
        user = User.query.filter_by(email='ad@min.com').first()
        


class UserViewsTests(BaseTestCase):

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            
    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

if __name__ == '__main__':
    unittest.main()
