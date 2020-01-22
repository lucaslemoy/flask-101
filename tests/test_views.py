from flask_testing import TestCase
import json
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 1) # 2 is not a mistake here.

    def test_get_id_name(self):
        response = self.client.get("/api/v1/products/1")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json['id'],1)
        self.assertEqual(response.json['name'],1)

    def test_get_id_name(self):
        response = self.client.delete("/api/v1/products/1")
        self.assertEqual(response.status_code,204)

    def test_error_404(self):
        response = self.client.get("/api/v1/products/5")
        self.assertEqual(response.status_code,404)

    def test_post_product(self):
        response = self.client.post("/api/v1/products", data=json.dumps({"name":"toto"}), content_type='application/json')
        self.assertEqual(response.json['id'], 4)
        self.assertEqual(response.json['name'], 'toto')

'{"name":"toto"}'
