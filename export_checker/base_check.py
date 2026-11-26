class BaseCheck:

    name = ""
    category = ""
    severity = "error"
    description = ""
    can_fix = False

    def check(self, targets):
        raise NotImplementedError(f"{type(self).__name__}: check is not implemented.")

    def fix(self, issues):
        raise NotImplementedError(f"{type(self).__name__}: fix is not implemented.")