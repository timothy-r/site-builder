import sys
from site.node.page import Page
from site.process.clean_source_service import CleanSourceService
from site.process.extraction_service import ExtractionService

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


    main(sys.argv)