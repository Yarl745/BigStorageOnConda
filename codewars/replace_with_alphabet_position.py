def alphabet_position(text):
    return " ".join([str(ord(let) - 96) for let in text.lower() if let.isalpha()])


print(alphabet_position("The sunset sets at twelve o' clock."))
