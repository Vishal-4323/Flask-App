# Flask Application

## Steps
### Create a Database and Table in PostgreSQL
- Create a new database
```bash
CREATE DATABASE db_name;
```
- Connect to the database
```bash
\c db_name;
```
- Create a table
```bash
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
```
- Insert sample data
```bash
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');
```

### Run the Application
- Created a .env file.
- And added the database credentials in following format in the file.
```bash
DB_HOST=GIVE YOUR DB HOST
DB_PORT=GIVE YOUR DB PORT
DB_NAME=GIVE YOUR DB NAME
DB_USER=GIVE YOUR DB USER
DB_PASSWORD=GIVE YOUR DB PASSWORD
```
- Then, run the application using python command.
```python
python app.py
```
- You can see the application running on port 5000.
