class Solution:
    import re

    def validIPv4(self, segments):
        pattern = "(\A1[0-9][0-9]\Z)|(\A25[0-5]\Z)|(\A2[0-4][0-9]\Z)|(\A[1-9]?[0-9]\Z)"
        for segment in segments:
            if re.search(pattern, segment) is None:
                return False

        return True

    def validIPv6(self, segments):
        # Valid digit is an Hex digit. Might contain leading zeros
        pattern = "(\A[A-Fa-f0-9]?[A-Fa-f0-9]?[A-Fa-f0-9]?[A-Fa-f0-9]\Z)"

        for segment in segments:    
            if re.search(pattern, segment) is None:
                return False

        return True

    def validIPAddress(self, IP: str) -> str:

        segments = IP.split(".")
        if len(segments) == 4 and self.validIPv4(segments):
            return "IPv4"
        
        segments = IP.split(":")
        if len(segments) == 8 and self.validIPv6(segments):
            return "IPv6"
            
        return "Neither"