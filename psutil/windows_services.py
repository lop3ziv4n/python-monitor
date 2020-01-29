import psutil

print(list(psutil.win_service_iter()))
s = psutil.win_service_get('alg')
print(s.as_dict())
