def test_list(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarin et kiwi")
    elif type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "fruits" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("error 404 fruits/legumes not found")

test_list("fruits", "hiver")