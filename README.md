# flask base with db

### Install

```bash
pip install -r requirements.txt
mysql -u root -p
```

>Maybe install, `pip install pymysql`

### Create database

```sql
mysql> create database flaskbase;
```

### Change your database url in app.py

```python
DB_URL = 'mysql+pymysql://user:password@localhost:3306/flaskbase'
```

### start app

```bash
python app.py
```

### Open browser or ...

[home](http://localhost:5000)


---
License: no

