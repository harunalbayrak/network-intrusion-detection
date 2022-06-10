from datetime import datetime
from colorama import Fore, Style

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    def __init__(self, module):
        self.module = module
        self.debug = 0
        
    def print_log_debug(self, log):
        if(self.debug == 1):
            self.print_log(log,"DEBUG", Fore.GREEN)
        else:
            self.write_log_to_file(log,"DEBUG")

    def print_log_info(self, log):
        if(self.debug == 1):
            self.print_log(log,"INFO", Fore.CYAN)
        else:
            self.write_log_to_file(log,"INFO")

    def print_log_warning(self, log):
        if(self.debug == 1):
            self.print_log(log,"WARNING", Fore.YELLOW)
        else:
            self.write_log_to_file(log,"WARNING")

    def print_log_error(self, log):
        if(self.debug == 1):
            self.print_log(log,"ERROR", Fore.LIGHTRED_EX)
        else:
            self.write_log_to_file(log,"ERROR")

    def print_log(self, log, status, color):
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")

        if self.module == 'DATABASE':
            print(f"[DATABASE Module - {color}{status}{Style.RESET_ALL} - {currentTime}] {log}")
        elif self.module == 'DETECTION':
            print(f"[DETECTION Module - {color}{status}{Style.RESET_ALL} - {currentTime}] {log}")
        elif self.module == 'GUI':
            print(f"[GUI Module - {color}{status}{Style.RESET_ALL} - {currentTime}] {log}")
        elif self.module == 'PACKETCAPTURE':
            print(f"[PACKETCAPTURE Module - {color}{status}{Style.RESET_ALL} - {currentTime}] {log}")
        elif self.module == 'RULEPARSER':
            print(f"[RULEPARSER Module - {color}{status}{Style.RESET_ALL} - {currentTime}] {log}")
        else:
            print(f"[UNKNOWN Module - {color}{status}{Style.RESET_ALL} - {currentTime}] {log}")

    def write_log_to_file(self, log, status):
        self.logfile = open("logs.txt", "a")
        
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")

        if self.module == 'DATABASE':
            self.logfile.write(f"[DATABASE Module - {status} - {currentTime}] {log}\n")
        elif self.module == 'DETECTION':
            self.logfile.write(f"[DETECTION Module - {status} - {currentTime}] {log}\n")
        elif self.module == 'GUI':
            self.logfile.write(f"[GUI Module - {status} - {currentTime}] {log}\n")
        elif self.module == 'PACKETCAPTURE':
            self.logfile.write(f"[PACKETCAPTURE Module - {status} - {currentTime}] {log}\n")
        elif self.module == 'RULEPARSER':
            self.logfile.write(f"[RULEPARSER Module - {status} - {currentTime}] {log}\n")
        else:
            self.logfile.write(f"[UNKNOWN Module - {status} - {currentTime}] {log}\n")

        self.logfile.close()