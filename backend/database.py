'''
  database.py
  
  Module to connect to the Postgres database 
  using psycopg2-binary
'''
import getpass
import psycopg2

def get_db_connection(database, username, password, host='127.0.0.1', port=5432,
                      connect_timeout=10):
    connection = psycopg2.connect(user=username,
                                  password=password,
                                  host=host,
                                  port=int(port),
                                  database=database,
                                  connect_timeout=connect_timeout)
    connection.autocommit = True
    return connection

def query_user_for_superuser_credentials():
    username = input("Provide a Postgres role name with superuser privileges "
                     "in the configured cluster: ")
    password = getpass.getpass("Give the password: ")
    return username, password

def connect_as_user(db_name, host='127.0.0.1', port=5432):
    db_connection = None
    try:
        db_connection = psycopg2.connect(database=db_name)
        db_connection.autocommit = True
    except psycopg2.OperationalError:
        print("could not connect as local superuser with current user, credentials required")

    if not db_connection:
        superuser, password = query_user_for_superuser_credentials()
        db_connection = get_db_connection(db_name, superuser, password, host, port)

    if not db_connection or db_connection.closed:
        raise Exception("failed connecting the database: " + db_name)

    return db_connection

if __name__ == '__main__':
    conn = connect_as_user("albee")
    