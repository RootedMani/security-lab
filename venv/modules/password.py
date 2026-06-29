from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def check_password_strength(password):
    """ Takes a password and checks if the password is strong enough and gives responses.
    Args:
        password (str): The password that needs to be checked.
    Returns: 
        str: How weak or strong is the password and what is the score of it's 
        security from 0 to 4 and how can it get better and if it was weak, warnings
        about it.
    """
    result = zxcvbn(password)
    score = result["score"]

    if score == 3:
        response = "Strong enough password. Score: 3"
    if score == 4:
        response = "Very strong password. Score: 4"
    else:
        feedback = result.get("feedback")
        warning = feedback.get("warning")
        suggestions = feedback.get("suggestions")

        # Declare the response using the variables created earlier
        response = f"Weak password. Score: {result["score"]}"
        response += f"\nWarning: {warning}"
        response += f"\nSuggestions: {suggestions}"

        for suggestion in suggestions: 
            response += " " + suggestion

    return response
        
def hash_pw(password):
    """ Takes a password and hash it.
    Args:
        password (str): A string representing the password that needs to be hashed
    Returns:
        The hashed equivelant of the password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encrypt(), salt)
    return hashed_password

if __name__ == "__main__":
    while True:
        password1 = getpass("Enter your password: ")
        if check_password_strength(password1).startswith("Weak"):
            print("Please choose a strong password. Try again.")
        else:
            break