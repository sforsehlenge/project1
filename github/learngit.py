# This is a simple Python script
def greet(name):
    """
    Greets the person with the given name.

    Parameters:
    - name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the world of coding."

if __name__ == "__main__":
    # Example usage
    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)
