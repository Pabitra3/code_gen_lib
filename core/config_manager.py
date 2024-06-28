
import yaml

class ConfigManager:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_config(self, template_name):
        if template_name not in self.config:
            raise ConfigError(f"No configuration found for template: {template_name}")
        return self.config[template_name]

    def get_required_kwargs(self, template_name):
        config = self.get_config(template_name)
        return config.get('required_kwargs', [])