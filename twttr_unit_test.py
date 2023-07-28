def main():
    words = input("Enter any word you like : ")
    new_word = shorten(words)
    print(f"The new word is {new_word}")


def shorten(words):
    for word in words:
        if word in 'aeiou':
            words = words.replace(word,'')
    return words


if __name__ == '__main__':
    main()