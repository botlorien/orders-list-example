# Orders

`Orders` é uma classe em Python que permite gerenciar uma lista de pedidos. A classe oferece funcionalidades para adicionar, acessar, e filtrar pedidos, além de calcular o total de itens vendidos.

## Funcionalidades

- **Adicionar Pedido (`add_order`)**: Permite adicionar um pedido, desde que siga a estrutura correta.
- **Acesso a Pedidos (`__getitem__`)**: Permite acessar um pedido pelo seu índice.
- **Tamanho da Lista de Pedidos (`__len__`)**: Retorna o número de pedidos adicionados.
- **Pedidos com Alto Valor (`get_high_value_orders`)**: Filtra e retorna os pedidos com valor acima ou igual ao especificado.
- **Total de Itens Vendidos (`total_items_sold`)**: Calcula a quantidade total de itens vendidos em todos os pedidos.
- **Representação Amigável (`__repr__`)**: Mostra a lista completa de pedidos de forma clara quando impressa.

## Exemplo de Uso

```python
# Importando a classe Orders
from orders import Orders

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

# Exibindo a lista completa de pedidos
print(orders)
```
## Como Funciona
### Adicionar Pedido (add_order)
Este método adiciona um pedido ao objeto Orders. O pedido deve ser um dicionário contendo as chaves: order_id (int), customer (str), total_value (float) e items (int). Se o formato for incorreto, um ValueError será lançado.

### Acesso a Pedidos (__getitem__)
Permite acessar um pedido pelo índice. Exemplo: orders[1] retorna o segundo pedido da lista.

### Tamanho da Lista de Pedidos (__len__)
Retorna o número de pedidos na lista. Útil para verificar quantos pedidos foram adicionados.

### Pedidos com Alto Valor (get_high_value_orders)
Recebe um valor mínimo como argumento e retorna uma lista de pedidos cujo valor total é maior ou igual ao valor fornecido.

### Total de Itens Vendidos (total_items_sold)
Calcula e retorna o total de itens vendidos em todos os pedidos registrados.

### Representação Amigável (__repr__)
Exibe a lista completa de pedidos quando o objeto é impresso.

## Requisitos
Python 3.7 ou superior.
## Instalação
1. Clone o repositório:

   ```bash
   git clone https://github.com/botlorien/orders-list-example.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd orders-list-example
   ```
3. Execução:
   ```bash
   python orders.py
   ```
## Erros Possíveis
* ValueError: Lançado quando:
  * O pedido não segue a estrutura esperada.
  * O valor mínimo para pedidos de alto valor não é um inteiro ou float.
## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE.md](https://github.com/botlorien/orders-list-example/blob/main/LICENSE) para mais detalhes.
