def toilettes(nb_marche, hauteur_marche):
    marche_cm = hauteur_marche / 100
    distance_totale = 2 * nb_marche * hauteur_marche
    distance_daily = distance_totale * 5
    distance_week = distance_daily * 7

    return "Pour {} marches de {} cm, le gardien parcours {:.2f} m par semaine.".format(nb_marche, hauteur_marche, distance_week)

print(toilettes(100, 15))