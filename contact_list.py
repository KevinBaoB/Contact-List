from re import M


class ContactList():


    def __init__(self, list_name, list_actual):
        self.list_name = list_name
        self.list_actual = list_actual
        
    @property
    def contacts(self):
        print("Your contacts are: ")
        return self.list_actual

    def add_contacts(self, person, info):
        self.person = person
        self.list_actual.append({'name':person,'number':info})

    def delete_contact(self, person):
        self.person = person
        for i in range(len(self.list_actual)):
            # print(person)
            # print(self.list_actual[i]['name'] == person)
            if self.list_actual[i]['name'] == person: 
                del self.list_actual[i]

    def find_shared_contacts(self, compared_list):
        self.compared_list = compared_list
        for i in self.list_actual:
            for j in compared_list.contacts:
                if( i == j):
                    return i
        

            


friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]

work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)

print(friends_i_work_with)

# my_friends_list.add_contacts('Kevin', '409-567-9871')
# print(my_friends_list.contacts)
# my_friends_list.delete_contact('Kevin')
# print(my_friends_list.contacts)

