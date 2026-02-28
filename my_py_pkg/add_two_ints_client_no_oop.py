#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

#Remove the class

def main(args=None):
    #Initialize ROS2 communications
    rclpy.init(args=args)
    #Create the node 
    node = Node("add_two_ints_client_no_oop")

    #Create the client
    client = node.create_client(AddTwoInts, "add_two_ints")
    #Wait for the service to be up 
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for Add Two Ints server...")
    
    # Create the request to the server
    request = AddTwoInts.Request()
    request.a = 3
    request.b = 8 

    #Send the request obtained
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)

    #Print the response
    response = future.result()
    node.get_logger().info(str(request.a) + " + " + 
                           str(request.b) + " = " +
                           str(response.sum))

    #ShutDown ROS2 communication
    rclpy.shutdown()


if __name__ == "__main__":
    main()