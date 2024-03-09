from dependency_injector import containers, providers

from site_gen.node.node import Node
from site_gen.generator.node_tree_generator import NodeTreeGenerator

class Container(containers.DeclarativeContainer):

    node_factory = providers.Factory(
        Node
    )

    node_tree_generator = providers.Singleton(
        NodeTreeGenerator,
        node_factory
    )