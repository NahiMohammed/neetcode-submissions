class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        for email in emails :
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")

            normalized = local + "@" + domain
            s.add(normalized)
        return len(s)
        