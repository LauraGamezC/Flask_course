# Application Package

The application package is where all the application code, templates, and static files live. The database models and the email support functions are part of this package too.

## __init__.py

Is a constructor that imports most of the Flask extensions currently in use, but because there is no application instance to initialize them with, it creates them uninitialized by passing no arguments into their constructors.
 