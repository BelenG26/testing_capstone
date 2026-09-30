

def check_answer(user_answer, correct_answer):
    """ Tests if the user's answer is the same as the correct ansert, regardless of case and blanck space before 
    and after the user response. For example, if the answer is "Chicago"
    and "   Chicago   " are both considered correct."""
# remove whitespace 
    if user_answer.strip() == correct_answer:
        return True
    else:
        return False

# informal way for checking
#print(check_answer('Chicago', 'chicago'))