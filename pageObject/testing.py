import paramiko

output_file = 'paramiko.org'
def connect_machine(hostname, username, password):
    print('running')
    try:
        # created client using paramiko
        client = paramiko.SSHClient()

        # here we are loading the system
        # host keys
        client.load_system_host_keys()

        # connecting paramiko using host
        # name and password
        client.connect(hostname, port=22, username=username,
                       password=password)

        # below line command will actually
        # execute in your remote machine
        # (stdin, stdout, stderr) = client.exec_command("free | awk '{print $4}'")

        # (stdin, stdout, stderr) = client.exec_command('df -h | awk \'$NF=="/"{printf "%s", $5}\'')
        (stdin, stdout, stderr) = client.exec_command('free -m | awk \'NR==2{printf "%.2f%%", $3*100/$2 }\'')

        # redirecting all the output in cmd_output
        # variable
        cmd_output = stdout.read()
        memorystr =str(cmd_output).split("'")
        print(memorystr[1][:-1])

        # we are returning the output
        return memorystr[1][:-1]
    finally:
        client.close()

