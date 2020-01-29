import psutil

print(psutil.net_io_counters(pernic=True))
print(psutil.net_connections())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())
