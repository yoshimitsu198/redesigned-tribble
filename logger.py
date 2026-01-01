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

