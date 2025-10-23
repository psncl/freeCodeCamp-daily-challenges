def wise_speak(sentence: str) -> str:

    end_punctuation = sentence[-1]
    all_words = sentence.lower()[0:-1].split(" ")
    wise_phrases = ["have", "must", "are", "will", "can"]

    def capitalize_first(sentence: str) -> str:
        return sentence[0].upper() + sentence[1:]

    def to_sentence_fragment(words: list[str]) -> str:
        return " ".join(words)

    found_indices = [index for index, phrase in enumerate(all_words) if phrase in wise_phrases]
    first_match = found_indices[0]
    first_half = to_sentence_fragment(all_words[(first_match + 1):])
    second_half = to_sentence_fragment(all_words[:(first_match + 1)])
    return f"{capitalize_first(first_half)}, {second_half}{end_punctuation}"

## Tests

assert wise_speak("You must speak wisely.") == "Speak wisely, you must."
assert wise_speak("You can do it!") == "Do it, you can!"
assert wise_speak("Do you think you will complete this?") == "Complete this, do you think you will?"
assert wise_speak("All your base are belong to us.") == "Belong to us, all your base are."
assert wise_speak("You have much to learn.") == "Much to learn, you have."
