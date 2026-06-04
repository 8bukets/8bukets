# Developer Corner

Here is a starter snippet for your deployment:

```python
# Python: Connect to Oracle Database
import cx_Oracle
import os

dsn = cx_Oracle.makedsn("dbhost", 1521, service_name="orcl")

# Use environment variables for credentials
user = os.environ.get("DB_USER", "hr")
password = os.environ.get("DB_PASSWORD")

if not password:
    raise ValueError("DB_PASSWORD environment variable not set")

connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
print("Successfully connected to Oracle Database")
```
