from collections import UserDict

class Record:
    """
        Class represent address book record
        
        Attributes
        ----------
        name : str
            Name of the address book record
        phones : str
            List of the phones
    """

    def __init__(self, name: str):
        """
            Constructor of class

            Args:
                name (str): name of the record
        """
        
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        """
            Add phone to the record

            Args:
                phone (str): phone number
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
            Remove phone number from the record

            Args:
                phone (str): phone number
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str):
        """
            Change phone number

            Args:
                old_phone (str): Old phone number
                new_phone (str): New phone number
        """
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone: str) -> str:
        """
            Search by phone number

            Args:
                phone (str): phone number

            Returns:
                str: phone number
        """
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self) -> str:
        """
            String representation of record

            Returns:
                str: String
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    """
        Class address book to store Records

        Args:
            UserDict ([Records]): records
    """
    def add_record(self, record: Record):
        """
            Add record to address book

            Args:
                record (Record): record to add
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        """
            Search record in address book by name

            Args:
                name (str): name

            Returns:
                Record: record by name
        """
        return self.data.get(name)

    def delete(self, name: str):
        """
            Delete record by name

            Args:
                name (str): name of record
        """
        if name in self.data:
            del self.data[name]


class Field:
    """
        Base class for field
    """
    def __init__(self, value):
        self._value = value


    def __str__(self):
        return str(self._value)
    
    @property
    def value(self) -> str:
        return self._value

               
class Name(Field):
    """
        Represent name field
    """
    def __init__(self, name: str):
        """
            Constructor

            Args:
                name (str): name

            Raises:
                ValueError: Name cannot be empty
        """
        if not name or len(name) == 0:
            raise ValueError("Name cannot be empty")
        
        super().__init__(name)

class Phone(Field):
    
    """
        Phone field
    """
    def __init__(self, phone: str):
        """
            Constructor

            Args:
                phone (str): phone number
        """
       
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number format. It should contain 10 digits.")
        super().__init__(phone)
    
    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, value: str):
        """
            Value property setter 

            Args:
                input_value (str): phone number

            Raises:
                ValueError: Invalid phone number format. It should contain 10 digits.
        """
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format. It should contain 10 digits.")
        self._value = value