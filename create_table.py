import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:
        # Establish a connection
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='Kannada@2'
        )
        print('🎉 Connection Established')

        # Cursor objects allow us to perform SQL operations
        cursor = conn.cursor()

        # Perform SQL Operations
        # create a query to use
        myquery2 = "CREATE TABLE `laptop` (`Id` int(11) NOT NULL,\
            `Name` varchar(250) NOT NULL,\
            `Price` float NOT NULL,\
            `Purchase_date` date NOT NULL)"
        
        #Execute query with the cursor.execute() function
        cursor.execute(myquery2)
        print('✅ Table Creation Success')

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn.is_connected():
            conn.close()
            print('🛑 Connection Closed')


if __name__ == '__main__':
    connect()