import subprocess

def execute(command):
    p = subprocess.Popen(
        command, universal_newlines=True, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    if p.returncode != 0:
        errorMsg = '%s %s' % (output, error)
        e = subprocess.CalledProcessError(p.returncode, command)
        e.message += errorMsg
        raise e
    return output