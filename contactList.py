class ContactList:

    def __init__(self, groupName, contactList):
        self.groupName = groupName
        self.contactList = contactList

    def add_contact(self, contact):
        self.contactList.append(contact)
        self.contactList.sort()

    def remove_contact(self, nameToRemove):
        try:
            for i in range(len(self.contactList)): 
                if self.contactList[i]['name'] == nameToRemove:
                    indexToRemove = i
            self.contactList.pop(indexToRemove)
        except:
            print("error")

    def find_shared_contacts(self, ContactList):
        contactList2 = []
        list1 = self.contactList
        list2 = ContactList.contactList
        for i in list1:
            if i in list2:
                contactList2.append(i)

        return contactList2


    
    

    

                
friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

cl1 = ContactList('My Friends', friends)
cl2 = ContactList('Work Buddies', work_buddies)
cl1.add_contact({'name': 'Cassie', 'number': '1234'})
cl2.add_contact({'name': 'Brian', 'number': '5678'})
cl1.remove_contact('Cassie')
print(cl1.groupName, cl1.contactList)
print(cl2.groupName, cl2.contactList)
friends_i_work_with = cl1.find_shared_contacts(cl2)
print(friends_i_work_with)