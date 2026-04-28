# Import libraries
# Import libraries
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect(id, name, price, purchase_date):
    conn = None
    try:
        conn = mydbconnection.connect(
            database='usersdb',   # ✅ Fix 1: 'dbase' → 'database'
            user='root',
            password='Kannada@2'
        )
        print('🎉 Connection Established')

        cursor = conn.cursor()
        myquery = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)"""

        record = (id, name, price, purchase_date)

        cursor.execute(myquery, record)
        conn.commit()
        print('✅ Records successfully added to Laptop table')

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('✅ Connection Closed')


# ✅ Fix 2: Moved outside the finally block — correct indentation
# ✅ Fix 3: Corrected the invalid date '202-01-01' → '2026-01-01'
if __name__ == '__main__':
    connect(23, 'MacBook Pro', 5000, '2026-01-01')
    connect(24, 'Chromebook',   500, '2026-01-01')
    
