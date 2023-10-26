#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from core.settings import base

def main():
    """Run administrative tasks."""
    # for many service tasks need check DEBUG value
    if base.DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')
        print("Running local management command: ", sys.argv)
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.production')
        print("Running production management command: ", sys.argv)
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
