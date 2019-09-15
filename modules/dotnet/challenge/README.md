# Challenge: SQL Lite Connect

For this challenge you are tasked to get data from a SQL Lite store and filter on alma mater data.

The database `employees.db` was created with the following script
```
CREATE TABLE employees
                (first_name text, last_name text, birth_date DATETIME, alma_mater text)

INSERT INTO employees(first_name, last_name, birth_date, alma_mater) VALUES
        ('Andrew', 'Zoolkowski', '1995-03-05', 'University of Nebraska-Lincoln'),
        ('John', 'Loween', '1997-02-01', 'University of Minnesota Twin Cities'),
        ('William', 'Portails', '1959-02-03', 'Harvard'),
        ('David', 'Millar', '1992-04-04', 'MIT'),
        ('Winston', 'Pickler', '1991-08-09', 'Stanford'),
        ('Anna', 'Boardman', '1970-06-02', 'University of Nebraska-Lincoln');
```

You should create a function that will read a file and return a List of strings in the format

"{first} {last}, {age} {almamater}"

But the list should only contain people who went to:
University of Nebraska-Lincoln
Stanford
MIT


## Tips

- You may want to use a data browser like DBeaver or sqlitestudio to view the data
- You can install an auto-using extension that will help getting your using statements loaded