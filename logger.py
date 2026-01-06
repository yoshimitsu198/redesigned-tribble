"""
Logging utility for the application.
"""

import logging
import config

def setup_logger():
    """Set up and configure the application logger."""
    logger = logging.getLogger(config.APP_NAME)
    logger.setLevel(getattr(logging, config.LOG_LEVEL))
    
    handler = logging.FileHandler(config.LOG_FILE)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger



# add_console_handler - commit 4

# improve_formatter - commit 15

# add_log_rotation - commit 16

# add_logger_comments - commit 39

# optimize_logger - additional commit 6

# add_async - additional commit 7

# add_structured - additional commit 8
