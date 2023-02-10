import paramiko

from Utility.custom_log import Log1
from Utility.writeXcel import xlrWrite


class MachinePerformance:
    logg = Log1.log1()
    machineData = []

    def connect_machine(self, hostname, username, password):
        try:
            global client
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.connect(hostname, port=22, username=username, password=password, timeout=5)
            

        except Exception as e:
            self.logg.info(e)

    def get_memory(self):
        try:
            (stdin, stdout, stderr) = client.exec_command('free -m | awk \'NR==2{printf "%.2f%%", $3*100/$2 }\'')

            cmd_output = stdout.read()
            memorystr = str(cmd_output).split("'")
            wr=xlrWrite()
            wr.writememory(memorystr[1][:-1])
            # we are returning the output
            return memorystr[1][:-1]
        finally:
            client.close()

    def getusage(self):
        try:
            (stdin, stdout, stderr) = client.exec_command('df -h | awk \'$NF=="/"{printf "%s", $5}\'')
            cmd_output = stdout.read()

            memorystr = str(cmd_output).split("'")
            MachinePerformance.machineData.append(memorystr)
            wr = xlrWrite()
            wr.writeusage(memorystr[1][:-1])
            # we are returning the output
            return memorystr[1][:-1]
        finally:
            client.close()

    def getCpu(self):
        try:
            (stdin, stdout, stderr) = client.exec_command('top -bn1 | grep load | awk \'{printf "%.2f%%", $(NF-2)}\'')

            cmd_output = stdout.read()
            memorystr = str(cmd_output).split("'")
            wr = xlrWrite()
            wr.writecpu(memorystr[1][:-1])
            # we are returning the output
            return memorystr[1][:-1]
        finally:
            client.close()

    def testMemory(self, hostname, username, password):
        self.connect_machine(hostname, username, password)
        machinmemory = self.get_memory()
        machinmemory = float(machinmemory)
        print(machinmemory)
        if machinmemory == 0:
            self.logg.info("Memory is showing 0 % Usage ")
            print("Memory is showing 0 % Usage ")
            assert False
        elif machinmemory > 90.00:
            self.logg.info("Test case Failed Due to current Memory usage is " + str(machinmemory) + "%")
            print("Test case Failed Due to current Memory usage is " + str(machinmemory) + "%")
            assert False
        else:
            self.logg.info("current Memory usage is " + str(machinmemory) + "%")
            print("current Memory usage is " + str(machinmemory) + "%")
            assert True

    def testUsage(self, hostname, username, password):
        self.connect_machine(hostname, username, password)
        usage = self.getusage()
        usage = float(usage)
        print(usage)
        if usage == 0:
            self.logg.info("Disk usage  is showing 0 % ")
            print("Disk usage  is showing 0 % ")
            assert False
        elif usage > 90.00:
            self.logg.info("Test case Failed Due to Disk usage is " + str(usage) + "%")
            print("Test case Failed Due to Disk usage is " + str(usage) + "%")
            assert False
        else:
            self.logg.info("current Disk usage is " + str(usage) + "%")
            print("current Disk usage is " + str(usage) + "%")
            assert True

    def testCpu(self, hostname, username, password):
        self.connect_machine(hostname, username, password)
        usage = self.getCpu()
        usage = float(usage)
        print(usage)
        if usage == 0:
            self.logg.info("CPU  usage  is showing 0 % ")
            print("CPU  usage  is showing 0 % ")
            assert False
        elif usage > 90.00:
            self.logg.info("Test case Failed Due to CPU usage is " + str(usage) + "%")
            print("Test case Failed Due to CPU usage is " + str(usage) + "%")
            assert False
        else:
            self.logg.info("current CPU  usage is " + str(usage) + "%")
            print("current CPU  usage is " + str(usage) + "%")
            assert True
