#!/usr/bin/env python3

import pickle
import sys
from Note import Note


class App:
    FILE_LOCATION = "notes.pkl"

    def __init__(self):
        self.notes = []

    def add_note(self, note):
        note.id = len(self.notes)
        self.notes.append(note)

    def load(self):
        try:
            with open(self.FILE_LOCATION, "rb") as f:
                self.notes = pickle.load(f)
        except:
            self.notes = []

    def save(self):
        with open(self.FILE_LOCATION, "wb") as f:
            pickle.dump(self.notes, f)
        for note in self.notes:
            note.saved = True

    def __str__(self):
        return "\n".join([str(a) for a in self.notes if not a.deleted])

    def __iter__(self):
        return iter(self.notes)

    def __getitem__(self, i):
        return self.notes[i]


def main():
    print("note taker")
    app = App()
    app.load()

    while True:
        print("usage: note create")
        commands = input("?").split()

        if commands[0] == "create":
            text = input("Enter your note: ")
            n = Note(text)
            app.add_note(n)
        elif commands[0] == "exit":
            sys.exit()
        elif commands[0] == "list":
            print(app)
        elif commands[0] == "save":
            app.save()
        elif commands[0] == "delete":
            app[int(commands[1])].deleted = True
        elif commands[0] == "detail":
            app[int(commands[1])].print_detail()
        elif commands[0] == "append":
            app[int(commands[1])].append()


if __name__ == "__main__":
    main()
