from src.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService
from src.repositories.pedido_repository import PedidoRepository
from src.controllers.pedido_controller import PedidoController
from src.database.connection import DatabaseConnection

if __name__ == "__main__":
    service = PedidoService()
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    controller = PedidoController()

    """Criando pedidos e aplicando descontos"""
    pedido1 = Pedido("Cliente A", DescontoNormal())
    pedido1.valor_original = 100

    pedido2 = Pedido("Cliente B", DescontoVIP())
    pedido2.valor_original = 200

    pedido3 = Pedido("Cliente C", DescontoPremium())
    pedido3.valor_original = 300

    controller.adicionar_pedidos(pedido1)
    controller.adicionar_pedidos(pedido2)
    controller.adicionar_pedidos(pedido3)

    controller.processar_pedidos()
