import subprocess

def get_all_states():
    cmd = ["wsl", "--list", "--verbose"]
    stdout = subprocess.run(cmd, capture_output=True).stdout.decode("utf-16-le")
    info_list = [x.strip().split()[-3:] for x in stdout.strip().split("\r\n")][1:]
    info = {x[0]: {"state": x[1], "version": x[2]} for x in info_list}
    return info


def get_state(distro_name):
    info = get_all_states()
    return info[distro_name]["state"]


def start_distro(distro_name):
    cmd = f"wsl --distribution {distro_name}"
    return subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)


def terminate_distro(distro_name):
    cmd = ["wsl", "--terminate", distro_name]
    return subprocess.run(cmd)


def toggle_state(distro_name):
    state = get_state(distro_name)
    if state == "Stopped":
        return start_distro(distro_name)
    elif state == "Running":
        return terminate_distro(distro_name)
    
    return None


def terminate_all(*args):
    info = get_all_states()
    for distro_name, i in info.items():
        if i["state"] != "Stopped":
            terminate_distro(distro_name)


def shutdown_all(*args):
    cmd = ["wsl", "--shutdown"]
    return subprocess.run(cmd)
