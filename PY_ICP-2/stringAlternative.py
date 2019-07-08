def string_alternative(message):
    return message[::2]


if __name__ == '__main__':
    message = input("Enter a message : ")
    alternative_message = string_alternative(message)
    print("Alternative characters in message : " + alternative_message)
