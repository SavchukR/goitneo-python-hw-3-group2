from task_2 import *

def main():
    """
        Run test on address book classes
    """

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    
    # More tests
    
    # remove phone
    john = book.find("John")

    print(john)

    john.remove_phone("1112223333")

    print(john)
    
    # get non existing contact
    NonExistingContact = book.find("NonExistingContact")
    
    print(NonExistingContact)
    
    # try add non-valid phone
    try:
        john.add_phone("abc")
    except Exception as ex:
        print(ex)
        
    # try add non-valid phone (length is 10)
    try:
        john.add_phone("123A567890")
    except Exception as ex:
        print(ex)
        
    # try add empty name
    try:
        book.add_record(Record(""))
    except Exception as ex:
        print(ex)
        
    # try add None name
    try:
        book.add_record(Record(None))
    except Exception as ex:
        print(ex)
        
    # try change phone to invalid
    
    john = book.find("John")
    
    try:
        john.edit_phone("5555555555", "bob")
    except Exception as ex:
        print(ex)
        
if __name__ == "__main__":
    main()
