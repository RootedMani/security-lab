from zxcvbn import zxcvbn
from getpass import getpass

def check_password_strength(password):
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
        
if __name__ == "__main__":
    while True:
        password1 = getpass("Enter your password: ")
        print(check_password_strength(password1))