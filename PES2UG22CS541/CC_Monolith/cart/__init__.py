import products
from cart import dao
from products import Product
from typing import List

class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> 'Cart':
        contents = [products.get_product(product_id) for product_id in data['contents']]
        return Cart(data['id'], data['username'], contents, data['cost'])

    @staticmethod
    def get_cart(username: str) -> List[Product]:
        cart_details = dao.get_cart(username)
        if not cart_details:
            return []
        return [
            products.get_product(product_id)
            for cart_detail in cart_details
            for product_id in cart_detail['contents']
        ]

    @staticmethod
    def add_to_cart(username: str, product_id: int):
        dao.add_to_cart(username, product_id)

    @staticmethod
    def remove_from_cart(username: str, product_id: int):
        dao.remove_from_cart(username, product_id)

    @staticmethod
    def delete_cart(username: str):
        dao.delete_cart(username)
