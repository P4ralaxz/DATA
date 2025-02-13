import json
def insertionSort(list, last):
    current = 1
    comparison_count = 0
    while current <= last:
        hold = list[current]
        walker = current - 1
        c = 0
        if walker >= 0 and hold > list[walker]:
                comparison_count += 1
        while walker >= 0 and hold < list[walker]:
            list[walker + 1] = list[walker]
            walker -= 1
            comparison_count += 1
            c += 1
            
            
            if walker >= 0 and hold > list[walker]:
                comparison_count += 1
        list[walker + 1] = hold
        current += 1

        print(list)
    print(f"Comparison times: {comparison_count}")




insertionSort(json.loads(input()), int(input()))
