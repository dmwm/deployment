#-*- coding: ISO-8859-1 -*-
#pylint: disable-msg=C0111,C0103
#pylint disabled: C0111(missing-docstring), C0103(invalid-name)
"""
Minor customizations to validate files of multiple json documents
Based on: https://github.com/halst/schema

Sample schemas:

.. doctest::
    inputvals = Schema({'_id': {'$oid': And(basestring, len)},
                        'ts': float,
                        'value': basestring})

    keylearning_schema = \
        Schema(Or({'_id': {'$oid': And(basestring, len)},
                   'keys': [basestring, ],
                   'members': [basestring, ],
                   'system': basestring,
                   'urn': basestring},
                  {'_id': {'$oid': And(basestring, len)},
                   'member': basestring,
                   'stems': [basestring, ]}))

"""
__version__ = '0.2.0'

import json
import pprint


def validate_mongodb_json(schema, filename):
    """
    validates the given file of multiple json documents to given json schema
    (which was exported by MongoDB)

    in case of non-conformance a schema.SchemaError is thrown.
    """
    with open(filename) as file_:
        for doc in file_:
            data = json.loads(doc)
            schema.validate(data)
    return True


def validate_verbose(rules, item, print_success=False):
    """
    Validate the item to match the schema of at least one schema rule (i.e. OR)

    .. doctest::
        rules = {
                'arecord_record': Schema(arecord_record),
                'map_record': Schema(map_record),
                'presentation_record': Schema(presentation_record),
                'notation_record': Schema(notation_record)}
    """
    errors = []
    for rule_name, rule in rules.items():
        try:
            rule.validate(item)
            if print_success:
                print 'OK:', item
            break
        except SchemaError as err:
            errors.append(('rule %s failed:' % rule_name, err))
    else:
        print 'can not validate the record:'
        pprint.pprint(item)
        pprint.pprint(errors)
        return False
    return True


def validate_file_verbose(rules, filename):
    """
    Validate the file composed of json documents to match the given rules;
    see validate_verbose() for details.
    """
    with open(filename) as file_:
        for line in file_:
            doc = json.loads(line)
            if not validate_verbose(rules, doc):
                return False
    return True


# original version below

class SchemaError(Exception):

    """Error during Schema validation."""

    def __init__(self, autos, errors):
        self.autos = autos if type(autos) is list else [autos]
        self.errors = errors if type(errors) is list else [errors]
        Exception.__init__(self, self.code)

    @property
    def code(self):
        def uniq(seq):
            seen = set()
            seen_add = seen.add
            return [x for x in seq if x not in seen and not seen_add(x)]
        a = uniq(i for i in self.autos if i is not None)
        e = uniq(i for i in self.errors if i is not None)
        if e:
            return '\n'.join(e)
        return '\n'.join(a)


class And(object):

    def __init__(self, *args, **kw):
        self._args = args
        assert list(kw) in (['error'], [])
        self._error = kw.get('error')

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__,
                           ', '.join(repr(a) for a in self._args))

    def validate(self, data):
        for s in [Schema(s, error=self._error) for s in self._args]:
            data = s.validate(data)
        return data


class Or(And):

    def validate(self, data):
        x = SchemaError([], [])
        for s in [Schema(s, error=self._error) for s in self._args]:
            try:
                return s.validate(data)
            except SchemaError as _x:
                x = _x
        raise SchemaError(['%r did not validate %r' % (self, data)] + x.autos,
                         [self._error] + x.errors)


class Use(object):

    def __init__(self, callable_, error=None):
        assert callable(callable_)
        self._callable = callable_
        self._error = error

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._callable)

    def validate(self, data):
        try:
            return self._callable(data)
        except SchemaError as x:
            raise SchemaError([None] + x.autos, [self._error] + x.errors)
        except BaseException as x:
            f = self._callable.__name__
            raise SchemaError('%s(%r) raised %r' % (f, data, x), self._error)


def priority(s):
    if type(s) in (list, tuple, set, frozenset):
        return 6
    if type(s) is dict:
        return 5
    if hasattr(s, 'validate'):
        return 4
    if type(s) is type:
        return 3
    if callable(s):
        return 2
    else:
        return 1


class Schema(object):

    def __init__(self, schema, error=None):
        self._schema = schema
        self._error = error

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._schema)

    def validate(self, data):
        s = self._schema
        e = self._error
        if type(s) in (list, tuple, set, frozenset):
            data = Schema(type(s), error=e).validate(data)
            return type(s)(Or(*s, error=e).validate(d) for d in data)
        if type(s) is dict:
            data = Schema(dict, error=e).validate(data)
            new = type(data)()  # new - is a dict of the validated values
            x = None
            coverage = set()  # non-optional schema keys that were matched
            # for each key and value find a schema entry matching them, if any
            for key, value in data.items():
                valid = False
                skey = None
                for skey in sorted(s, key=priority):
                    svalue = s[skey]
                    try:
                        nkey = Schema(skey, error=e).validate(key)
                        try:
                            nvalue = Schema(svalue, error=e).validate(value)
                        except SchemaError as _x:
                            x = _x
                            raise
                    except SchemaError:
                        pass
                    else:
                        coverage.add(skey)
                        valid = True
                        break
                if valid:
                    new[nkey] = nvalue
                elif skey is not None:
                    if x is not None:
                        raise SchemaError(['invalid value for key %r' % key] +
                                          x.autos, [e] + x.errors)
            coverage = set(k for k in coverage if type(k) is not Optional)
            required = set(k for k in s if type(k) is not Optional)
            if coverage != required:
                raise SchemaError('missed keys %r' % (required - coverage), e)
            if len(new) != len(data):
                wrong_keys = set(data.keys()) - set(new.keys())
                s_wrong_keys = ', '.join('%r' % k for k in sorted(wrong_keys))
                raise SchemaError('wrong keys %s in %r' % (s_wrong_keys, data),
                                  e)
            return new
        if hasattr(s, 'validate'):
            try:
                return s.validate(data)
            except SchemaError as x:
                raise SchemaError([None] + x.autos, [e] + x.errors)
            except BaseException as x:
                raise SchemaError('%r.validate(%r) raised %r' % (s, data, x),
                                 self._error)
        if type(s) is type:
            if isinstance(data, s):
                return data
            else:
                raise SchemaError('%r should be instance of %r' % (data, s), e)
        if callable(s):
            f = s.__name__
            try:
                if s(data):
                    return data
            except SchemaError as x:
                raise SchemaError([None] + x.autos, [e] + x.errors)
            except BaseException as x:
                raise SchemaError('%s(%r) raised %r' % (f, data, x),
                                  self._error)
            raise SchemaError('%s(%r) should evaluate to True' % (f, data), e)
        if s == data:
            return data
        else:
            raise SchemaError('%r does not match %r' % (s, data), e)


class Optional(Schema):

    """Marker for an optional part of Schema."""