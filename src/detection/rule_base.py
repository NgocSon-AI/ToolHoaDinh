import re

class RuleDetector:
    """
    Detects suspicious content based on keywords and regex rules.
    """
    def __init__(self, keywords, regex_rules):
        self.keywords = [kw.lower() for lang in keywords.values() for kw in lang if kw]
        self.regex_rules = regex_rules
    
    def detect(self, text):
        findinds = []

        # keyword-based detection

        for kw in self.keywords:
            if kw in text.lower():
                findinds.append(f"Keyword matched: {kw}")
        
        # Regex-based detection
        for rule_name, pattern in self.regex_rules.items():
            matches = re.findall(pattern, text)
            if matches:
                findinds.append(f"{rule_name} found: {matches[:3]}...") #limit output

            return findinds