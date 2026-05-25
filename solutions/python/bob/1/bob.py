def response(hey_bob):
    
    # silence - empty or whitespace only
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    
    is_question = hey_bob.strip().endswith('?')
    is_yelling = hey_bob.upper() == hey_bob and any(c.isalpha() for c in hey_bob)
    
    # yelling a question - check this BEFORE yelling alone
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    # yelling
    if is_yelling:
        return "Whoa, chill out!"
    
    # question
    if is_question:
        return "Sure."
    
    # anything else
    return "Whatever."