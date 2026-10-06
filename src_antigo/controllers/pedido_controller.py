from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService
class PedidoController:
    """Classe de controlador para gerenciar a logica de negocio aos pedidos"""

    def __init__(self, service: PedidoService):
        self.service = service

    def adicionar_pedido(self, pedido: Pedido):
        self.service.adicionar_pedidos(pedido)

    def processar_pedidos(self):
        self.service.processar_pedidos()

    