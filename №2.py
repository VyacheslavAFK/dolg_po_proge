def count_unique_chars(text):
    return f"Количество уникальных символов - {len(set(''.join(text)))}"


print(count_unique_chars("hello123334455aaadddccc"))
