from reminderClass import Reminder
from reminderTrackerClass import ReminderTracker


ReminderTracker = ReminderTracker()

while True:
    userInput = input("""
    Reminders Menu: \n
    1. show all reminders
    2. search reminders
    3. add reminders
    4. modify reminders
    5. export reminders
    6. import reminders
    7. quit \n
enter an option: """)

    if userInput == "1":
        ReminderTracker.showReminders()
        userInput

    elif userInput == "2":
        searchInput = input("search for: ")
        ReminderTracker.searchReminders(searchInput)
        userInput

    elif userInput == "3":
        newReminder = input("enter a reminder: ")
        if (newReminder == ""):
            print("returning to menu...")
        newTags = input("enter tags, comma seperated if multiple: ")
        listedNewTags = newTags.replace(","," ").split()
        # print (listedNewTags)
        reminder = Reminder(newReminder, listedNewTags)
        ReminderTracker.addReminder(reminder)
        userInput

    elif userInput == "4":
        allReminders = ReminderTracker.showReminders()
        reminderID= str(input("enter id of reminder you wish to edit: "))
        textValue = input("enter modified reminder: ")
        tagsValue = input("enter modified tags: ")
        listTagsValue = tagsValue.replace(",", " ").split()
        modified = Reminder(textValue, listTagsValue)
        modified.id = reminderID
        ReminderTracker.modifyReminder(modified)
    
        userInput

    elif userInput == "5":
        fileName = input("enter a name for the file: ")
        ReminderTracker.exportReminder(fileName)

        userInput
    elif userInput == "6":
        fileName = input("enter the name of the file you want to open: ")
        ReminderTracker.importReminder(fileName)
        userInput
    elif userInput == "7":
        print("Goodbye")
        break
    else:
        print('choose an option between 1 to 7')
