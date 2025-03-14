import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import logging

# Define the TemperatureLogger node
class TemperatureLogger(Node):
    def __init__(self, file: str):
        super().__init__('temperature_logger')
        self.subcriber = self.create_subscription(Float32, '/temperature', self.callback, 10)
        self.file_name = file
        self.logger  = self.get_logger()
        logging.basicConfig(
            filename='temperature_log.txt',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )


    def callback(self, msg: Float32):
        if msg.data > 50.0:
            self.logger.info('Publishing temperature: %.2f' % msg.data)
            logging.info('Publishing temperature: %.2f' % msg.data)
    

def main(args=None):
    rclpy.init(args=args)

    logger = TemperatureLogger("log.txt")

    rclpy.spin(logger)

    logger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
