# Quotas used by RootFileQuotaControl on any flavor of the locally setup
# development machine. We don't make a difference between the flavors here,
# since we assume people can mix any kind of data with any kind of server
# flavor.
# We also assume space on local dev machines is limited, allowing max 2 GB per
# kind.
{'online_data':      2 * 1024 ** 3,
 'offline_data':     2 * 1024 ** 3,
 'relval_data':      2 * 1024 ** 3,
 'relval_mc':        2 * 1024 ** 3,
 'relval_rundepmc':  2 * 1024 ** 3,
 'simulated_rundep': 2 * 1024 ** 3,
 'simulated':        2 * 1024 ** 3,
}
