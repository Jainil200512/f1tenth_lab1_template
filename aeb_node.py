import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped

class AEBNode(Node):
    def __init__(self):
        super().__init__('aeb_node')
        self.subscriber = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.publisher = self.create_publisher(AckermannDriveStamped, '/drive', 10)
        
        # Define safe distance thresholds (in meters)
        self.front_threshold = 1.0   # Front wall distance
        self.side_threshold = 0.5     # Side wall distance

    def scan_callback(self, msg):
        # Assuming msg.ranges contains distance readings
        # The LaserScan data format may vary; adjust indices as needed
        front_distance = min(msg.ranges[0:30] + msg.ranges[330:360])  # Front (forward direction)
        left_distance = min(msg.ranges[60:120])  # Left side
        right_distance = min(msg.ranges[240:300])  # Right side

        if front_distance < self.front_threshold or left_distance < self.side_threshold or right_distance < self.side_threshold:
            self.trigger_braking()

    def trigger_braking(self):
        # Create a braking command
        brake_cmd = AckermannDriveStamped()
        brake_cmd.drive.speed = 0.0  # Stop the vehicle
        self.publisher.publish(brake_cmd)
        self.get_logger().info('Emergency braking activated!')

def main(args=None):
    rclpy.init(args=args)
    aeb_node = AEBNode()
    rclpy.spin(aeb_node)
    aeb_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

