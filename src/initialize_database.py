from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa kaikki tietokantataulut.

    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists reservations;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo kaikki tietokantataulut.

    Args:
        connection: Tietokantayhteyden Connection-olio
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text,
            admin boolean
        );
    ''')

    cursor.execute('''
        CREATE TABLE reservations ( 
            id integer primary key,
            username text,
            date text,
            hour integer, 
            FOREIGN KEY(username) REFERENCES users(username)   
        );
    ''')

    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut."""
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
