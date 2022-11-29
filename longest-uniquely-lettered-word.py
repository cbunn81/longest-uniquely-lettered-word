def main() -> None:
    # Set a var to hold the current longest word
    current_longest_word = ""

    # Read file, line by line (aka word by word)
    with open("words.txt") as f:
        for word in f:
            unique_letters = set(word)
            if len(word) == len(unique_letters) and len(word) > len(
                current_longest_word
            ):
                print(f"New longest word found: {word} ({len(word)} letters)")
                current_longest_word = word


if __name__ == "__main__":
    main()
