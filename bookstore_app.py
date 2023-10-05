import datetime
import os
from abc import ABC, abstractmethod

#This is an abstract class.
#It contains abstract methods which act as placeholders for variables.
#Abstract methods allow us to call in 
class management_system(ABC): 
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def update(self):
        pass
        
class Events(management_system):
    events_list = [] #Create list to store all events.

    def __init__(self, event_ID, event_name, date, location):
        self.__event_ID = event_ID
        self.__event_name = event_name
        self.__date = date
        self.__location = location
        self.event_attendees_list = [] #List for when an attendee is added to an event.
        Events.events_list.append(self) #Each time a new attendee object is created, it automatically gets appended into a list.
    
    #After setting up each variable as a private attribute, we set up getters and setters.
    #This way, anyone can view and edit them.
    @property
    def get_event_id(self):
        return self.__event_id
    
    @get_event_id.setter
    def set_event_id(self,value):
        self.__event_id = value 
    
    @property
    def get_event_name(self):
        return self.__event_name
    
    @get_event_name.setter
    def set_event_name(self,value):
        self.__event_name = value
        
    @property
    def get_date(self):
        return self.__date
    
    @get_date.setter
    def set_date(self,value):
        self.__date = value
    
    @property
    def get_location(self):
        return self.__location
    
    @get_location.setter
    def set_location(self,value):
        self.__location = value
    
    def add_attendee(self, attendee):
        self.event_attendees_list.append(attendee) #A method that allows an attendee to be added to a specific event. Takes in attendee as an input.

    def event_attendees(self):
        for attendee in self.event_attendees_list: 
            print(f'Name: {attendee.name}') #Method to list out all names of attendees of each event.

    def __str__(self):
        return f'Event_ID: {self.event_ID}, Event: {self.event_name}, Date: {self.date}, Location: {self.location}' #After an object is created with this class, it can be printed in this format.

    def add(self): #This is inherited from the abstract class 'management_system'- we take in the abstract method 'add' and make our own function for adding attendees.
        while True:
            try: #Error handling applied here as the ID the user enters must be an integer or it'll show an error and will not proceed until the user enters an integer value.
                event_id_input = int(input("Please enter the event ID, this should be an integer value and must not be the same as another existing event: \n"))
                event_id = f'E{event_id_input}' #Take the input the user has entered and add an "E" to the start of it to show that it is an event.
                event_date = (input("Please enter the date of the event in format 'DD-MM-YY': \n")) #Event date should be entered in this specific format.
                date_obj = datetime.datetime.strptime(event_date, '%d-%m-%y').date() #Extract the day,month and year from the user's input.
                event_name = input("Please enter the event name: \n")
                event_location = input("Please enter the event location: \n")
                event_attendees[event_id] = []
                #Add all the events details to file 'Events.txt' line by line.
                with open('Events.txt', 'a') as file:
                    file.write(f'{event_id} {event_name} {date_obj} {event_location}') 
                    file.write('\n')
                with open('Events_attendees.txt', 'w') as text_file:
                    for key, value in event_attendees.items():
                        attendees_str = ' '.join(value)
                        text_file.write(f'{key} {attendees_str}\n')  # Update event_attendees file
                break #Break the 'while' loop once a valid value has been input.
            except ValueError: #If an input is invalid (ID not int), output error message.
                print('Invalid attendee ID.') #If an invalid ID or date value is entered by user, we get an error value and the user has to re-enter all the details.      

    def update(self): 
        delete_or_update = input("\nDelete an attendee: type 'd'\nUpdate an attendee: type 'u'\n")
        if delete_or_update == 'u': #Allows user to update an existing event.
            while True:
                try: 
                    update_event_ID = input("\nPlease enter the ID of the event you would like to update: ")
                    update_event_index = int(input("\nUpdate the event name: type '0'\nUpdate the date: type '1'\nUpdate the location: type '2'\n "))
                    update_to = input("\nPlease enter the value you you would like to change to: ")
                    
                    if (update_event_ID in events_dict) and (update_event_index<=2): #Using, error handling, we check to see if the ID the user entered is even in events_dict. 
                        events_dict[update_event_ID][update_event_index] = update_to #Update the events dictionary inputs the user provided.
                        print('\nUpdate successful.')
                        with open('Events.txt', 'w') as text_file:
                            for key, value in events_dict.items():
                                text_file.write(f'{key} {value[0]} {value[1]} {value[2]} \n') #Once the changes have been made, overwrite the text file with the changes.
                        break
                    else:
                        print("You have entered something invalid.") 
                except ValueError:
                    print("\nYou have entered something invalid.")
                    
        if delete_or_update == 'd': #Allows user to delete an existing event.
            while True:
                try:
                    delete_event_ID = input("\nPlease enter the ID of the event you would like to delete: ")
                    if (delete_event_ID in events_dict): 
                        del events_dict[delete_event_ID] #Delete the key (event_id) the user entered after checking if it exists in the events_dict.
                        del event_attendees[delete_event_ID] #If we delete an event, it automatically gets deleted from the events_attendees dictionary too.
                        print('\nDeletion successful.')
                        #Write the updated dictionaries to the relevant text files.
                        with open('Events.txt', 'w') as text_file:
                            for key, value in events_dict.items():
                                text_file.write(f'{key} {value[0]} {value[1]} {value[2]} \n')
                        with open('Events_attendees.txt', 'w') as text_file:
                            for key, value in event_attendees.items():
                                attendees_str = ' '.join(value)
                                text_file.write(f'{key} {attendees_str}\n')  # Update event_attendees file
                        break
                    else:
                        print("You have entered something invalid.")
                    
                except ValueError:
                    print("\nYou have entered something invalid.")

