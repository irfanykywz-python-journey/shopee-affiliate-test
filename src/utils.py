import inspect
import os

from importlib.util import spec_from_loader, module_from_spec
from PySide6.QtCore import QSettings


def get_setting():
    setting = QSettings('setting.ini', QSettings.Format.IniFormat)
    return setting

def get_script():
    files = []
    for file in os.listdir('scripts'):
        if '__init' in file or '__pycache' in file:
            continue
        files.append(file)
    return files

def import_module_from_string(s, n='mod'):
    spec = spec_from_loader(n, None)
    module = module_from_spec(spec)
    exec(s, module.__dict__)
    return module

def import_class_from_string(s):
    module = import_module_from_string(s, 'core_class')
    for name, className in inspect.getmembers(module, inspect.isclass):
        if className.__module__ == 'core_class':
            return className

def get_string(file_name):
    with open(file_name, 'rb') as file:
        return file.read()

def get_class(file_name):
    string = get_string(file_name)
    return import_class_from_string(string)

def get_module(file_name):
    string = get_string(file_name)
    return import_module_from_string(string, 'core_module')
