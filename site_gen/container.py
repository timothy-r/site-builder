from dependency_injector import containers, providers

from site_gen.node.node import Node
from site_gen.generator.node_tree_generator import NodeTreeGenerator
from site_gen.reader.reader_factory import ReaderFactory

class Container(containers.DeclarativeContainer):

    node_factory = providers.Factory(
        Node
    )

    reader_factory = providers.Factory(
        ReaderFactory
    )

    node_tree_generator = providers.Singleton(
        NodeTreeGenerator,
        node_factory,
        reader_factory
    )

