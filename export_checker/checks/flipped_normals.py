from export_checker.base_check import BaseCheck

class FlippedNormalsCheck(BaseCheck):

    name = "法線の反転"
    category = "メッシュ"
    severity = "error"
    description = "メッシュの法線が反転しています。"
    can_fix = True

    def check(self, targets):
        pass