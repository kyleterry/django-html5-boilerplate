# A Simple Django HTML5 Boilerplate

This is meant to be very simple. No batteries included. I often need only
what you see in these templates when firing up a new project.

It provides only the base set of block tags you need to get started with 
HTML5.

## Installation

Through pypi:

`pip install djangohtml5boilerplate`

Or take the manual route:

`git clone https://github.com/kyleterry/django-html5-boilerplate.git && cd djangohtml5boilerplate && python setup.py install`

## Configuration

Add `djangohtml5boilerplate` to your settings.py's `INSTALLED_APPS` tuple.

Start a new template:

    {% extends "html5boilerplate/base.html" %}
    
    {% block css %}
        <link href="{{STATIC_URL}}appname/css/core.css">
    {% endblock css %}
    
    {% block header_content %}
        <h1>This is an awesome header!</h1>
    {% endblock header_content %}
    
    {% block content %}
        <p>Here is some of my favorite content.</p>
    {% endblock content %}
    
    {% block footer_content %}
        <p>&copy; Some Name 2013</p>
    {% endblock footer_content %}
    
    {% block body_js %}
        ... Google analytics or something
    {% endblock body_js %}

Or you can override the body completely. (body_js sticks around because everyone needs that):

    {% extends "html5boilerplate/base.html" %}
    
    {% block css %}
        <link href="{{STATIC_URL}}appname/css/core.css">
    {% endblock css %}
    
    {% block body %}
    <div id="custom_header">
        <h1>Custom Header</h1>
    </div>
    <div id="custom_content">
        <h1>Custom content</h1>
    </div>
    <div id="custom_footer">
        <h1>&copy; Custom footer 2013</h1>
    </div>
    {% endblock body %}
