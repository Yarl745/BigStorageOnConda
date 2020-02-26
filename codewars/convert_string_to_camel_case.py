def to_camel_case(text):
    text = text.replace('-', '_')
    return "".join([word if not text.find(word, 0, len(word)) else word.capitalize() for word in text.split('_')])


print(to_camel_case("the-stealth-warrior"))