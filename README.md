# django_snippets
My personal django snippets &amp; templates for easy setup 

# Project directory structure

```
myproject
│   README.md
│   manage.py    
│
└───templates
│   │   index.html
│   │   header.html
|   |   page.html
│   │
│   └───css
│   |   │   main.css
|   |   |   page.css
|   |   
│   └───js
│       │   main.js
│       |   page.js   
|
└───home
│   │   __init__.py
│   │   admin.py
│   │   apps.py
│   │   tests.py
│   │   views.py
│   │   models.py
│   │   forms.py
│   
└───myproject
    │   __init__.py
    │   asgi.py
    │   wsgi.py
    │   settings.py
    │   urls.py
```

# Basic commands

- ### Creating models by introspecting all tables in an existing database 
    - ```$~ python manage.py inspectdb > home/models.py```

- ### Introspecting specific tables in an existing database 
    - ```$~ python manage.py inspectdb table1 table2 tableN > home/dbdata.py```

- ### Introspecting specific tables in specific database when multiple databases are connected to django
    - ```$~ python manage.py inspectdb --database=[dbname_as_defined_in_settings] table1 table2 tableN > home/dbdata.py```
