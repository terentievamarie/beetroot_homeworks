def in_range(start, end, step=1):
    current_value = start

    # виконується поки стартове значення менше кінцевого, крок більше нуля,
    # інакше - виконується поки стартове значення більше кінцевого
    while (current_value < end) if step > 0 else (current_value > end):
        yield current_value
        current_value += step

for i in in_range(5, 1, -1):
    print(i)