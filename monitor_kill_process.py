import os

import psutil as ps


def shutdown(pid, **kwargs):
    if ps.pid_exists(pid) and pid != os.getpid():
        process = ps.Process(pid)
        exe = process.exe()
        # check cpu and memory uss
        if (0.0 < kwargs["cpu"] <= process.cpu_percent(interval=None)) or (
                0 < kwargs["memory"] <= process.memory_full_info().uss):
            process.kill()
            process.wait()
            return True, exe
        else:
            return False, exe


def startup(shell):
    os.system(shell)


def find_process(name):
    # the list the contain process dictionaries
    return [p.info for p in ps.process_iter(attrs=['pid', 'name']) if name in p.info['name']]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Kill process by cpu or memory")
    parser.add_argument("-p", "--process",
                        help="Find process name")
    parser.add_argument("-m", "--memory",
                        help="Memory limit in bytes to restart java service, example 15028224", default=0)
    parser.add_argument("-u", "--cpu",
                        help="CPU Usage limit to restart java service, example 0.5",
                        default=0.0)

    # parse arguments
    args = parser.parse_args()
    process_name = args.process
    cpu = float(args.cpu)
    memory = int(args.memory)

    if process_name is not None:
        for p in find_process(process_name):
            # analyze the shutdown of the process
            dead, process_exe = shutdown(p['pid'], cpu=cpu, memory=memory)
            if dead:
                # the startup of the process
                startup(process_exe)
