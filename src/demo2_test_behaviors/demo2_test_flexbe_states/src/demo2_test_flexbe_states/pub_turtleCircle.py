import rospy
from geometry_msgs.msg import Twist
from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher


class PubTurtleCircleState(EventState):  # 类名建议用 PascalCase（首字母大写）
    """
    Implements a state that can be used to print a message.

    -- printStr  str  Text to be printed.

    <= done           Indicates completion.
    """

    def __init__(self, topic=""):
        super(PubTurtleCircleState, self).__init__(outcomes=['done'])
        self._topic = topic
        self.count=20
        self._publisher=ProxyPublisher({self._topic:Twist})
        self.twistData=Twist()
        self.twistData.angular.y=0
        self.twistData.angular.z=0.5
        self.twistData.angular.x=0
        self.twistData.linear.x=1.0
        self.twistData.linear.y=0
        self.twistData.linear.z=0
        
    def execute(self, userdata):             
        self.count-=1
        self._publisher.publish(self._topic,self.twistData)
        if self.count<0:
            return 'done'  # 直接返回 'done'，因为打印在 on_enter 中完成

    def on_enter(self, userdata):
        """Print the message when the state becomes active."""
        Logger.loginfo("task start!")  # 修正缩进：对齐方法内的其他语句