import json
from saleapp import app
def load_categories():
    with open('data/categories.json',encodings='utf-8') as f:
        return json.load(f)