import paramiko

from Utility.custom_log import Log1


class MachinePerformance:

    logg = Log1.log1()

    def connect_machine(self, hostname,username,password):
        try:
            global client
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.connect(hostname, port=22, username=username,password=password)
            (stdin, stdout, stderr) = client.exec_command('free -m | awk \'NR==2{printf "%.2f%%", $3*100/$2 }\'')

        except Exception as e:
            self.logg.info(e)





    def get_memory(self, hostname,username,password):
        try:
            # client = paramiko.SSHClient()
            # client.load_system_host_keys()
            # client.connect(hostname, port=22, username=username,password=password)
            (stdin, stdout, stderr) = client.exec_command('free -m | awk \'NR==2{printf "%.2f%%", $3*100/$2 }\'')

            cmd_output = stdout.read()
            memorystr = str(cmd_output).split("'")
            # we are returning the output
            return memorystr[1][:-1]
        finally:
            client.close()

    def getusage(self, hostname,username,password):
        try:
            # client = paramiko.SSHClient()
            # client.load_system_host_keys()
            # client.connect(hostname, port=22, username=username, password=password)
            (stdin, stdout, stderr) = client.exec_command('df -h | awk \'$NF=="/"{printf "%s", $5}\'')
            cmd_output = stdout.read()
            memorystr = str(cmd_output).split("'")
            # we are returning the output
            return memorystr[1][:-1]
        finally:
            client.close()

    def getCpu(self, hostname, username, password):
        try:
            # client = paramiko.SSHClient()
            # client.load_system_host_keys()
            # client.connect(hostname, port=22, username=username, password=password)
            (stdin, stdout, stderr) = client.exec_command('top -bn1 | grep load | awk \'{printf "%.2f%%", $(NF-2)}\'')

            cmd_output = stdout.read()
            memorystr = str(cmd_output).split("'")
            # we are returning the output
            return memorystr[1][:-1]
        finally:
            client.close()

    def testMemory(self,hostname,username,password):
        self.connect_machine(hostname,username,password)
        machinmemory = self.get_memory(hostname,username,password)
        machinmemory = float(machinmemory)
        print(machinmemory)
        if machinmemory == 0:
            self.logg.info("Memory is showing 0 % Usage ")
            assert False
        elif machinmemory > 90.00:
            self.logg.info("Test case Failed Due to current Memory usage is " + str(machinmemory) +"%")
            assert False
        else:
            self.logg.info("current Memory usage is " + str(machinmemory) + "%")
            assert True

    def testUsage(self,hostname,username,password):
        self.connect_machine(hostname, username, password)
        usage= self.getusage(hostname,username,password)
        usage = float(usage)
        print(usage)
        if usage == 0:
            self.logg.info("Disk usage  is showing 0 % ")
            assert False
        elif usage > 90.00:
            self.logg.info("Test case Failed Due to Disk usage is " + str(usage) + "%")
            assert False
        else:
            self.logg.info("current Disk usage is " + str(usage) + "%")
            assert True

    def testCpu(self,hostname,username,password):
        self.connect_machine(hostname, username, password)
        usage= self.getCpu(hostname,username,password)
        usage = float(usage)
        print(usage)
        if usage == 0:
            self.logg.info("Disk usage  is showing 0 % ")
            assert False
        elif usage > 90.00:
            self.logg.info("Test case Failed Due to CPU usage is " + str(usage) + "%")
            assert False
        else:
            self.logg.info("current CPU  usage is " + str(usage) + "%")
            assert True


