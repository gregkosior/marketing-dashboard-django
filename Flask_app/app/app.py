from flask import Flask, jsonify, render_template, send_from_directory
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "database.db"

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/summary")
def summary():
    conn = get_db_connection()
    row = conn.execute("""
        SELECT
            SUM(cost) AS total_cost,
            SUM(revenue) AS total_revenue,
            SUM(pandl) AS total_pandl
        FROM shop_data
    """).fetchone()
    conn.close()
    return jsonify(dict(row))

@app.route("/api/group")
def group():
    conn = get_db_connection()
    rows = conn.execute("""
        SELECT
            ad_group,
            SUM(pandl) AS total_pandl
        FROM shop_data
        GROUP BY ad_group
        ORDER BY total_pandl DESC
    """).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        str(app.static_folder),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

if __name__ == "__main__":
    app.run(debug=True)
