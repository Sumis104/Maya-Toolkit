class BaseCheck:

    name = ""
    category = ""
    severity = "error"
    description = ""
    can_fix = False

    def check(self, targets):
        raise NotImplementedError("checkが実装されていません。")

    def fix(self, issues):
        raise NotImplementedError("fixが実装されていません。")