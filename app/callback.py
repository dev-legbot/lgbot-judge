import log


def judge(message):
    log.logger().info(message)
    message.ack()
