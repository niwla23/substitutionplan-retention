from prometheus_client import Summary

# Create a metric to track time spent and requests made.
DOWNLOAD_TIME = Summary(
    'iserv_download_time',
    'Time spent downloading files from iserv',
    ['operation']
)

DOWNLOAD_SIZE = Summary(
    'iserv_download_size',
    'Size of a downloaded files in bytes',
    ['operation']
)
