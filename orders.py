from typing import List, Dict,Union

class Orders:
    _orders:List[Dict]

    def __init__(self) -> None:
        self._orders = []
    
    @property
    def orders(self):
        return self._orders

    def __repr__(self) -> str:
        return f'Orders({self.orders})'

    def __getitem__(self,position):
        return self.orders[position]

    def __len__(self):
        return len(self.orders)

    def add_order(self, order:dict):
        repr = {
            "order_id": int,
            "customer": str,
            "total_value": float,
            "items": int
        }

        if isinstance(order,dict) \
           and set(order.keys()) == set(repr.keys()) \
           and all(type(order[key])==repr[key] for key in order
        ):
            self._orders.append(order)
        else:
            raise ValueError(
                """The order value needs to be a dict like 
                {
                "order_id": int,
                "customer": str,
                "total_value": float,
                "items": int
                }"""
            )

    def get_high_value_orders(self,min_value:Union[int,float]):
        if isinstance(min_value,(int,float)):
            return [total for order in self.orders if (total := order['total_value']) >= min_value] #Use of Walrus operator to optimization only one acess to the 'total_value' key in the order dict
        else:
            raise ValueError(
                """The value of 'min_value' needs to be integer or float"""
            )

    def total_items_sold(self):
        return sum([order['items'] for order in self.orders])
    
    
if __name__=='__main__':
    # Criando uma instância da classe Orders
    orders = Orders()

    # Adicionando pedidos
    orders.add_order({"order_id": 1, "customer": "Alice", "total_value": 150.0, "items": 3})
    orders.add_order({"order_id": 2, "customer": "Bob", "total_value": 85.5, "items": 1})
    orders.add_order({"order_id": 3, "customer": "Carol", "total_value": 200.0, "items": 5})

    # Acessando pedidos por índice
    print(orders[1])  # Pedido de Bob

    # Obtendo o número de pedidos
    print(len(orders))  # Saída: 3

    # Iterando sobre pedidos
    for order in orders:
        print(order)

    # Obtendo pedidos com valor total maior ou igual a 100
    high_value_orders = orders.get_high_value_orders(100.0)
    print(high_value_orders)

    # Calculando o total de itens vendidos
    total_items = orders.total_items_sold()
    print(f'Total de itens vendidos: {total_items}')
    print(orders)

