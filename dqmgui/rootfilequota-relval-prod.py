# Quota for root files on the Relval production server.
# Note that all this data is backed up to Castor upon receipt.
{'online_data':        50 * 1024 ** 3,
 'offline_data':       50 * 1024 ** 3,
 'relval_data':      2000 * 1024 ** 3,
 'relval_mc':        1000 * 1024 ** 3,
 'relval_rundepmc':  1000 * 1024 ** 3,
 'simulated':        1000 * 1024 ** 3,
 'simulated_rundep': 1000 * 1024 ** 3,
}