#--------------------------------------------------------------------------------------------------------------------------------------------

class Attendees(management_system):
    attendees_list = [] #Create list to store all attendees.

    def __init__(self, ID, name, age): #Initialise the name and age of each attendee.
        self.__ID = ID
        self.__name = name
        self.__age = age
        Attendees.attendees_list.append(self) #Each time a new attendee object is created, it automatically gets appended into a list.
    
    @property
    def get_id(self):
        return self.__ID
    
    @get_id.setter
    def set_id(self,value):
        self.__ID = value
        
    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def set_name(self,value):
        self.__name = value
        
    @property
    def get_age(self):
        return self.__age
    
    @get_age.setter
    def set_age(self,value):
        self.__age = value

    def __str__(self):
        #return f'Name: {self.name}, Age: {self.age}' #After an object is created with this class, it can be printed in this format.
        return f'{self.name} {self.age}'
    
    def add(self):
        while True:
            try:
                attendee_id_input = int(input("Please enter the attendee's id, this should be an integer value and must not be the same as another existing attendee: \n"))
                attendee_id = f'A{attendee_id_input}'
                attendee_name = input("Please enter the attendee's name: \n")
                attendee_age = int(input("Please enter the attendee's age: \n"))
                with open('Attendees.txt', 'a') as file:
                    file.write(f'{attendee_id} {attendee_name} {attendee_age}')
                    file.write('\n')
                break
            except ValueError:
                print('Attendee ID invalid. ')

    def update(self):
        delete_or_update = input("\nDelete an attendee: type 'd'\nUpdate an attendee: type 'u'\n")
        if delete_or_update == 'u':
            while True:
                try: 
                    update_attendee_ID = input("\nPlease enter the ID of the attendee you would like to update?: ")
                    update_attendee_index = int(input("\nPlease enter 0 to update the attendee's name or 1 to update their age: "))
                    update_to = input("\nPlease enter the value you you would like to change to: ")
                    
                    if (update_attendee_ID in attendees_dict) and (update_attendee_index<=1):
                        attendees_dict[update_attendee_ID][update_attendee_index] = update_to
                        print('\nUpdate successful.')
                        with open('Attendees.txt', 'w') as text_file:
                            for key, value in attendees_dict.items():
                                text_file.write(f'{key} {value[0]} {value[1]} \n')
                        break
                    else:
                        print("You have entered something invalid.")
                    
                except ValueError:
                    print("\nYou have entered something invalid.")
                    
        if delete_or_update == 'd':
            while True:
                try:
                    delete_attendee_ID = input("\nPlease enter the ID of the attendee you would like to delete?: ")
                
                    if (delete_attendee_ID in attendees_dict):
                        del attendees_dict[delete_attendee_ID]
                        for key in event_attendees:
                            event_attendees[key].remove(delete_attendee_ID)
                        print('\nDeletion successful.')
                        with open('Attendees.txt', 'w') as text_file:
                            for key, value in attendees_dict.items():
                                text_file.write(f'{key} {value[0]} {value[1]} \n')
                        with open('Events_attendees.txt', 'w') as text_file:
                            for key, value in event_attendees.items():
                                attendees_str = ' '.join(value)
                                text_file.write(f'{key} {attendees_str}\n')  # Update event_attendees file
                        break
                    else:
                        print("You have entered something invalid.")
                    
                except ValueError:
                    print("\nYou have entered something invalid.")

    def assign(self):
        event_attendees = {}
        for key,values in events_dict.items():
            event_attendees[key] = []

        with open('Events_attendees.txt', 'r') as file2:
            for line in file2:
                parts2 = line.strip().split()
                event_attendees[parts2[0]] = parts2[1:]
        print(" ")
        del_or_append = (input("Assign attendee to event: type 'a'\nDelete attendee from event: type 'd'\n"))
        print(" ")
        
        if del_or_append == 'a':
            while True:
                try:
                    assign_attendee = input("Please input the ID of the attendee you would like to assign: ")
                    assign_event = input("Please input the ID of the event you would like to assign the attendee to: ")

                    if assign_attendee in attendees_dict and assign_event in events_dict and assign_attendee not in event_attendees[assign_event]:
                        event_attendees[assign_event].append(assign_attendee)
                        with open('events_attendees.txt', 'w') as text_file:
                            for key, value in event_attendees.items():
                                attendees_str = ' '.join(value)
                                text_file.write(f'{key} {attendees_str}\n')
                            print('Written successfully')
                        break
                    else:
                        print('\nInvalid attendee or event has been entered.')
                except ValueError:
                    print("\nInvalid attendee or event has been entered.")

        if del_or_append == 'd':
            while True:
                try:
                    delete_attendee = input("please input the ID of the Attendee you would like to delete: ")
                    delete_from = input("please input the ID of the event you would like to delete from: ")                  
                    
                    if delete_attendee in attendees_dict and delete_from in events_dict:
                        event_attendees[delete_from].remove(delete_attendee)
                        with open('Events_attendees.txt', 'w') as text_file:
                            for key, value in event_attendees.items():
                                attendees_str = ' '.join(value)
                                text_file.write(f'{key} {attendees_str}\n')
                            print('Written successfully')
                        break
                    else:
                        print('\nInvalid attendee or event has been entered.')
                except ValueError:
                    print("\nInvalid attendee or event has been entered.")

