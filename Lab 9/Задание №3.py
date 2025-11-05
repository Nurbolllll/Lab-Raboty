def sort_words(words):
    if len(words) <= 1:
        return words
    pivot = words[0]
    smaller = [w for w in words[1:] if w.lower() < pivot.lower()]
    larger = [w for w in words[1:] if w.lower() >= pivot.lower()]
    return sort_words(smaller) + [pivot] + sort_words(larger)
word_list = ["Яблоко", "груша", "апельсин", "вишня", "банан"]
sorted_words = sort_words(word_list)
print("Исходный список:", word_list)
print("Отсортированный список:", sorted_words)

