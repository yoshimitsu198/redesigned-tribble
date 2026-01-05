#!/usr/bin/env python3
"""
Main application entry point.
"""

import config
import logger

def main():
    log = logger.setup_logger()
    log.info("Application starting")
    
    print(f"Welcome to {config.APP_NAME}!")
    print(f"Version {config.APP_VERSION}")
    
    log.info("Application initialized successfully")
    return 0

if __name__ == "__main__":
    exit(main())


# improve_error_handling - commit 7

# add_comments - commit 36

# add_cli_args - additional commit 16
