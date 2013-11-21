#!/usr/bin/env python
# __author__ = 'Vidmantas Zemleris'
"""
Provide validation of DAS Maps

It checks:
 * presence of mandatory fields
 * correct naming/typing of known fields
 * validity of hash value, if one present
"""
from schema import Schema, And, Or, Optional, validate_mongodb_json
import hashlib
import json
import sys


def check_hash(rec):
    """Check record hash"""
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

# validate_record_map
map_record = And(
    {'hash': _str,
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
     Optional('instances'): list,  # TODO
     # TODO: optional str:str allowed, as in original validator
     #Optional(_str): Optional(_str),
     },
    check_hash)

# validate_presentation_map
presentation_record = And({'presentation': dict,
                           'ts': float,
                           'hash': _str},
                          check_hash)
# TODO: enforce presence of obligatory fields?
# validate_notation_map
notation_record = And({'notations': [{'rec_key': _str,
                                      'api': _str,
                                      'api_output': _str}],
                       'system': _str,
                       'ts': float,
                       'hash': _str,
                       # TODO: optional str:str allowed, as in original validator
                       # TODO: Optional(_str): _str
                       },
                      check_hash)
# arecord
arecord_record = {'arecord': dict}

#TODO: schema: optional(type) when the name is unknown matches even known items

mapping_schema = \
    Schema(Or(  # the arecord that use no hash shall go first
                # to avoid false complaints in check_hash
                arecord_record,
                map_record,
                presentation_record,
                notation_record))

from schema import SchemaError
import pprint
rules = {
        'arecord_record': Schema(arecord_record),
        'map_record': Schema(map_record),
        'presentation_record': Schema(presentation_record),
        'notation_record': Schema(notation_record)}


def validate_verbose(item, print_success=False):
    ok = False
    errors = []
    for rule_name, rule in rules.items():
        try:
            rule.validate(item)
            ok = True
            if print_success:
                print 'OK:', item
            continue
        except SchemaError as x:
            errors.append(('rule %s failed:' % rule_name, x))
    if not ok:
        print 'can not validate the record:', item
        pprint.pprint(errors)
        return False
    return True


def validate_file_verbose(filename):
    with open(filename) as f:
        for line in f:
            doc = json.loads(line)
            if not validate_verbose(doc):
                return False
    return True


def main():
    "Main function"
    if  len(sys.argv) != 2:
        print "Usage: validator <dasmap_update_file.js>"
        sys.exit(1)
    if not validate_file_verbose(sys.argv[1]):
        sys.exit(1)
#
# main
#
if __name__ == '__main__':
    main()        
