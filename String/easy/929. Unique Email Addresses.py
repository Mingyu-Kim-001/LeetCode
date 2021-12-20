class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        adresses = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".","")
            adresses.add(local+"@"+domain)
        return len(adresses)