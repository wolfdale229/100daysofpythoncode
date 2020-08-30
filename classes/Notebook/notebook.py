import datetime
from typing import Any, List

#Store the next available id for all new notes
last_id = 0

class Note():
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note."""

    def __init__(self, memo, tags=''):
        """initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter:Any)->bool:
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags."""
        return filter in self.memo or filter in self.tags

class NoteBook():
    """Represents a collection of notes that can be tagged, searched and modified"""

    def __init__(self):
        """Initialize a notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags="")-> Note:
        """ Make  a new note and append to the list of notes"""
        self.notes.append(Note(memo, tags)) # makes a new note by appending the Note class

    def _find_note(self, note_id:int)-> Note:
        """Locate the note with the given id, else return None."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id:int, memo:str)->bool:
        """Modify the memo of a existing note using it's id"""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id:int, tags:str)-> None:
        """modify the tag of an existing note by searching
         through the notes for a matching id"""
        for note in self.notes:
            self._find_note(note_id).tags = tags

    def search(self, filter:str)-> List[str]:
        """Find all notes that match the given filter"""
        return [note for note in self.notes if note.match(filter)]










































