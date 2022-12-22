
class MessageQueue:

    def __init__(self, message_queue="redis://localhost:6379/0"):

        self.message_queue = message_queue
