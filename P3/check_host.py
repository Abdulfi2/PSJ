import platform as p
import subprocess as sub
import sys

def checkping(host):
    systemOs = '-n' if p.system().lower() == 'windows' else '-c'
    pinging = ['ping', systemOs, '1', host]
    status = ''

    if sub.call(pinging) == 0:
        status = 'UP'
    else:
        status = 'DOWN'

    output = '\nHost {} is {}'.format(host, status)

    return output

ping_def = '192.168.1.1'
response = 'Gagal: IP address belum diberikan\nContoh: check_host.py {}'.format(
    ping_def)

try:
    args = str(sys.argv[1])
    args_len = len(sys.argv[1:])
except IndexError:
    args_len = ''

if not args_len == 1 or args_len == 0:
    sys.exit(response)

finalOutput = checkping(args)

print(finalOutput)