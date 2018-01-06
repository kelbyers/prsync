import sys

from os import stat_result

if sys.platform == 'win32':
    import wmi
    statvfs = None
else:
    from os import statvfs
    wmi = None

NAME = sys.platform

__all__ = ['wmi', 'statvfs', 'stat_result']
