"""Creating a contact class"""
class ContactList(list):
    def search(self, name):
        """Return all contact that have the search value 
        in their name """
        matching_contact = []
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact


class Contacts():
    """Making a contact application"""
    all_contacts = []

    def __init__(self, name, email):
        """Initailizing the contact"""
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)


class Supplier(Contacts):
    def order(self, order):
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )
