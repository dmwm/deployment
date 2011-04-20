# DAS analytics web server configuration
log_to_stdout = 0
log_to_file = 0
web_history = 10000
minimum_interval = 60
log_format = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
max_retries = 1
retry_delay = 60
no_start_offset = False
web = True
web_port = 8213
global_das = False
logfile_mode = "None"
workers = 4
log_to_stderr = 0
web_base = "/analytics"
pid = '{ROOT}/state/das/das_analytics.pid'

# DAS analytics tasks
Task("DatasetHotspot", "ValueHotspot", 3600, key="dataset.name")
Task("BlockHotspot", "ValueHotspot", 3600, key="block.name")
Task("FileHotspot", "ValueHotspot", 3600, key="file.name")
Task("SiteHotspot", "ValueHotspot", 3600, key="site.name")
Task("RunHotspot", "ValueHotspot", 3600, key="run.run_number")
