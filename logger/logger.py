from datetime import datetime

class Logger:
    def __init__(self, module):
        self.module = module
        
    def print_log_debug(self, log):
        self.print_log(log,"DEBUG")

    def print_log_info(self, log):
        self.print_log(log,"INFO")

    def print_log_warning(self, log):
        self.print_log(log,"WARNING")

    def print_log_error(self, log):
        self.print_log(log,"ERROR")

    def print_log(self, log, status):
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")

        if self.module == 'DATABASE':
            print(f"[DATABASE Module - {status} - {currentTime}] - {log}")
        elif self.module == 'DETECTION':
            print(f"[DETECTION Module - {status} - {currentTime}] - {log}")
        elif self.module == 'GUI':
            print(f"[GUI Module - {status} - {currentTime}] - {log}")
        elif self.module == 'PACKETCAPTURE':
            print(f"[PACKETCAPTURE Module - {status} - {currentTime}] - {log}")
        elif self.module == 'RULEPARSER':
            print(f"[RULEPARSER Module - {status} - {currentTime}] - {log}")
        else:
            print(f"[UNKNOWN Module - {status} - {currentTime}] - {log}")