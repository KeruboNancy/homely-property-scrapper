import mysql.connector
from mysql.connector import Error
from typing import List, Dict


class HomelyEngine:
    """
    Architectural Engine: ETL (Extract, Transform, Load) 
    Process for Real Estate Data Strata.
    """

    def __init__(self):
        # Configuration - Update these from your LocalWP 'Database' tab
        self.config = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'root',
            'database': 'local',
            'port': '10011'  # <--- Ensure this matches LocalWP exactly
        }
        self.listings: List[Dict] = []

    def extract_data(self):
        """Simulates data extraction from digital sources."""
        print("🔍 Scanning Digital Strata...")
        self.listings = [
            {'title': 'Luxury Gold Villa', 'price': 45000000,
                'loc': 'Karen', 'beds': 5},
            {'title': 'Modern Black Suite', 'price': 12500000,
                'loc': 'Westlands', 'beds': 2},
            {'title': 'Sunset Penthouse', 'price': 30000000,
                'loc': 'Kilimani', 'beds': 3},
        ]

    def load_to_sql(self):
        """Hydrates the SQL database with extracted listings."""
        conn = None
        try:
            conn = mysql.connector.connect(**self.config)
            if conn.is_connected():
                with conn.cursor() as cursor:
                    # 1. Initialize Schema
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS wp_property_listings (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            title VARCHAR(255) NOT NULL,
                            price DECIMAL(15, 2),
                            location VARCHAR(100),
                            beds INT,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)

                    # 2. Batch Injection
                    sql = "INSERT INTO wp_property_listings (title, price, location, beds) VALUES (%s, %s, %s, %s)"
                    params = [(l['title'], l['price'], l['loc'], l['beds'])
                              for l in self.listings]

                    cursor.executemany(sql, params)
                    conn.commit()

                    print(
                        f"✅ SUCCESS: {cursor.rowcount} records injected into SQL Strata.")

        except Error as e:
            print(f"❌ DATABASE ERROR: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()
                print("🔌 Connection securely closed.")


if __name__ == "__main__":
    engine = HomelyEngine()
    engine.extract_data()
    engine.load_to_sql()
