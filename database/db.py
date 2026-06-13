import sqlite3

DB_PATH = "data/jobs.db"

def init_db():

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id TEXT UNIQUE,
        title TEXT,
        link TEXT UNIQUE,
        source TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS skipped (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def job_exists(link):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM jobs WHERE link=?",
        (link,)
    )

    result = cur.fetchone()

    conn.close()

    return result is not None


def save_job(job_id, title, link, source):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO jobs
        (job_id, title, link, source)
        VALUES (?, ?, ?, ?)
    """, (job_id, title, link, source))

    conn.commit()
    conn.close()

def save_favorite(job_id):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO favorites (job_id)
        VALUES (?)
    """, (job_id,))

    conn.commit()
    conn.close()

def save_skipped(job_id):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO skipped (job_id)
        VALUES (?)
    """, (job_id,))

    conn.commit()
    conn.close()

def is_skipped(job_id):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM skipped WHERE job_id=?",
        (job_id,)
    )

    result = cur.fetchone()

    conn.close()

    return result is not None

def get_favorites():

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT job_id FROM favorites
    """)

    rows = cur.fetchall()

    conn.close()

    return [r[0] for r in rows]

def get_job_by_id(job_id):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT title, link, source
        FROM jobs
        WHERE job_id=?
    """, (job_id,))

    row = cur.fetchone()

    conn.close()

    return row


def remove_favorite(job_id):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM favorites WHERE job_id=?", (job_id,))
    print("BEFORE DELETE:", cur.fetchone())

    cur.execute("DELETE FROM favorites WHERE job_id=?", (job_id,))

    conn.commit()

    cur.execute("SELECT * FROM favorites WHERE job_id=?", (job_id,))
    print("AFTER DELETE:", cur.fetchone())

    conn.close()