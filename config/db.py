
import os

import mysql.connector


def get_connection():
    password = os.getenv("DB_PASSWORD")
    if not password:
        raise ValueError(
            "DB_PASSWORD is not set. "
            "Set it in the environment before running the application."
        )

    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=password,
        database=os.getenv("DB_NAME", "employee_db"),
    )


if __name__ == "__main__":
    try:
        conn = get_connection()
        if conn.is_connected():
            print("MySQL Database Connected Successfully!")
        conn.close()
    except (mysql.connector.Error, ValueError) as error:
        print("Database Connection Failed:", error)
