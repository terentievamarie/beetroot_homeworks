def stop_words(words):
    def decorator(func):
        def wrapper(sentence):
            words_list = sentence.split()
            new_words = [word if word.lower() not in words else '*' for word in words_list]
            return func(' '.join(new_words))
        return wrapper
    return decorator

@stop_words(['summer', 'winter'])
def create_slogan(sentence):
    return sentence

result = create_slogan("Mary likes summer not winter")
print(result)

