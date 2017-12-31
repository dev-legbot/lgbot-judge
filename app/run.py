import argparse
import config
import log
import pubsub


def run(args):
    log.logger().info("Start worker ...")
    pubsub.subscribe(config.SUBSCRIPTION)


def run_with_prepare(args):
    log.logger().info("Create topic ...")
    pubsub.create_topic(config.TOPIC)
    pubsub.create_subscription(config.TOPIC, config.SUBSCRIPTION)
    run(args)


def publish_message(args):
    log.logger().info("Publish message %s", args.message)
    pubsub.publish(config.TOPIC, args.message)


def init_command():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # トピック作成コマンド
    parser_run_default = subparsers.add_parser(
        "default",
        help="Run worker"
    )
    parser_run_default.set_defaults(handler=run)

    # トピック作成コマンド
    parser_run_with_prepare = subparsers.add_parser(
        "prepare",
        help="Run worker with prepare topic and subscription."
    )
    parser_run_with_prepare.set_defaults(handler=run_with_prepare)

    # メッセージ公開コマンド
    parser_publish = subparsers.add_parser(
        "publish",
        help="Publish message to tipic",
    )
    parser_publish.add_argument("message", help="Message to publish")
    parser_publish.set_defaults(handler=publish_message)

    return parser


if __name__ == "__main__":
    parser = init_command()
    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()
