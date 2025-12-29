"""
Utility functions for the application.
"""

def format_message(text):
    """Format a message with proper capitalization."""
    return text.strip().capitalize()

def validate_input(value):
    """Validate user input."""
    if not value:
        return False
    return True

def get_timestamp():
    """Get current timestamp as a string."""
    from datetime import datetime
    return datetime.now().isoformat()


# add_type_hint - commit 1
