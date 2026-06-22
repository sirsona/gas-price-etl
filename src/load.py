from dotenv import load_dotenv

from db.database import get_connections

load_dotenv()


def load(state, cities):
    # database
    conn = get_connections()
    # execute
    cursor = conn.cursor()

    cursor.execute(
        """
                INSERT INTO states
                (name, gasoline, "midGrade", premium, diesel)
                VALUES (%s, %s, %s, %s, %s)
            """,
        (
            state["name"],
            state["gasoline"],
            state["midGrade"],
            state["premium"],
            state["diesel"],
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
                city["name"],
                city["currency"],
                city["gasoline"],
                city["midGrade"],
                city["premium"],
                city["diesel"],
            ),
        )

    conn.commit()
    conn.close()

    print("Data loaded successfully")
