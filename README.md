# 📚 Library Management System

A RESTful API built with **FastAPI** and **PostgreSQL** to manage a collection of books and user rentals.

## 🛠️ Tech Stack
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Package Manager:** [uv](https://docs.astral.sh/uv/)

---

## 📁 Project Structure
```text
.
├── backend/                # Main application package
│   ├── main.py             # App entry point & routes
│   ├── models.py           # Database models
│   ├── schemas.py          # Pydantic schemas (Data validation)
│   ├── database.py         # Database configuration
│   └── booksdata.csv       # Raw data source
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependency versions
└── README.md               # Project documentation
🚀 Getting Started


1. Installation
Ensure you have uv installed, then run:

uv sync

2. Database Configuration
Update the database connection string in backend/database.py:

Python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

3. Run the Application
Start the development server:
uv run uvicorn backend.main:app --reload

