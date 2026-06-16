from db.database import get_connections
from dotenv import load_dotenv

load_dotenv()

# DB_PORT = os.getenv("PORT")
# DB_HOST = os.getenv("DB_HOST")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
#
# # Print to see what's loaded
# print("DB_HOST:", DB_HOST)
# print("DB_PORT:", DB_PORT)
# print("DB_NAME:", DB_NAME)
# print("DB_USER:", DB_USER)
# print("DB_PASSWORD:", DB_PASSWORD)
#


def load(state, cities):
    # database
    conn = get_connections()
    # # execute
    cursor = conn.cursor()

    cursor.execute(
        """
                INSERT INTO states
                (name, gasoline, "midGrade", premium, diesel)
                VALUES (%s, %s, %s, %s, %s)
            """,
        (
            state.name,
            state.gasoline,
            state.midGrade,
            state.premium,
            state.diesel,
        ),
    )

    for city in cities:
        cursor.execute(
            """
                INSERT INTO cities 
                (name, currency,gasoline, "midGrade", premium, diesel)
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                city.name,
                city.currency,
                city.gasoline,
                city.midGrade,
                city.premium,
                city.diesel,
            ),
        )

    conn.commit()
    conn.close()

    print("Data loaded successfully")
