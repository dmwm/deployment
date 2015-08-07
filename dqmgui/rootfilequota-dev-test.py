# Quota for root files on the Dev test server.
# Historically this was merely ~1G per type, which meant data was deleted very
# quickly.
# Considering that most of the testing happens with offline files, we reserve
# the biggest chunk of data for offline data.
{'online_data':      20 * 1024 ** 3,
 'offline_data':    200 * 1024 ** 3,
 'relval_data':      20 * 1024 ** 3,
 'relval_mc':        20 * 1024 ** 3,
 'relval_rundepmc':  20 * 1024 ** 3,
 'simulated_rundep':  5 * 1024 ** 3,
 'simulated':         5 * 1024 ** 3,
}

