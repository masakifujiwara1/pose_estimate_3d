#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(msg):
    goal_radius = rospy.get_param('/waypoint_manager/waypoint_visualization/set_goal_radius', 0.0)

    pose_with_z = PoseWithCovarianceStamped()
    pose_with_z.header = msg.header
    pose_with_z.pose.pose.position.x = msg.pose.pose.position.x
    pose_with_z.pose.pose.position.y = msg.pose.pose.position.y
    pose_with_z.pose.pose.position.z = goal_radius

    pose_with_z.pose.pose.orientation = msg.pose.pose.orientation

    pose_with_z.pose.covariance = msg.pose.covariance

    pub.publish(pose_with_z)
    rospy.loginfo("Published modified initialpose with z={}".format(goal_radius))

def main():
    global pub
    rospy.init_node('pose_estimate_3d_node')

    rospy.Subscriber('initialpose_2d', PoseWithCovarianceStamped, callback)
    
    pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped, queue_size=10)

    rospy.loginfo("Pose Modifier Node Started")
    rospy.spin()

if __name__ == '__main__':
    main()
