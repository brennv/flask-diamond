Configuration Explanation
=========================

The use of configuration files permits your application to easily adapt to multiple environments.  Often times, different systems will use different path structures, user accounts, database configurations, and TCP ports.  Flask-Diamond implements `the practices suggested by Flask 0.10 <http://flask.pocoo.org/docs/0.10/config/>`_, and by default stores these config files in the ``./etc`` folder of your project.

The SETTINGS Environment Variable
---------------------------------

Flask-Diamond will load its configuration from whatever file is referenced by the ``$SETTINGS`` environment variable.  You can use ``$SETTINGS`` to easily manage several profiles for your application.  The following example demonstrates choosing the development profile stored in ``dev.conf``.

::

    export SETTINGS=$PWD/etc/conf/dev.conf

Another common way to control ``$SETTINGS`` is to use it as a prefix in front of a command.  In the following example, the script ``bin/manage.py`` is invoked with the ``dev.conf`` profile to start the embedded HTTP server:

::

    SETTINGS=$PWD/etc/conf/dev.conf bin/manage.py server


To start the server with the ``production.conf`` environment:

::

    SETTINGS=$PWD/etc/conf/production.conf bin/manage.py server

Examples of Configurations
--------------------------

Flask-Diamond ships with a few configuration profiles to get you started:

dev.conf
^^^^^^^^

The development environment is typically used on your developer workstation.  You probably have root access to the machine.  Any databases are probably temporary in nature, and exist mostly for testing purposes.

production.conf
^^^^^^^^^^^^^^^

The production environment is typically your front-facing web server (a "live server").  In this case, the application is probably not running as root.  In fact, you may not even have root access to this machine.  Thus, you must choose filenames for logging output that are owned by the application user's account.  The production database is also likely to have different permissions, and unlike the development database, the production database probably has important information on it that you want to protect.

testing.conf
^^^^^^^^^^^^

For testing purposes, there is a special configuration that writes to a temporary database that is created and destroyed during tests.

Makefile Support
----------------

If you inspect the ``Makefile``, you will see that ``$SETTINGS=$PWD/etc/conf/dev.conf`` appears before most commands.  Most cases will use ``dev.conf`` by default in order to protect against accidentally performing tasks upon the production database.  Those prefixes are hardcoded so that a command like ``make db`` (which resets the database from scratch) cannot easily be applied to the production database.

Flask-Diamond Configuration Variables
-------------------------------------

By default, Flask-Diamond expects the following variables to be present within a configuration file.

Project
^^^^^^^

The project is configured with the following directives.

::

    PROJECT_NAME = "Flask-Diamond"
    PORT = 5000
    LOG = "/tmp/dev.log"
    LOG_LEVEL = "DEBUG"
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/flask-diamond-dev.db"
    SECRET_KEY = "av^\x81\x03\xd7\xd1\xbd\x92~b\x00\xe8\xf7n9\x0e\xf8i\xdb\xba'\xa9\xea"
    BASE_URL = "http://flask-diamond.org"

- ``PROJECT_NAME``: the human-readable name of the project
- ``PORT``: which TCP port will the HTTP server listen on?
- ``LOG``: the filename to log messages to
- ``LOG_LEVEL``: control the verbosity of logging output; DEBUG prints everything, INFO prints less, and WARN will only display problems.
- ``SQLALCHEMY_DATABASE_URI``: a URI that points to your database.  See `Flask-SQLAlchemy <https://pythonhosted.org/Flask-SQLAlchemy/config.html>`_ for more examples.
- ``SECRET_KEY``: a randomly-generated string that you created during scaffolding
- ``BASE_URL``: the canonical name for your web application

Debugging
^^^^^^^^^

Debugging instructs the application to print extra information during operation.  For example, there may be more verbose logging and it may be possible to inspect the application internals.  All of this is helpful during development, but can be extremely dangerous in production.

::

    DEBUG = False
    DEBUG_TOOLBAR = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

- ``DEBUG``: when debugging is enabled, Flask produces tracebacks when an exception is encountered.
- ``DEBUG_TOOLBAR``: whether to include `Flask-DebugToolbar <http://flask-debugtoolbar.readthedocs.org/en/latest/>`_, which is a helpful in-browser debugging widget.
- ``DEBUG_TB_INTERCEPT_REDIRECTS``: it is possible to inject the debug toolbar before URL redirects, which can be helpful for isolating routing problems.

Accounts and Security
^^^^^^^^^^^^^^^^^^^^^

