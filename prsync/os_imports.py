import sys

NAME = sys.platform
if sys.platform == 'win32':
    import wmi
    statvfs = None
else:
    from os import statvfs
    wmi = None

__all__ = ['wmi', 'statvfs']
