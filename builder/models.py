from django.db import models
from django_grapesjs.models import GrapesJsHtmlField
from django.template.loader import render_to_string

class ExampleModel(models.Model):
    html = GrapesJsHtmlField()


    # default_html - path to the html file to display the default value
    # for the field when the form page is received
    html = GrapesJsHtmlField(default_html='default.html')

    # or default - if the page is simply static
    html = GrapesJsHtmlField(default=render_to_string('default.html'))


    # use the redactor_config argument to select the configuration of the editor
    # Available:
    #     - redactor_config='base' - basic setting, most widgets are used
    #     - redactor_config='min' - minimum setting, only the most necessary
    html = GrapesJsHtmlField(redactor_config='base')
 
    # use apply_django_tag = True, if you want to apply render django or jinja tags
    html = GrapesJsHtmlField(default_html='default.html', apply_django_tag=True)
    

    # use template_choices to select multiple templates
    html = GrapesJsHtmlField(template_choices=(('django_grapesjs/default.html', 'default'),))