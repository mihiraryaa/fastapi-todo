# FastAPI To-Do List API

## Project Overview
This project is a simple To-Do List API built using FastAPI and MySQL. It provides endpoints to create, retrieve, update, and delete tasks.
## Features
- CRUD operations for managing to-do tasks
- FastAPI for high-performance API development
- MySQL database integration
- Environment-based configuration using `config.env`

## Requirements
- Python 3.8+
- MySQL Server
- Dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/fastapi-todo-api.git
   cd fastapi-todo-api
   ```
2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    ```
    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    venv\Scripts\activate
    ```
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configuration**
    Configure the config.env file in the project root with the following values:
    ```bash
    DB_HOST=your_mysql_host
    DB_USER=your_mysql_user
    DB_PASS=your_mysql_password
    DB_NAME=your_mysql_database
    ```

5. **Running the application**
    Start the FastAPI server using Uvicorn:
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be accessible at http://127.0.0.1:8000.

