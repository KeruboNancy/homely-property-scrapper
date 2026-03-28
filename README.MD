# Homely Digital Strata: Automated SQL Hydration Engine 🐍🏗️

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

This is a **portable Python utility** designed to automate the extraction and injection of real estate data into any WordPress-based SQL environment.

Instead of manual entry, this engine provides a structured **ETL (Extract, Transform, Load)** pipeline that architects can integrate into their existing digital ecosystems to manage large-scale property datasets.

---

## 💎 Why Use This Engine?

If you are managing high volumes of data (e.g., **17,000+ listings**), manual WordPress entry is not an option. This engine treats data as "strata"—layers of information that must be precision-deposited into a database.

### Core Capabilities:

- **Modular Integration:** Drop this script into any project to handle data migration.
- **Automated Schema Creation:** Automatically builds the `wp_property_listings` table in your target SQL database.
- **High-Speed Hydration:** Uses batch processing (`executemany`) to populate thousands of rows in seconds.
- **Scientific Precision:** Built with strict data typing for currency and location metadata.

---

## 🚀 How to Integrate This Into Your Project

This engine is designed to be a **standalone tool**. You do not need to clone a specific site to use it; you simply need a running MySQL/MariaDB instance.

### 1. Requirements

- Python 3.x
- A target MySQL Database (LocalWP, XAMPP, or Live Server)
- `mysql-connector-python` library

### 2. Setup

1.  **Clone this Utility:**
    ```bash
    git clone [https://github.com/KeruboNancy/homely-property-scrapper.git](https://github.com/KeruboNancy/homely-property-scrapper.git)
    ```
2.  **Configure your Handshake:**
    Open `engine.py` and update the `self.config` dictionary with your specific site's database credentials:
    ```python
    self.config = {
        'host': '127.0.0.1',
        'user': 'your_db_user',
        'password': 'your_db_password',
        'database': 'your_target_db_name',
        'port': 'your_port'
    }
    ```

### 3. Execution

Run the engine to hydrate your database:

```bash
python engine.py
📊 Technical Architecture
The engine acts as the bridge between raw data sources and your WordPress UI. It performs a "digital deposition," ensuring that every property record is mapped correctly to its SQL column.

## 📧 Contact & Collaboration
**Nancy Kerubo** | *Geologist & Digital Architect* * [Email Me](mailto:nancykerry77@gmail.com)
* [Portfolio Site](https://kerubonancyportfolio.netlify.app/g)

Portable. Precise. Professional.
```
