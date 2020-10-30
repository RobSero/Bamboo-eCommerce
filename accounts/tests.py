from django.contrib.auth import get_user_model
from django.test import TestCase, Client

# Create your tests here.
client = Client()
User = get_user_model()


class URLGetRequests(TestCase):
  
  def test_register_template(self):
    register_res = client.get('/account/register/')
    self.assertEqual(register_res.status_code, 200)
    self.assertTemplateUsed(register_res, 'auth/register.html')
    
  
    def test_login_template(self):
      login_res = client.get('/account/login/')
      self.assertEqual(login_res.status_code, 200)
      self.assertTemplateUsed(login_res, 'auth/login.html')
      
      
class UserTest(TestCase):
  def setUp(self):
    new_user = User.objects.create_user(email='test@email.com',password='test123', full_name='John Tester')
    
  def test_get_user(self):
    test_user = User.objects.get(email='test@email.com')
    self.assertEqual(test_user.full_name,'John Tester')
  
  def test_login_user_and_session(self):
      login_res = client.post('/account/login/', {'email': 'test@email.com', 'password':'test123'})
      self.assertEqual(login_res.status_code, 200)
    
  