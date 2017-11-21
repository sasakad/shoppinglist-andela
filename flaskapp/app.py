import unittest
from app import accounts

class FlaskTestCase(BaseTestCase):


   
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
 if __name__ == '__main__':
 unittest.main()  
        
