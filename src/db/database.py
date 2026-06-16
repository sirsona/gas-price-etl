import psycopg2
from dotenv import load_dotenv

from config.settings import settings

load_dotenv()


def get_connections():
    return psycopg2.connect(
        host=settings.db_host,
        port=settings.db_port,
        dbname=settings.db_name,
        user=settings.db_user,
        password=settings.db_password,
    )
