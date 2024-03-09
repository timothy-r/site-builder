from dependency_injector import containers, providers

from site_gen.node.node import Node

class Container(containers.DeclarativeContainer):

    node_factory = providers.Factory(
        Node
    )