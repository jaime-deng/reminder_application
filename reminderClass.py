class Reminder:
    reminderCounter = 0
    def __init__(self, text, tags = []):
        self.text = text
        self.tags = tags
        self.id = id(self)
        # self.id = Reminder.reminderCounter + 1
        # Reminder.reminderCounter += 1


 