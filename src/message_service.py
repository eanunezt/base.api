class MessageService:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def clear_messages(self):
        self.messages = []        

    def update_message(self, id, message):
        for i, msg in enumerate(self.messages):
            if msg.get("id") == id:
                self.messages[i] = message
                return True
        return False