#--------------------------------------------------------------------------------------------------------------------------------------------


if os.path.exists('Events.txt'):
    pass
else:
    with open('Events.txt','w') as file:
        pass

if os.path.exists('Attendees.txt'):
    pass
else:
    with open('Attendees.txt','w') as file:
        pass

if os.path.exists('Events_attendees.txt'):
    pass
else:
    with open('Events_attendees.txt','w') as file:
        pass       


while True: #At the beginning, and after each change is made, the program outputs all the up-to-date dictionaries and asks the user what changes they would like to make.
    #Set up the dictionaries that we are going to use.
    attendees_dict = {} 
    events_dict = {} 
    event_attendees = {} 

    with open('Events.txt', 'r') as file:
        for line in file: 
            #Open the files, read them in line-by-line and append them onto their relevent dictionaries with the specified keys are values.
            parts = line.strip().split()
            event_id, event_name, event_date, event_location = parts
            events_dict[event_id] = [event_name, event_date, event_location]

    with open('Attendees.txt', 'r') as file:
        for line in file:
            parts = line.strip().split()
            attendee_id, attendee_name, attendee_age = parts
            attendees_dict[attendee_id] = [attendee_name, (attendee_age)]

    with open('Events_attendees.txt', 'r') as file2:
        for line in file2:
            parts2 = line.strip().split()
            event_attendees[parts2[0]] = parts2[1:]

    print(" ")
    print("Up-to-date dictionary of attendees info:")
    print(attendees_dict) #Output the most-up-to date dictionaries at the start and each time after a change is made.
    print(" ")
    print("Up-to-date dictionary of events info:")
    print(events_dict)
    print(" ")
    print("Up-to-date dictionary of events and their attendees:")
    print(event_attendees)

    attendee_system = Attendees('ID','name','age') #Instantiation of the attendees and events classes.
    event_system = Events('ID','name','date','location')

    #Let the user pick what changes they would like to make to the system:
    choices = input("\nAppend a new attendees or event: type 1.\nUpdate or delete an event or attendee: type 2.\nAdd/remove attendee from event: type 3.\nQuit: type 4.\n")
    print(" ")
    
    if choices == '1':
        event_or_attendee = input("Add new attendee: type 'a'.\nAdd new event: type 'e'.\nContinue: type anything else.\n")
        print(" ")
        if event_or_attendee == 'a':
            attendee_system.add() #Apply the 'add' function from the attendee's class.

        if event_or_attendee == 'e':
            event_system.add()            

    if choices == '2':
        update_info = input("Delete or update attendee: type 'a'.\nDelete or update event: type 'e':\n")
        if update_info == 'a':
            attendee_system.update() 

        if update_info == 'e':
            event_system.update()

    if choices == '3':
            attendee_system.assign()

    if choices == '4': #The user is continuously given the options to make changes to the dictionary, until '4' is entered- the program ends.
        break
    
    

    



