import pickle
from reminderClass import Reminder


class ReminderTracker:
    reminders = []

    @classmethod
    def showReminders(cls):
        allReminders = cls.reminders 
        # print(allReminders)
        for elements in allReminders:
            allTags = elements.tags
            stringTags = ', '.join(allTags)
            print(f"ID: {elements.id} \nReminders: {elements.text} \nTags: {stringTags} \n")
        return allReminders

    @classmethod
    def searchReminders(cls, userInput):
        allReminders = cls.reminders
        result = []
        for item in allReminders:
            listData = userInput.replace(' ','')
            # print (listData)
            if(listData in item.text):
                result.append(item)
                continue
            for tag in item.tags:
                if(userInput in tag):
                    result.append(item)
                    break
        else:
            print("None found...")
        # print(itemsFound)
        for elements in result:
            allTags = elements.tags
            stringTags = ', '.join(allTags)
            print(f"ID: {elements.id} \nReminders: {elements.text} \nTags: {stringTags}")
        return result
            
    
    @classmethod
    def addReminder(cls, reminder):
        cls.reminders.append(reminder)
        print ("Reminder added!")
    

    @classmethod
    def modifyReminder(cls, reminder):
        # @property
        # def text(self):
        #     return self.text
    
        # @text.setter
        # def text(self, value):
        #     self.text = value

        # @property
        # def tags(self):
        #     return self.tags

        # @tags.setter
        # def tags(self, value):
        #     self.tags = value
        # allReminders = cls.reminders
        # if reminder =  
        allReminders = cls.reminders
        for element in allReminders:
            if element.id == reminder.id: 
                if (reminder.text == ""):
                    element.text = reminder.text
            else:
                element.text = reminder.text

            if (reminder.tags == ""):
                element.tags = reminder.tags
            else:
                element.tags= reminder.tags
           


    @classmethod
    def exportReminder(cls, fileName):
        allReminders = cls.showReminders()
        pickle_out = open(fileName + ".py", "wb")
        pickle.dump(allReminders, pickle_out)
        pickle_out.close()
        print(f"{fileName} exported successfully!")

    
    @classmethod
    def importReminder(cls, fileName):
        try:
            pickle_in = open(fileName, "rb")
            loadedFile = pickle.load(pickle_in)
            print(loadedFile)
        except:
            print("File not found.")





# deng = Reminder("hello my friend", ["world", "monkey", "cat", "dog"])
# jaime = ReminderTracker()
# jaime.addReminder(deng)
# jaime.showReminders()
# jaime.searchReminders("world jaime")
# jaime.modifyReminder(deng, "hi", "")
# jaime.showReminders()
# jaime.exportReminder("test")
# jaime.importReminder("test.py")
