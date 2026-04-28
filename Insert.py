# Import libraries
import mysql.connector as mydbconnection
from mysql.connector import Error

def connection():
    conn = None

    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='Kannada@2'
        )
        print('🎉 Connection Established')

        cursor = conn.cursor()

        myquery = "INSERT INTO `laptop` (`Id`, `Name`, `Price`, `Purchase_date`) VALUES (%s, %s, %s, %s)"

        # ✅ Better approach — use executemany() instead of 6 separate execute() calls
        records = [
            (1, 'Dell',    50000, '2022-01-01'),
            (2, 'Lenovo',  60000, '2022-02-01'),
            (3, 'Asus',    70000, '2022-03-01'),
            (4, 'HP',      80000, '2022-04-01'),
            (5, 'Acer',    90000, '2022-05-01'),
            (6, 'Macbook', 100000, '2022-06-01'),
        ]

        cursor.executemany(myquery, records)

        conn.commit()  
        print('✅ Insertion Success')

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('✅ Connection Closed')


if __name__ == '__main__':
    connection()