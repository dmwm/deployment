# Quota for root files on the Offline production server.
# Considering that all Online root files are off-loaded to the Offline server,
# we also foresee a considerable amount of space for Online data.
# Note that all this data is backed up to Castor upon receipt.
{'online_data':      1000 * 1024 ** 3,
 'offline_data':     2500 * 1024 ** 3,
 'relval_data':       100 * 1024 ** 3,
 'relval_mc':          70 * 1024 ** 3,
 'relval_rundepmc':    70 * 1024 ** 3,
 'simulated':          10 * 1024 ** 3,
 'simulated_rundep':   10 * 1024 ** 3,
}
