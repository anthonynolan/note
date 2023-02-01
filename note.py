#!/usr/bin/env python3

import pickle
import sys
from datetime import datetime

class App:
    FILE_LOCATION = 'notes.pkl'

    def __init__(self):
        self.notes = []
    def add_note(self, note):
        note.id = len(self.notes)
        self.notes.append(note)
    def load(self):
        try:
            with open(self.FILE_LOCATION, 'rb') as f:
                self.notes = pickle.load(f)
        except:
            self.notes = []
    def save(self):
        with open(self.FILE_LOCATION, 'wb') as f:
            pickle.dump(self.notes, f)
    def __str__(self):
        return '\n'.join([str(a) for a in self.notes if not a.deleted])
    def __iter__(self):
        return iter(self.notes)
    def __getitem__(self, i):
        return self.notes[i]


def get_now():
    return datetime.now().strftime('%a %b %-d %Y %-H:%M')


class Note():
    def __init__(self, text=None):
        self.text = text
        self.dt = get_now()
        self.id = 0
        self.deleted = False
    def __repr__(self):
        return f'#{self.id}. {self.dt}, {self.text}, {self.deleted}'

    def __str__(self):
        return f'#{self.id}. {self.dt}, {self.text}'

    def print_detail(self):
        print(f'Id: {self.id}\nDate: {self.dt}\n{self.text}')
    def __setstate__(self, state):
        new_fields = {'deleted': False}
        for k, v in new_fields.items():
            try:
                state[k]
            except:
                state[k]=v
        self.__dict__.update(state)
    def append(self):
        additional_text = input("Enter additional text: \n")
        self.text+=f'({get_now()}) {additional_text}'

def main():
    print('note taker')
    app = App()
    app.load()

    while True:
        print('usage: note create')
        commands = input('?').split()
        
        if commands[0]=='create':
            text = input('Enter your note: ')
            n = Note(text)
            app.add_note(n)
        elif commands[0]=='exit':
            sys.exit()
        elif commands[0]=='list':
            print(app)
        elif commands[0]=='save':
            app.save()
        elif commands[0]=='delete':
            app[int(commands[1])].deleted = True
        elif commands[0]=='detail':
            app[int(commands[1])].print_detail()
        elif commands[0]=='append':
            app[int(commands[1])].append()


if __name__=='__main__':
    main()
