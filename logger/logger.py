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
        
    def print_log_debug(self, log):
        self.print_log(log,"DEBUG", Fore.GREEN)

    def print_log_info(self, log):
        self.print_log(log,"INFO", Fore.CYAN)

    def print_log_warning(self, log):
        self.print_log(log,"WARNING", Fore.YELLOW)

    def print_log_error(self, log):
        self.print_log(log,"ERROR", Fore.LIGHTRED_EX)

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