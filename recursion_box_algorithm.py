def find_key(box):
    for item in box:
        if item.is_a_box():
            find_key(item)
        elif item.is_a_key():
            print("Found the key!")