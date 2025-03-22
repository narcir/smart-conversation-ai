import unittest
import os
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_upload_no_file(self):
        response = self.app.post('/upload')
        self.assertEqual(response.status_code, 400)
        
    # 当你有示例音频文件时，可以添加更多测试

if __name__ == '__main__':
    unittest.main()