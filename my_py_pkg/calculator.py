#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class CalculatorNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        #Create the subscriber (Data Type, Topic, Callback, Buffer) 
        self.counter_ = 0
        self.number_count_publisher_ = self.create_publisher(
            Int64,"number_count", 10)
        self.subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number, 10)
        self.reset_counter_service_ = self.create_service(
            SetBool, "reset_counter", self.callback_reset_counter)
        self.get_logger().info("Number Counter has been started.")

    #Create the callback for the subscriber 
    def callback_number(self, msg:Int64):
        self.counter_ += msg.data
        new_msg = Int64()
        new_msg.data = self.counter_
        self.number_count_publisher_.publish(new_msg)
        #self.get_logger().info(f"Received number {msg.data}")

    def callback_reset_counter(self, request: SetBool.Request, response: SetBool.Response):
        if request.data:
            self.counter_ = 0
            response.success = True
            response.message = "Counter has been reset"
        else:
            response.success = False
            response.message = "Counter has not been reset"
        return response
        


#class PublisherCalculatorNode(Node):
#    def __init__(self):
#        super().__init__("number_counter") # Node Name 
        # Create the publisher (Data Type, Topic Name, Lenght of the msg)
#        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
#        self.timer_ = self.create_timer(0.5, self.publish_news)
#        self.get_logger().info("Number Counter Calculator has been started.")

def main (args=None):
    rclpy.init(args=args)
    node = CalculatorNode()
#    node2 = PublisherCalculatorNode()
    rclpy.spin(node)
#    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
