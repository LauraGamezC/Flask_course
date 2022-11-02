# Database Operations

In chapter5.py were configured a database and defined two classes (Role and User) with their table respectively.  
You can add data to this tables with following the next instructions

## Creating tables

To create a table is needed to define the env variable:  

```
export FLASK_APP=chapter5.py
```

Start the Flask shell, import db from the file chapter5.py and create the table
```
flask shell
>>> from chapter5.py import db
>>> db.create_all()
```
In the directory you will see a new file data.sqlite   

## Update existing database

```
>>> db.drop_all()
>>> db.create_all()
```

### Insert Rows

```
>>> from hello import Role, User
>>> admin_role = Role(name='Admin')
>>> mod_role = Role(name='Moderator')
>>> user_role = Role(name='User')
>>> user_john = User(username='john', role=admin_role)
>>> user_susan = User(username='susan', role=user_role)
>>> user_david = User(username='david', role=user_role)
```
Changes to the database are managed through a database session, which FlaskSQLAlchemy provides as db.session.  

```
db.session.add_all([admin_role, mod_role, user_role,
... user_john, user_susan, user_david])
```

To write the objects to the database, the session needs calling its commit() method:

```
db.session.commit()
```

Now, you can notice the id were generated.  

### Modifying Rows

```
>>> admin_role.name = 'Administrator'
>>> db.session.add(admin_role)
>>> db.session.commit()
```

### Deleting Rows

```
>>> db.session.delete(mod_role)
>>> db.session.commit()
```

### Querying Rows

The next lines returns all rows  

```
>>> Role.query.all()
>>> User.query.all()
```

A query object can be configured to issue more specific database searches through
the use of filters

```
>>> User.query.filter_by(role=user_role).all()
>>> user_role = Role.query.filter_by(name='User').first() 
````



