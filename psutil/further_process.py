import psutil

for proc in psutil.process_iter(attrs=['pid', 'name']):
    print(proc.info)

print(psutil.pid_exists(3))


def on_terminate(proc):
    print("process {} terminated".format(proc))


# waits for multiple processes to terminate
gone, alive = psutil.wait_procs(procs_list, timeout=3, callback=on_terminate)

from subprocess import PIPE

p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
print(p.name())
print(p.username())
print(p.communicate())
print(p.wait(timeout=2))
