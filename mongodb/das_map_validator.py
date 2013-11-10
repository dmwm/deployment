#!/usr/bin/env python
#pylint: disable-msg=R0912

"""
DAS map validator
"""
__author__ = "Valentin Kuznetsov"

import sys
import json
import inspect
import hashlib

def print_map(msg, imap, linenumber):
    "Print failure message for given DAS map"
    print "Failed   :", msg
    print "Code line:", linenumber
    print "DAS map  :", imap

def line_number():
    "Returns the current code line number"
    return inspect.currentframe().f_back.f_lineno

def check_hash(rec):
    "Check record hash"
    nrec = dict(rec)
    if  nrec.has_key('hash'):
        md5 = nrec.pop('hash')
        # exclude timestamp since they are dynamic
        if  'ts' in nrec:
            del nrec['ts']
        if  'timestamp' in nrec:
            del nrec['timestamp']
        nrec = json.JSONEncoder(sort_keys=True).encode(nrec)
        keyhash = hashlib.md5()
        keyhash.update(nrec)
        rmd5 = keyhash.hexdigest()
        if  md5 != rmd5:
            print 'Invalid hash'
            print "record:", rec
            print "md5   :", md5
            print "rmd5  :", rmd5
            sys.exit(1)

def check_keys(imap, valid_keys, map_name):
    "Check imap keys"
    check_hash(imap)
    if  set(imap.keys()) & set(valid_keys) != set(valid_keys):
        msg = "Invalid %s map keys" % map_name
        print imap.keys()
        print valid_keys
        print_map(msg, imap, line_number())
        sys.exit(1)

def validate_notation_map(imap):
    "Validate notation map"
    valid_keys = ['notations', 'system', 'ts', 'hash']
    check_keys(imap, valid_keys, 'notation')
    if  not isinstance(imap['notations'], list):
        msg = "Invalid data type of notation value"
        print_map(msg, imap, line_number())
        sys.exit(1)
    for key, val in imap.items():
        if  key == 'notations':
            for item in val:
                if  item.keys() != ['rec_key', 'api', 'api_output']:
                    msg = "Invalid keys of notation record"
                    print_map(msg, imap, line_number())
                    sys.exit(1)
        elif key == 'ts':
            if  not isinstance(val, float):
                msg = "Invalid 'create' data type"
                print_map(msg, imap, line_number())
                sys.exit(1)
        else:
            if  not isinstance(val, basestring):
                msg = "Invalid '%s' data type" % key
                print_map(msg, imap, line_number())
                sys.exit(1)

def validate_presentation_map(imap):
    "Validate presentation map"
    valid_keys = ['presentation', 'ts', 'hash']
    check_keys(imap, valid_keys, 'presentation')

def validate_record_map(imap):
    "Validate record map"
    valid_keys = ['format', 'wild_card', 'expire', 'services', 'ts',
            'url', 'urn', 'system', 'das_map', 'lookup', 'params', 'hash']
    check_keys(imap, valid_keys, 'record')
    for key, val in imap.items():
        if  key == 'das_map':
            if  not isinstance(val, list):
                msg = "Invalid data type of das_map key"
                print_map(msg, imap, line_number())
                sys.exit(1)
            else:
                das_map_keys = ['rec_key', 'api_arg', 'das_key']
                for rec in val:
                    if  not set(rec.keys()) & set(das_map_keys):
                        msg = "Invalid das_map_keys"
                        print_map(msg, imap, line_number())
                        sys.exit(1)
        elif key == 'params':
            if  not isinstance(val, dict):
                msg = "Invalid params data type"
                print_map(msg, imap, line_number())
                sys.exit(1)
        elif key == 'services':
            if  not val:
                continue
            if  not isinstance(val, dict):
                msg = "Invalid params data type"
                print_map(msg, imap, line_number())
                sys.exit(1)
        elif key == 'expire':
            if  not isinstance(val, int):
                msg = "Invalid 'expire' data type"
                print_map(msg, imap, line_number())
                sys.exit(1)
        elif key == 'ts':
            if  not isinstance(val, float):
                msg = "Invalid 'create' data type"
                print_map(msg, imap, line_number())
                sys.exit(1)
        elif key == 'instances':
            if  not isinstance(val, list):
                msg = "Invalid 'instances' data type"
                print_map(msg, imap, line_number())
                sys.exit(1)
        else:
            if  not (isinstance(val, basestring) or isinstance(val, list)):
                msg = "Invalid '%s' data type, val=%s, type=%s" \
                        % (key, val, type(val))
                print_map(msg, imap, line_number())
                sys.exit(1)

def validator(fname):
    "DAS map JSON validator"
    valid_map_keys = ['notations', 'urn', 'presentation', 'arecord']
    with open(fname, 'r') as stream:
        for line in stream.readlines():
            try:
                das_map = json.loads(line)
            except:
                msg = "Unable to parse das_map file"
                print_map(msg, line, line_number())
                sys.exit(1)
            if  not isinstance(das_map, dict):
                msg = "Invalid data type"
                print_map(msg, das_map, line_number())
                sys.exit(1)
            keys = set(das_map.keys()) & set(valid_map_keys)
            if  not keys:
                msg = "Invalid keys %s" % das_map.keys()
                print_map(msg, das_map, line_number())
                sys.exit(1)
            if  das_map.has_key('notations'):
                validate_notation_map(das_map)
            if  das_map.has_key('urn'):
                validate_record_map(das_map)

def main():
    "Main function"
    if  len(sys.argv) != 2:
        print "Usage: validator <das_map.js>"
        sys.exit(1)
    validator(sys.argv[1])
#
# main
#
if __name__ == '__main__':
    main()
