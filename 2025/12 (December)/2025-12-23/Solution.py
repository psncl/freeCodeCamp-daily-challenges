import re

def email_chain_count(subject: str) -> int:

    pattern = r"\b(re|fwd?):"
    matches = re.findall(pattern, subject, re.IGNORECASE)
    return len(matches)
    
## Tests

assert email_chain_count("Re: Meeting Notes") == 1
assert email_chain_count("Meeting Notes") == 0
assert email_chain_count("Re: re: RE: rE: Meeting Notes") == 4
assert email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes") == 5
assert email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary") == 23