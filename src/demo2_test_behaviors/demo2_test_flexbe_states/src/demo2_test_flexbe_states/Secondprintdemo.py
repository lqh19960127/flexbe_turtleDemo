import rospy
from flexbe_core import EventState, Logger


class SecondPrintDemoState(EventState):  # 类名建议用 PascalCase（首字母大写）
    """
    Implements a state that can be used to print a message.

    -- printStr  str  Text to be printed.

    <= done           Indicates completion.
    """

    def __init__(self, printStr=""):
        super(SecondPrintDemoState, self).__init__(outcomes=['done'])
        self._str = printStr
        self.count=4
        
    def execute(self, userdata):      
        Logger.loginfo(f"Executing with message: {self._str}")  # 额外日志
        self.count-=1
        if self.count<0:
            return 'done'  # 直接返回 'done'，因为打印在 on_enter 中完成

    def on_enter(self, userdata):
        """Print the message when the state becomes active."""
        Logger.loginfo(self._str)  # 修正缩进：对齐方法内的其他语句

