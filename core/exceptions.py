
class CodeGenLibError(Exception):
    """Base exception for Code Generation Library."""
    pass

class TemplateError(CodeGenLibError):
    """Raised when there's an issue with templates."""
    pass

class ConfigError(CodeGenLibError):
    """Raised when there's an issue with configuration."""
    pass

class OutputError(CodeGenLibError):
    """Raised when there's an issue with output operations."""
    pass