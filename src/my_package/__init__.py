"""
My Package - A self-maintaining Python package.

This is a template package demonstrating Claude-powered automated maintenance.
Replace this with your actual package code.
"""

__version__ = "0.1.0"


def hello(name: str = "World") -> str:
    """Return a greeting message.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.

    Example:
        >>> hello("Claude")
        'Hello, Claude!'
    """
    return f"Hello, {name}!"


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b
