from collections import UserDict
from datetime import date, timedelta, datetime
from collections import defaultdict
import calendar

class Field:
    """
        Base class for field
    """
    def __init__(self, value):
        self._value = None
        
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
        
class Birthday(Field):
    
    """
        Birthday field
    """
    def __init__(self, date: date):
        """
            Constructor

            Args:
                date (date): birthday date
        """
       
        super().__init__(date)
    
        
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
        self.birthday = None
        self.phones = []

    def add_phone(self, phone: str):
        """
            Add phone to the record

            Args:
                phone (str): phone number
        """
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday: date):
        """
            Add birthday to the record

            Args:
                birthday (datetime): birthday
        """
        self.birthday = Birthday(birthday)

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


    def get_birthdays_per_week(self) -> None:
        """
            Based on input dictionary print peoples who's birthday is within next week

            Logic:
                In case today is Monday - we print all birthdays for next 7 days ignoring weekends
                
                In case today is not Monday - we print all birthdays for next 7 days moving weekend birthday to Monday

            Args:
                users (dictionary): Birthday catalog (name and date)
                
                    Format: 
                    
                    { "name": "<name>", "birthday": datetime() },
                    
                    Sample:
                    
                    { "name": "Bill Foolkland", "birthday": datetime(1955, 10, 28) },
            
            Output:
                Print in console who's birthday within this week
                
                Sample:
                    
                    Monday: Bob, Lily Gates, Lily Evans
                    Tuesday: Geremy Evans
                    Wednesday: Geremy Gates
                    Thursday: Karter Gates
                    Friday: Karter Gates
        """
        # const
        DAY_OF_WEEK_CODE_FRIDAY = 4
        DAY_OF_WEEK_CODE_MONDAY = 0

        today_date = datetime.today().date()
        
        is_monday = today_date.weekday()
        
        date_range_upper_limit = today_date + timedelta(days=7)
        
        birthdays_todo = defaultdict(list)

        for name, record in self.data.items():
            
            if name == "":
                print(f"Warning: name is empty. Birthday: {str(birthday)}")

            birthday = record.birthday.value
            
            birthday_this_year = birthday.replace(year=today_date.year)


            # case: today_date is monday
            # calculate all birthday up to Friday (ignore Sat,Sun)
            if is_monday and (today_date <= birthday_this_year 
                            and birthday_this_year < date_range_upper_limit):
                
                weekday_code = birthday_this_year.weekday()

                if weekday_code <= DAY_OF_WEEK_CODE_FRIDAY:
                    weekday_name = calendar.day_name[weekday_code]
                
                birthdays_todo[weekday_name].append(name)
            
            # case: today_date is not monday
            # calculate all birthday for 7 days (Sat,Sun move to monday)
            if (not is_monday) and (today_date <= birthday_this_year 
                                    and birthday_this_year < date_range_upper_limit):
                
                weekday_code = birthday_this_year.weekday()

                if weekday_code <= DAY_OF_WEEK_CODE_FRIDAY:
                    weekday_name = calendar.day_name[weekday_code]
                else:
                    # move birthday to Monday
                    weekday_name = calendar.day_name[DAY_OF_WEEK_CODE_MONDAY]
                
                birthdays_todo[weekday_name].append(name)

        # print results
        
        return birthdays_todo
