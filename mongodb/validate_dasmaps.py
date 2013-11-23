#!/usr/bin/env python
#-*- coding: ISO-8859-1 -*-
# __author__ = 'Vidmantas Zemleris'
"""
Provide validation of DAS Maps

It checks:
 * presence of mandatory fields
 * correct naming/typing of known fields
 * validity of hash value, if one present
"""
import hashlib
import json
import sys

from schema_validator import Schema, And, Or, Optional, validate_file_verbose


def check_hash(rec):
    """ Check record hash """
    nrec = dict(rec)
    if 'hash' in nrec:
        md5 = nrec.pop('hash')
        # exclude timestamps since they are dynamic
        if 'ts' in nrec:
            del nrec['ts']
        if 'timestamp' in nrec:
            del nrec['timestamp']
        nrec = json.JSONEncoder(sort_keys=True).encode(nrec)
        keyhash = hashlib.md5()
        keyhash.update(nrec)
        rmd5 = keyhash.hexdigest()
        if md5 != rmd5:
            print 'Invalid hash'
            print "record:", rec
            print "nrec:", nrec
            print "md5   :", md5
            print "rmd5  :", rmd5
            return False
    return True


_str = basestring  # a shorthand for string type

# schema of map_record
MAP_RECORD = And(
    {
        'hash': _str,
        'format': _str,
        'url': _str,
        'urn': _str,
        'ts': float,
        'system': _str,
        'das_map': [{
                        'rec_key': _str,
                        'das_key': _str,
                        Optional('api_arg'): _str,
                        Optional('pattern'): _str}],
        'services': Or({_str: _str},
                       # it can also be empty value
                       lambda v: not v),
        'expire': int,
        'lookup': _str,
        'wild_card': _str,
        'params': {_str: Or(_str, bool, list)},
        'type': 'service',
        Optional('instances'): list,

        #TODO: error message when an unexpected field is present is not clear
        # see https://github.com/halst/schema/issues/3

        # Currently we do not allow just arbitrary fields..
        # to allow optional args of unknown names as in the original validator
        # one may just use  _str: _str. however more strict is better?
    },
    check_hash)

# schema of presentation_map record
PRESENTATION_RECORD = And(
    {
    'presentation': dict,
    'ts': float,
    'hash': _str,
    'type': 'presentation'},
    check_hash)

# schema of notation_map record
NOTATION_RECORD = And(
    {'notations': [{'rec_key': _str,
                    'api': _str,
                    'api_output': _str}],
     'system': _str,
     'ts': float,
     'hash': _str,
     'type': 'notation'
     # TODO: allow optional str:str, as in original validator
     # Optional(_str): _str
     },
    check_hash)

# schema of "arecord"
ARECORD_RECORD = {'arecord': dict}

# define a list of complementary rules, where at least one must match, this
# instead of just Schema(Or(a, b, c)) will provide more informative feedback
SCHEMA_RULES = {
    'arecord_record': Schema(ARECORD_RECORD),
    'map_record': Schema(MAP_RECORD),
    'presentation_record': Schema(PRESENTATION_RECORD),
    'notation_record': Schema(NOTATION_RECORD)}


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print "Usage: validator <dasmap_update_file.js>"
        sys.exit(1)
    if not validate_file_verbose(SCHEMA_RULES, sys.argv[1]):
        sys.exit(1)

#
# main
#
if __name__ == '__main__':
    main()
