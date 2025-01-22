from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: dict) -> 'Product':
        """Class method to load data into a Product instance."""
        return cls(data['id'], data['name'], data['description'], data['cost'], data['qty'])

    def list_products() -> list[Product]:
        """Fetch and return all products as Product instances."""
        return [Product.load(product) for product in dao.list_products()]

    def get_product(product_id: int) -> Product:
        """Fetch and return a specific product by ID."""
        product_data = dao.get_product(product_id)
        return Product.load(product_data) if product_data else None

    def add_product(product: dict):
        """Add a new product."""
        dao.add_product(product)

    def update_qty(product_id: int, qty: int):
        """Update product quantity with validation."""
        if qty < 0:
            raise ValueError('Quantity cannot be negative')
        dao.update_qty(product_id, qty)
