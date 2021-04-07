import os


ADB_ROOT = os.getcwd()
ADB_HOST = "127.0.0.1:7555" # MuMu模拟器
SCREEN_SHOOT_SAVE_PATH = ADB_ROOT + "\\screen_shoot\\"
STORAGE_PATH = ADB_ROOT + "\\storage\\"
RES_PATH = ADB_ROOT + "\\resources\\"



# manlike action
FLAGS_CLICK_BIAS_TINY = (3, 3)


class ShellColor(object):
    def __init__(self):
        self.H_HEADER = '\033[95m'
        self.H_OK_BLUE = '\033[94m'
        self.H_OK_GREEN = '\033[96m'
        self.H_WARNING = '\033[93m'
        self.H_FAIL = '\033[31m'
        self.E_END = '\033[0m'
        self.E_BOLD = '\033[1m'
        self.E_UNDERLINE = '\033[4m'

    def warning_text(self, string):
        print(self.H_WARNING + string + self.E_END)

    def info_text(self, string):
        print(self.H_OK_BLUE + string + self.E_END)

    def failure_text(self, string):
        print(self.H_FAIL + string + self.E_END)

    def helper_text(self, string):
        print(self.H_OK_GREEN + string + self.E_END)

    def run_test(self, string="[*] DEBUG COLOR"):
        self.warning_text(string)
        self.info_text(string)
        self.failure_text(string)
        self.helper_text(string)

# if __name__ == '__main__':
#     ShellColor().run_test()
