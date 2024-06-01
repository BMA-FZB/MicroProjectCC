import unittest
from app import create_app

class PdfsToBase64TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_convert_pdfs(self):
        with open('app/Ressource/helloWorld.pdf', 'rb') as pdf1, open('app/Ressource/Micro.pdf', 'rb') as pdf2:
            data = {
                'files': (pdf1, 'helloWorld.pdf'),
                'files': (pdf2, 'Micro.pdf')
            }
            response = self.client.post('/convert', data=data, content_type='multipart/form-data')
            self.assertEqual(response.status_code, 200)
            self.assertIn('base64_pdfs', response.json)

if __name__ == '__main__':
    unittest.main()
