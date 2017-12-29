from platform import system

NAME = system()
if NAME == 'Windows':
    import wmi
    statvfs = None
else:
    from os import statvfs
    wmi = None
