Change Log
==========

This file contains a summary of major changes to Flask-Diamond.

0.5.1
-----

2017-01-05

- fixed flask-diamond CLI python3 compatibility bug

0.5.0
-----

2017-01-04

- updating flask-security to 1.7.5, flask to 0.11.1
- more robust accounts facet
- moving templates out of core library into skel
- renamed all intances of flask.ext.whatever as flask_whatever
- update rest API docs and skel
- refactor of cli
- migrate global junk into scaffolds
- consolidate Planets tutorial
- update documentation
- testing uses latest available flask-diamond version
- permit testing of core flask-diamond library without scaffolding
- screencast in readme
- simplify naming of documentation files

0.4.12
------

2016-11-14

- remove tutorial dependencies from basic tests

0.4.11
------

2016-11-14

- ensure user registration signal works

0.4.10
------

2016-11-14

- ensure skel references latest version of flask-diamond

0.4.9
-----

2016-11-10

- add user name to GUI Create form

0.4.8
-----

2016-11-10

- fix other python 3 errors

0.4.7
-----

2016-11-05

- fix escaping problem with flask-diamond scaffold

0.4.6
-----

2016-07-25

- update scaffolds to be compatible with py3

0.4.5
-----

2016-07-25

- add example REST interface to scaffolds

0.4.4
-----

2016-07-25

- fix documentation
- fix namespace conflict with REST api

0.4.3
-----

2016-06-09

- permit any sufficiently modern version of Fabric3

0.4.2
-----

2016-05-22

- using Fabric3 instead of Fabric

0.4.1
-----

2016-05-21

- fixed typo in flask-diamond command line app

0.4.0
-----

2016-05-21

- renamed extensions to "facets" (backwards incompatible change)
- new command line utility: "flask-diamond" (was diamond-scaffold.sh)
- enhanced code skeletons: example-models and example-views
- migrated many application components from Flask-Diamond proper into skeletons
- migrated all testing into code skeletons to test actual usage scenario
- deeper integration with Travis CI, including testing using code skeletons
- generally cleaned up the Flask-Diamond core

0.3.6
-----

2016-05-17

- do not fail during setup if files cannot be copied

0.3.5
-----

2016-05-03

- Python 3 compatibility
- added Travis CI
- added Planetary model for testing
- testing for marshmallow

0.3.4
-----

2016-04-29

- adding username to User model schema

0.3.3
-----

2016-04-29

- Python 3 compatibility
- refactor test mixin

0.3.2
-----

2016-04-26

- Python 3 compatibility

0.3.1
-----

2016-04-25

- Python 3 compatibility

0.3.0
-----

2016-01-21

- a new application startup procedure based on extensions
- putting skels into project
- integrate wsgi launcher
- refine questions, add version to project config
- making readme generate from a template
- use alabaster doc theme
- refactor extensions into separate namespace
- added super method, fixing templates
- removing Individual from the skeleton
- refactoring mixins
- simplify views, create separate skel
- added change log document
- documented API creation
- diagram of libraries
- wrote sphinx docs
- wrote email document, testing document
- wrote about user accounts, project diagram
- wrote wsgi, fabric

0.2.16
------

2015-01-21

- putting skels into project

0.2.15
------

2015-08-05

- switch theme to be flask-esque
- adding new documentation stubs and restructuring TOC
- added build details to footer
- created quick-start
- stubbed several new documents
- gather git hash using a different command
- wrote scaffolding explanation
- wrote philosophy and some of the learning section
- starting GUIs with Flask-Admin
- remove sqlite from requirements for documentation build
- separate requirements from installation
- remove pysqlite2 requirement
- added relationship examples to models, rounded out gui examples
- finishing Views documentation
- update migration process

0.2.13
------

2015-07-30

- controlling documentation more closely
- migrating markdown documentation to sphinx
- inter-linking github, pypi, and readthedocs
- add resources to REST api before calling init_app

0.2.12
------

2015-07-30

- This release was used to debug packaging and documentation.

0.2.11
------

2015-07-30

- This release was used to debug packaging and documentation.

0.2.10
------

2015-07-29

- separate models into submodules
- remove backref on user roles to permit easier inheritance and overloading of the User model
- store requirements in separate file
- split documentation into smaller files

0.2.9
-----

2015-07-08

- admin views can be turned off
- admin views can be toggled
- Create Dependencies.md

0.2.8
-----

2015-06-01

- Update manage.py

0.2.7
-----

2015-05-13

- include marshmallow mixin
- loads() from unmarshalled data
- load(), loads(), loadf()

0.2.6
-----

2015-04-24

- hardcoding alembic because the latest version does not parse correctly in FlaskMigrate
- can disable admin views

0.2.5
-----

2015-03-20

- useradd and userdel
- migrate conf files into subdir
- decent isolation of blueprints, but weirdness with security

0.2.4
-----

2015-03-15

- bump flask-admin version
- fixed user create with password
- fixed layout of login page

0.2.3
-----

2015-03-03

- mrbob

0.2.2
-----

2015-03-03

- bump requirements
- reduce required libraries

0.2.1
-----

2015-02-17

- delayed commit in CRUD
- default repr in CRUD
- bump flask script and SQLAlchemy

0.2.0
-----

2015-02-07

- use latest Flask-Migrate==1.3.0
- move user management into user model
- remove unnecessary variables
- reorganize
- meta script helps keep skels aligned
- trying to get migrations neat
- working meta-build
- simpler test fixture
- using relative paths
- scaffolding util
- repair manifest
- fixing paths for databases
- tweak documentation
- automatically sync github pages with API documentation
- API more prominent
- autosync documentation
- include description in sphinx main document
- documented every method

0.1.10
------

2015-02-04

- freeze versions of other dependencies
- update docs

0.1.9
-----

2015-01-25

- PEP8 for setup, migrate a few Flask libraries into the core

0.1.8
-----

2014-11-19

- it is possible to contol the AdminIndexView during app creation

0.1.7
-----

2014-06-29

- use new class instantiation for flask-mail

0.1.6
-----

2014-06-23

- remove ipython dependency

0.1.5
-----

2014-06-16

- more robust user creation
- admin object local to entire package
- update flask-admin dependency

0.1.3
-----

2014-03-29

- do not require a specific version of distribute
- include webassets

0.1.2
-----

2014-03-22

- correct auth mixin ordering
- load/save mixins

0.1.1
-----

2014-03-20

- split error handlers and request handlers
- support changeable passwords
- removed hardcoded config options
- code annotation
- steps towards PEP8
- following Flask capitalization conventions
- account functions are behind /user URL
- CRUD create() may defer commit

0.1
---

2014-03-06

- Initial public release.
