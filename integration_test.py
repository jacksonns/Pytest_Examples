import pytest
import sqlite3

@pytest.fixture
def session(): 
    connection = sqlite3.connect(':memory:')
    db_session = connection.cursor()
    yield db_session
    connection.close()

@pytest.fixture
def setup_db(session): 
    session.execute('''CREATE TABLE numbers (number int, existing boolean)''')
    session.execute('INSERT INTO numbers VALUES (10, 1)')
    session.connection.commit()


@pytest.mark.usefixtures("setup_db")  # Execute setup_db fixture, could be passed as an argument
def test_get(session):
    existing = session.execute('SELECT existing FROM numbers WHERE number == 10')
    assert existing.fetchone()[0]