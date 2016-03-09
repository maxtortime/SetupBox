class vcs_wrapper:
    def init(self):
        pass

    def checkout(self, url, dest, username=None, password=None):
        pass

    def add(self, targets, username=None, password=None):
        pass

    def rm(self, targets, username=None, password=None):
        pass

    def commit(self, msg, username=None, password=None):
        pass

    def push(self):
        pass

    def update(self, username=None, password=None):
        pass

    def revert(self):
        pass

    def do_command(self, command, parameters=[], username=None, password=None):
        pass