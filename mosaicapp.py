import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="db_interview",
        user="postgres",
        password="crapcrap",
    )

def reset_db(conn):
    with conn.cursor() as cur:
        cur.execute("DROP SCHEMA public CASCADE")
        cur.execute("CREATE SCHEMA public")
    conn.commit()

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
    conn.commit()


# --- CRUD ---

def create_item(conn, name: str, description: str = None) -> dict:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "INSERT INTO items (name, description) VALUES (%s, %s) RETURNING *",
            (name, description),
        )
        conn.commit()
        return dict(cur.fetchone())


def get_all_items(conn) -> list[dict]:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM items ORDER BY id")
        return [dict(row) for row in cur.fetchall()]


def get_item(conn, item_id: int) -> dict | None:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM items WHERE id = %s", (item_id,))
        row = cur.fetchone()
        return dict(row) if row else None


def update_item(conn, item_id: int, name: str = None, description: str = None) -> dict | None:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            """
            UPDATE items
            SET name = COALESCE(%s, name),
                description = COALESCE(%s, description)
            WHERE id = %s
            RETURNING *
            """,
            (name, description, item_id),
        )
        conn.commit()
        row = cur.fetchone()
        return dict(row) if row else None


def delete_item(conn, item_id: int) -> bool:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM items WHERE id = %s RETURNING id", (item_id,))
        conn.commit()
        return cur.fetchone() is not None


# --- Main ---

def main():
    conn = get_connection()
    print("Connected to Postgres.")
    reset_db(conn)
    create_table(conn)
    print("Table ready.\n")

    # CREATE
    item = create_item(conn, "Hello", "First item")
    print(f"[CREATE] {item}")

    # READ (all)
    all_items = get_all_items(conn)
    print(f"[READ ALL] {all_items}")

    # READ (single)
    fetched = get_item(conn, item["id"])
    print(f"[READ ONE] {fetched}")

    # UPDATE
    updated = update_item(conn, item["id"], description="Updated description")
    print(f"[UPDATE] {updated}")

    # DELETE
    deleted = delete_item(conn, item["id"])
    print(f"[DELETE] id={item['id']} removed={deleted}")

    conn.close()


if __name__ == "__main__":
    main()