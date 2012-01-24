# DAS analytics web server configuration
log_to_stdout = False
log_to_file = False
log_to_stderr = False
logfile_mode = "None"
web_history = 10000
minimum_interval = 600
log_format = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
max_retries = 1
retry_delay = 60
no_start_offset = False
web = True
web_port = 8213
global_das = False
workers = 4
web_base = "/analytics"
pid = '{ROOT}/state/das/das_analytics.pid'

# options for results.py
db_uri  = "mongodb://localhost:8230/"
db_name = "analytics_results"
db_col  = "db"
db_size = 67108864 # 64MB

# Definitions:
## delta = finish-start (finish = start+period)
## period: the calls to be considered by analytics, default 1h
## allowed_gap: is maximum gap in the summary record we are happy to ignore, default 1h
## interval: interval of the task, suggested value 1h
#
# Production tasks
Task("DatasetHotspot", "ValueHotspot", interval=3600, period=3600, allowed_gap=60, key="dataset.name")
Task("BlockHotspot", "ValueHotspot", interval=3600, period=3600, allowed_gap=60, key="block.name")
Task("FileHotspot", "ValueHotspot", interval=3600, period=3600, allowed_gap=60, key="file.name")
Task("SiteHotspot", "ValueHotspot", interval=3600, period=3600, allowed_gap=60, key="site.name")
Task("RunHotspot", "ValueHotspot", interval=3600, period=3600, allowed_gap=60, key="run.run_number")

# task to clean-up analytics DB, cutoff parameter defines the
# threshold for old records, default is 1 month
Task("CleanUpHotspot", "AnalyticsCleanup", 3600, cutoff=2592000)
