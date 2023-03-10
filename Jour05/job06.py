def arr_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        else:
            multiple_5 = ((note + 4) // 5) * 5
            if multiple_5 - note < 3:
                arrondies.append(multiple_5)
            else:
                arrondies.append(note)
    return arrondies

notes = [83, 43, 6, 93, 78]
print(arr_notes(notes))