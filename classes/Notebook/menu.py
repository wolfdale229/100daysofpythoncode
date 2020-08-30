import sys
from typing import List
from notebook import Note, NoteBook

class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        print(
            """
            Notebook Menu

            1. Show all Notes
            2. Search Notes
            3. Add Note
            4. Modify Note
            5. Quit
              """)

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else :
                print(f'{choice} is not a valid option')

    def show_notes(self, notes=None)-> List:
        """displays all the notes in the notebook"""
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f'{note.id}: {note.tags}\n{note.memo}')

    def search_notes(self):
        """search for a note in the notebook"""
        filter = str(input('search for:'))
        note = self.notebook.search(filter)
        self.show_notes(note)

    def add_note(self):
        """Add a new note"""
        memo = str(input('Enter a memo:'))
        tags = str(input('Enter a tag:'))
        self.notebook.new_note(memo, tags)
        print('You have added a new note')

    def modify_note(self):
        """Modify an existing note"""
        id = input('Enter a note id:')
        memo = str(input('Enter a memo:'))
        tags = str(input('Enter a tag:'))
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print('Thank you for using the notebook today')
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()
