from prometheus_client import Summary, Gauge

# Create a metric to track time spent and requests made.
DOWNLOAD_TIME = Gauge(
    'iserv_download_time',
    'Time spent downloading files from iserv',
    ['operation']
)

DOWNLOAD_SIZE = Gauge(
    'iserv_download_size',
    'Size of a downloaded files in bytes',
    ['operation']
)


LAST_DOWNLOAD_TIME = Gauge(
    'iserv_last_download_time',
    'Time in UNIX timestamp of last download'
)
