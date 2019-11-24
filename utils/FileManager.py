#!/usr/bin/env python3
#last modified: 20191112
import os
from datetime import datetime


class FileManager:
    current_timestamp = ''
    log_path = ''
    out_path = ''
    caller_class_name = ''
    out_files = []

    def __init__(self, script_name='', class_name='', predefined_path=''):
        root = os.path.realpath(__file__).split('/utils/')[0]
        self.log_path = root + '/logs/' + script_name
        self.out_path = root + '/out/' + script_name
        self.current_timestamp = str(datetime.now().strftime('%Y%m%d%H%M%S'))

        if not os.path.exists(self.log_path):
            self.validate_dir(root, 'logs/' + script_name + '/')
        if not os.path.exists(self.out_path):
            self.validate_dir(root, 'out/' + script_name + '/')

        if predefined_path is '':
            self.out_path = self.out_path + '/' + self.current_timestamp
        else:
            self.out_path = self.out_path + '/' + predefined_path
            self.validate_dir(root, 'out/' + script_name + '/' + predefined_path + '/')

        if not os.path.exists(self.out_path):
            os.mkdir(self.out_path)

        self.caller_class_name = class_name

    def validate_dir(self, base_path, entry):
        entries = entry.split('/')
        if len(entries) > 1:
            a_path = base_path + '/' + entries.pop(0)
            if not os.path.exists(a_path):
                os.mkdir(a_path)
            self.validate_dir(a_path, '/'.join(entries))

    def delete_outfile(self, filename):
        if os.path.exists(self.out_path + '/' + filename):
            os.remove(self.out_path + '/' + filename)

    def get_outfile(self, filename):
        self.validate_dir(self.out_path, filename)
        return self.out_path + '/' + filename

    def get_all_outfiles(self):
        return self.out_files

    def log_info(self, message):
        self.log('info', message)
    
    def log_error(self, message):
        self.log('error', message)
    
    def log(self, level, message):
        filename = datetime.now().strftime('%Y%m%d')+'.log'
        log_file = open(self.log_path + '/' + level + '_' + filename, 'a')
        log_file.writelines(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + ' ' +
                            self.caller_class_name + ' - ' + "{}".format(message) +'\n')
        log_file.close()

    def out(self, entry, filename, unique=False):
        if unique:
            self.delete_outfile(filename)
        out_filename = self.get_outfile(filename)
        if not contains(self.out_files, out_filename):
            self.out_files.append(out_filename)
        out_file = open(out_filename, 'a')
        out_file.writelines(entry+'\n')
        out_file.close()


def contains(items, target):
    for item in items:
        if item == target:
            return True
    return False
