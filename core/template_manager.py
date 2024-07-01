
import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from .exceptions import TemplateError

class TemplateManager:
    def __init__(self, template_dirs=None):
        """
        Initialize the TemplateManager.

        Args:
            template_dirs (list): List of directories to search for templates.
                                  If None, uses the default 'templates' directory.
        """
        if template_dirs is None:
            # Use the default 'templates' directory relative to this file
            template_dirs = [os.path.join(os.path.dirname(__file__), '..', 'templates')]
        
        self.env = Environment(
            loader=FileSystemLoader(template_dirs),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True
        )

    def get_template(self, template_name):
        """
        Get a template by name.

        Args:
            template_name (str): Name of the template to retrieve.

        Returns:
            jinja2.Template: The requested template.

        Raises:
            TemplateError: If the template is not found.
        """
        try:
            return self.env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateError(f"Template not found: {template_name}")

    def render_template(self, template_name, context):
        """
        Render a template with the given context.

        Args:
            template_name (str): Name of the template to render.
            context (dict): Context data to use in rendering.

        Returns:
            str: The rendered template as a string.

        Raises:
            TemplateError: If there's an error during template rendering.
        """
        template = self.get_template(template_name)
        try:
            return template.render(context)
        except Exception as e:
            raise TemplateError(f"Error rendering template {template_name}: {str(e)}")

    def add_filter(self, name, filter_func):
        """
        Add a custom filter to the Jinja2 environment.

        Args:
            name (str): Name of the filter.
            filter_func (callable): Function to use as the filter.
        """
        self.env.filters[name] = filter_func

    def add_global(self, name, value):
        """
        Add a global variable to the Jinja2 environment.

        Args:
            name (str): Name of the global variable.
            value: Value of the global variable.
        """
        self.env.globals[name] = value

    def list_templates(self):
        """
        List all available templates.

        Returns:
            list: A list of available template names.
        """
        return self.env.list_templates()

    def reload_templates(self):
        """
        Reload all templates from the file system.
        Useful when templates have been added or modified.
        """
        self.env.cache.clear()

