#!/usr/bin/env python3
"""
Main application entry point.
"""

import config

def main():
    print(f"Welcome to {config.APP_NAME}!")
    print(f"Version {config.APP_VERSION}")
    return 0

if __name__ == "__main__":
    exit(main())

