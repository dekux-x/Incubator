from django.test import TestCase

class TestDogs(TestCase):
    
    def test_index_get(self):
        response = self.client.get('/dogs/')
        self.assertEqual(200, response.status_code)
    
    def test_index_post(self):
        response = self.client.post('/dogs/')
        self.assertEqual(400,response.status_code)
    
    def test_index_put(self):
        response = self.client.put('/dogs/')
        self.assertEqual(400,response.status_code)
    
    def test_index_patch(self):
        response = self.client.patch('/dogs/')
        self.assertEqual(400,response.status_code)

    def test_detail_get(self):
        response = self.client.get('/dogs/australian/')
        self.assertEqual(200, response.status_code)
    
    def test_detail_breed(self):
        response = self.client.get("/dogs/sldfj/")
        self.assertEqual(404,response.status_code)

    def test_detail_post(self):
        response = self.client.post('/dogs/australian/')
        self.assertEqual(400,response.status_code)
    
    def test_detail_put(self):
        response = self.client.put('/dogs/australian/')
        self.assertEqual(400,response.status_code)
    
    def test_detail_patch(self):
        response = self.client.patch('/dogs/australian/')
        self.assertEqual(400,response.status_code)

    def test_index_content(self):
        response = self.client.get("/dogs/")
        self.assertIn("ILoveDogs", response.content.decode())
    
    def test_detail_content(self):
        response = self.client.get("/dogs/australian/")
        self.assertIn("australian", response.content.decode())
        

