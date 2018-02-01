import argparse
import config
import log

from injector import Injector


class App(object):
    def __init__(self, injector):
        self._injector = injector
        self._pubsub_client = injector.pubsub_client()

    def run(self, args):
        log.logger().info("Start worker ...")
        cb = self._injector.callback()
        self._pubsub_client.subscribe(config.SUBSCRIPTION, cb.callback)

    def run_with_prepare(self, args):
        log.logger().info("Create topic ...")
        self._pubsub_client.create_topic(config.TOPIC)
        self._pubsub_client.create_subscription(
            config.TOPIC, config.SUBSCRIPTION)
        self.run(args)

    def publish_message(self, args):
        log.logger().info("Publish message %s", args.message)
        self._pubsub_client.publish(config.TOPIC, args.message)


def init_command():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    app = App(Injector())
    # トピック作成コマンド
    parser_run_default = subparsers.add_parser(
        "default",
        help="Run worker"
    )
    parser_run_default.set_defaults(handler=app.run)

    # トピック作成コマンド
    parser_run_with_prepare = subparsers.add_parser(
        "prepare",
        help="Run worker with prepare topic and subscription."
    )
    parser_run_with_prepare.set_defaults(handler=app.run_with_prepare)

    # メッセージ公開コマンド
    parser_publish = subparsers.add_parser(
        "publish",
        help="Publish message to tipic",
    )
    parser_publish.add_argument("message", help="Message to publish")
    parser_publish.set_defaults(handler=app.publish_message)

    return parser


if __name__ == "__main__":
    parser = init_command()
    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()
