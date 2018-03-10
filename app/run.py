import argparse
import config
import log

from injector import Injector


class App(object):
    def __init__(self, injector):
        self._injector = injector
        self._pubsub_client = injector.pubsub_client()
        self._logger = injector.logger(__name__)

    def run(self, args):
        self._logger.info("Start worker ...")
        cb = self._injector.callback()
        self._pubsub_client.subscribe(config.SUBSCRIPTION, cb.callback)


def init_command():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    app = App(Injector())
    parser_run_default = subparsers.add_parser(
        "default",
        help="Run worker"
    )
    parser_run_default.set_defaults(handler=app.run)

    return parser


if __name__ == "__main__":
    parser = init_command()
    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()
