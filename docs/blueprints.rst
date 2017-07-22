Facet: Blueprints
=================

As is explained in :doc:`model-view-controller`, a *View* takes data from a Model and presents it (typically to a user).
Often times, there are multiple Views of a data Model, and they may present different aspects of the Model.
A common pattern for multiple views is the use of permissions to restrict functionality to users based upon their account role.
The administrator may have a special *View* into the data that provides extra functionality that regular users do not have.

Views are frequently written using *templates*, which have placeholders for variables that may be filled in by the application.
In Flask-Diamond, the `Jinja templating language <http://jinja.pocoo.org/>`_ is used to generate HTML, javascript, CSS, and other web-facing files that create a user interface.
By populating the template with data from the Model, the result is that users can interact with Model data.

Jinja is a Templating Language
------------------------------

The rest of this document provides a summary of the key points about Jinja Views.
The `Jinja website <http://jinja.pocoo.org/>`_ provides a nice example of what Jinja looks like:

::

    {% extends "layout.html" %}
    {% block body %}
      <ul>
      {% for user in users %}
        <li><a href="{{ user.url }}">{{ user.username }}</a></li>
      {% endfor %}
      </ul>
    {% endblock %}

A detailed discussion of templates is available from the `Jinja templates documentation <http://jinja.pocoo.org/docs/dev/templates/>`_.

Variables in Jinja
^^^^^^^^^^^^^^^^^^

A python expression within a Jinja template is denoted using double-curlies as ``{{ }}``.
In this manner, it is easy to reference variables by simply placing them inside double-curlies.
In the example above, *user.username* will be replaced by the actual value of a user's username (e.g. "administrator").
If it were not inside the double-curlies, "user.username" would be printed verbatim (i.e. substitution is not performed unless inside double-curlies).

Statements in Jinja
^^^^^^^^^^^^^^^^^^^

A python statement (like an "if statement") is denoted in Jinja using ``{% %}``.
Using statements, it is possible to create dynamic templates that print different details based upon the data given to them.
To use :doc:`tutorial-planets` as an example, we could extend the template to print a special message when Earth is viewed.

::

    {% if planet.name=='earth' %}
        Go Earthlings!
    {% endif %}

Rendering a template with Flask
-------------------------------

Flask provides an easy mechanism for working with templates that is called `render_template() <http://flask.pocoo.org/docs/0.10/api/#flask.render_template>`_.
When a template is rendered with data, the placeholders inside the template are replaced with the data.
In the case of web applications, the result is typically an HTML document that presents the application's data model in a format that a human could use through a web browser.

To render the previous template, first save it to a file called ``my_template.html`` and place that in a directory called ``templates``.

The code looks like:

::

    my_data = {"users": [{"username": "administrator", "url", "http://example.com"}]}
    return flask.render_template("my_template.html", **my_data)

Flask searches for templates by looking through a directory called "templates".
This behaviour can be extended by using Blueprints, which are explained a little later in this document.
More information about Flask and templates is available from the `Flask templating documentation <http://flask.pocoo.org/docs/0.10/templating/>`_.

Routing a View
--------------

URLs are used within web applications to identify Views.
In :doc:`tutorial-planets`, the URL */planet_list* could return with a summary of all the planets in the database, and a URL like */planet/earth* could provide information about the named planet.

When building an :doc:`MVC <model-view-controller>` View for a web application, the Controller is responsible for actually routing the user to the View.
MVC Web applications use the URL to connect with a view, such that a user can use their web browser to request */user/login_form* in order to log in to a website or view the */planet/earth* to view details about a planet called Earth.
In Flask, the `route() <http://flask.pocoo.org/docs/0.10/api/#flask.Flask.route>`_ decorator is used to apply a route to a View function.

A simple route looks like:

::

    @app.route('/')
    def index():
        return "Hello world!"

The `Site Map <https://en.wikipedia.org/wiki/Site_map>`_ is used to determine all the routes that will be necessary for exposing a web application.
Every View must be present within the Site Map, and there must be a unique URL for each View.

It is possible to look at a Flask-Diamond web application site map from within the application itself:

::

    print flask.current_app.url_map

Flask Blueprints: a Collection of Views
---------------------------------------

Often times, there will be several related views and it makes sense to collect these together using a `Flask Blueprint <http://flask.pocoo.org/docs/0.10/blueprints/>`_.
When this happens, the views are collected into a URL subdirectory, and individual views are nested within that URL.
In :doc:`tutorial-planets`, there could be several views related to tracking moons (satellites), which could be collected into the */satellite* directory.

The Flask documentation demonstrates `an extremely simple blueprint <http://flask.pocoo.org/docs/0.10/blueprints/#my-first-blueprint>`_:

::

    from flask import Blueprint, render_template, abort
    from jinja2 import TemplateNotFound

    simple_page = Blueprint('simple_page', __name__,
                            template_folder='templates')

    @simple_page.route('/', defaults={'page': 'index'})
    @simple_page.route('/<page>')
    def show(page):
        try:
            return render_template('pages/%s.html' % page)
        except TemplateNotFound:
            abort(404)

This example demonstrates everything we have discussed so far:

- the ``render_template`` function
- the ``template_folder`` that contains Jinja templates
- routing the View to a URL with ``route()``

The Flask documentation also explains `how to register a blueprint <http://flask.pocoo.org/docs/0.10/blueprints/#registering-blueprints>`_ with an application:

::

    from flask import Flask
    from planets.simple_page import simple_page

    app = Flask(__name__)
    app.register_blueprint(simple_page)

Views within Flask-Admin BaseModelView
--------------------------------------

In :doc:`Flask-Admin <administration>`, each BaseModelView is actually a Blueprint that provides views for :doc:`creating, reading, updating, and deleting <crud>` model objects.  The BaseModelView template behaves much like a regular blueprint, except:

- `expose() <http://flask-admin.readthedocs.org/en/latest/api/mod_base/#flask_admin.base.expose>`_ is used to "expose" a view inside BaseModelView instead of `route() <http://flask.pocoo.org/docs/0.10/api/#flask.Flask.route>`_
- `self.render() <http://flask-admin.readthedocs.org/en/latest/api/mod_base/#flask_admin.base.BaseView.render>`_ is used instead of `render_template <http://flask.pocoo.org/docs/0.10/api/#flask.render_template>`_

In this manner, it becomes easy to extend a CRUD with custom methods that go beyond create, read, update, and delete.
