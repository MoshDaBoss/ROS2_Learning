import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.message_count = 0
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        message = String()
        message.data = f'Hello World: {self.message_count}'
        self.publisher.publish(message)
        self.get_logger().info(f'Publishing: "{message.data}"')
        self.message_count += 1


def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()