`Flask-Security <https://pythonhosted.org/Flask-Security/index.html>`_ provides an integrated platform of account security features, and Flask-Diamond incorporates most of its functionality.  The following directives control Flask-Security.

::

    SECURITY_PASSWORD_SALT = "aIf8ObrvtSTkIIGd"
    SECURITY_POST_LOGIN_VIEW = "/admin"
    SECURITY_PASSWORD_HASH = 'sha256_crypt'
    SECURITY_URL_PREFIX = '/user'
    SECURITY_CHANGEABLE = True
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    SECURITY_CONFIRMABLE = False
    SECURITY_REGISTERABLE = False
    SECURITY_RECOVERABLE = False
    SECURITY_TRACKABLE = True
    SECURITY_EMAIL_SENDER = "accounts@flask-diamond.org"

- ``SECURITY_PASSWORD_SALT``: The salt is a random string you generated during scaffolding.  This is used to encrypt the password database.
- ``SECURITY_POST_LOGIN_VIEW``: the name of the view to redirect to upon a successful login
- ``SECURITY_PASSWORD_HASH``: the name of the hashing algorithm to use for passwords.  **sha256_crypt** is recommended.
- ``SECURITY_URL_PREFIX``: Change the URL prefix to make all account-related facilities appear as a subdirectory (like ``/user``).
- ``SECURITY_CHANGEABLE``: Can users change their own passwords?
- ``SECURITY_SEND_PASSWORD_CHANGE_EMAIL``: Should users be notified by email when their password is changed?
- ``SECURITY_CONFIRMABLE``: Must users confirm their email address in order to activate their account?
- ``SECURITY_REGISTERABLE``: Is self-registration allowed?
- ``SECURITY_RECOVERABLE``: Can a user reset their password if they have forgotten it?
- ``SECURITY_TRACKABLE``: Does the User model include fields for recording User account history?  By default, Flask-Diamond provides these fields.  See `the Flask-Security docs <https://pythonhosted.org/Flask-Security/models.html#trackable>`_ for more information about this.
- ``SECURITY_EMAIL_SENDER``: What is the email address that security messages should be sent from?

ReCAPTCHA
^^^^^^^^^

Flask-Captcha provides a quick mechanism for ensuring your application is used by people instead of bots.  You may recognize CAPTCHA as the squiggly letters and numbers that you must type into a text box.  In order to get started with CAPTCHA and ReCAPTCHA, you must create a free account with their service.

::

    RECAPTCHA_PUBLIC_KEY = '0000_00000000000000000000000000000000000'
    RECAPTCHA_PRIVATE_KEY = '0000_00000000000000000000000000000000000'

- ``RECAPTCHA_PUBLIC_KEY``: The ReCAPTCHA online service will provide you with a public key, which will be included with your web application.
- ``RECAPTCHA_PRIVATE_KEY``: ReCAPTCHA also provides a private key, but this one must be kept secret.  You will enter it in this configuration file, but nowhere else.

Flask-Mail
^^^^^^^^^^

The simplest way for your application to send email is using Flask-Mail, which makes it pretty easy to create and send emails.

::

    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None

- ``MAIL_SERVER``: the hostname or IP address of your SMTP server
- ``MAIL_PORT``: the port used by your SMTP server.  Usually, this is 25 or 465.
- ``MAIL_USE_TLS``: If the server supports or requires encryption (with TLS), then set this to *True*
- ``MAIL_USERNAME``: If you must provide authentication information to your server in order to send email through it, then provide the username here.
- ``MAIL_PASSWORD``: As with the username, provide the password here if it is required.

Celery
^^^^^^

Celery is a job queue that has been integrated into Flask-Diamond so that you create background tasks for any operations that take a while to complete.  Typically, you will want your application to respond to requests within 100ms, but when this is not possible, you can achieve a rapid response by queueing the slow operation so that it executes separately.  This way, it is still possible to respond to requests quickly enough that nobody will notice.

::

    CELERY_BROKER_URL = 'sqla+sqlite:///var/db/celerydb.sqlite'
    CELERY_RESULT_BACKEND = 'db+sqlite:///var/db/results.sqlite'

- ``CELERY_BROKER_URL``: the URL pointing to a database connection.  This is like the SQLAlchemy URI, but different enough that you should consult the documentation.
- ``CELERY_RESULT_BACKEND``: Celery is able to store job results in a separate database, and for certain types of jobs, this is recommended.  The URI here is similar to but different from the *CELERY_BROKER_URL*.
