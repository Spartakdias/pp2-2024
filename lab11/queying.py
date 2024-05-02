import psycopg2
from config import load_config

def get_contacts_by_name(first_name, limit, offset):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "SELECT * FROM contacts WHERE first_name = %s LIMIT %s OFFSET %s"
        cur.execute(query, (first_name, limit, offset))
        
        contacts = cur.fetchall()
        
        return contacts
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error fetching contacts by name:", error)
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def get_contacts_by_phone(phone_number, limit, offset):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "SELECT * FROM contacts WHERE phone_number = %s LIMIT %s OFFSET %s"
        cur.execute(query, (phone_number, limit, offset))
        
        contacts = cur.fetchall()
        
        return contacts
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error fetching contacts by phone number:", error)
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
name_found = input("Enter name that you need: ")
number_found = input("Enter number that you need: ")
limit = int(input("Enter limit: "))
offset = int(input("Enter offset: "))

if __name__ == '__main__':
    # Example usage: get contacts with a specific first name
    contacts_with_name = get_contacts_by_name(name_found, limit, offset)
    if contacts_with_name:
        print(f"Contacts with name {name_found}:", contacts_with_name)
    else:
        print(f"No contacts found with name {name_found}.")

    # Example usage: get contacts with a specific phone number
    contacts_with_phone = get_contacts_by_phone(number_found, limit, offset)
    if contacts_with_phone:
        print(f"Contacts with phone number {number_found} :", contacts_with_phone)
    else:
        print(f"No contacts found with phone number {number_found}.")
