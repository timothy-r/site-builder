import sys
import logging

from site_gen.node.page import Page
from site_gen.process.clean_source_service import CleanSourceService
from site_gen.process.extraction_service import ExtractionService

def main(args):

    action = args[1]

    file = args[2]
    target = args[3]

    if 'clean' == action:
        service = CleanSourceService(root_page=file, target_dir=target)

    elif 'extract' == action:
        service = ExtractionService(root_page=file, target_dir=target)
        pass

    elif 'build' == action:
        pass

    service.process()

if __name__ == "__main__":

    # container = Container()
    # container.init_resources()
    # container.wire(modules=[__name__])

    # TODO: configure the logging
    logging.basicConfig(
        level=logging.DEBUG,
        filename='site-builder.log',
        filemode='a',
        format='%(name)s - %(levelname)s - %(message)s'
    )


    main(sys.argv)