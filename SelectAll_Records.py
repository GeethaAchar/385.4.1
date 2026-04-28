# Import libraries
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:
        # Establish connection
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='Kannada@2'
        )
        print('🎉 Succesfull Connection to SQL DB')

        query = 'SELECT * FROM laptop'
      
        # Excute Query
        cursor = conn.cursor()
        cursor.execute(query)

        records = cursor.fetchall()

        for line in records:
            print(line)
        
    except Error as e:
        print(f'❌ Error: {e}')
    
    finally:
        # Close connections
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 SQL DB connection closed')
            


if __name__ == '__main__':
    connect()