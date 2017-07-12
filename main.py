import os

import datetime


DATA_FILENAME = os.path.dirname(__file__) + '/book.txt'


def load_data():
    if not os.path.exists(DATA_FILENAME) or os.stat(DATA_FILENAME).st_size == 0:
        with open(DATA_FILENAME, 'w') as new_data_file:
            new_data_file.write('[]')
    with open(DATA_FILENAME, 'r') as data_file:
        return eval(data_file.read())


def store_data(entries):
    with open(DATA_FILENAME, 'w') as data_file:
        print >>data_file, repr(entries)


class AddressBook(object):

    def __init__(self):
        self.notes = []
        self.read_notes()

    def read_notes(self):
        for note in load_data():
            self.notes.append(Note(note))

    def show_users(self):
        if len(self.notes) == 0:
            print u'Your adress book is empty :( '
        else:
            for key, note in enumerate(self.notes):
                print str(key) + ' ' + str(note)

    def add_user(self):
        new_note = Note()

    # def Reminder(self):
    #   now = datetime.now()
    #     datetime.strftime(datetime.now(), "%Y.%m.%d")

        while True:
            input_str = raw_input(u'Add a name\n')
            if input_str.isalpha() and len(input_str) < 10:
                new_note.name = input_str
                break
            else:
                print u'Make sure that you are using only letter and your Name length less that 10 digits'
        while True:
            input_str = raw_input(u'Add a surename\n')
            if input_str.isalpha() and len(input_str) < 15:
                new_note.surename = input_str
                break
            else:
                print u'Make sure that you are using only letter and your Surename length less that 10 digits'
        while True:
            input_str = raw_input(u'Add a phone number without +\n')
            if input_str.isdigit() and len(input_str) == 11:
                new_note.phone_number = input_str
                break
            else:
                print u'Make sure that you are using only digits and your phone number equals to 11'
        while True:
            input_str = raw_input(u'Add a birthday: YYYY.MM.DD:\n')
            try:
                input_str = input_str.split('.')
                date = datetime.date(int(input_str[0]), int(input_str[1]), int(input_str[2]))
                new_note.birth_date = str(date)
                break
            except:
                print u'Invalid Format!'
            # input_str = raw_input(u'Add a birthday\n')
            # if input_str.isdigit():
            #     self.BirthDate = input_str
            #     break
            # else: print (u'Use only digits please')
        print u'DONE'
        self.notes.append(new_note)
        store_data(self.notes)

    def delete_note(self, idx):
        try:
            del self.notes[int(idx)]
            store_data(self.notes)
        except:
            print u'There is no such contact!'


class Note(object):

    def __init__(self, initial=None):
        self.name = ''
        self.surename = ''
        self.phone_number = ''
        self.birth_date = ''

        if initial:
            self.name = initial['name']
            self.surename = initial['surename']
            self.phone_number = initial['phone_number']
            self.birth_date = initial['birth_date']

    def __str__(self):
        return 'Name: ' + self.name + ' |Surename: ' + self.surename + ' |Phone number: ' + self.phone_number + ' |Birth date: ' + self.birth_date

    def __repr__(self):
        return '{"name":"' + self.name +  '","surename":"' + self.surename + '","phone_number":"' + self.phone_number + '","birth_date":"' + self.birth_date + '"}'


if __name__ == '__main__':
    new_user = AddressBook()

    while True:
        print '''
Choose the option
1. Watch all contacts
2. Add a new user
3. Delete a user
4.Exit
        '''
        user_input = raw_input()
        if user_input == '1':
            new_user.show_users()
        elif user_input == '2':
            new_user.add_user()
            new_user.show_users()
        elif user_input == '3':
            new_user.show_users()
            new_user.delete_note(raw_input('Select a contact by a number\n'))
            # print ('Select a contact by a number\n')
            # if (raw_input()> u'0'):
            #     new_user.delete_note(raw_input)
            # else:
            #     print ("There is no such contact! Make sure you entered nonnegative number\n") # Exclude the possibility of deleting from the list by reverse idx
            new_user.show_users()
        elif user_input == '4':
            break
        else:
            print '---ENTER CORRECT COMMAND--'