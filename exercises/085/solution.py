# Exercice 1
# Trier une liste dans l'ordre décroissant
def sort_a_list(l):
    new_list = l[:]
    ok = False # pour pouvoir entrer dans la boucle
    while(ok!=True): # tant qu'on a encore des réarrangements à faire
        ok = True
        # on parcourt la liste de l'arrière vers l'avant
        for i in reversed(range(1,len(l))):
            # s'il y a un dérangement
            if(new_list[i-1]<new_list[i]):
                # on permute
                temp = new_list[i-1]
                new_list[i-1] = new_list[i]
                new_list[i] = temp
                # on se souvient qu'il y a eu une permutation
                ok = False
    # quand on sort de la boucle, new_list est triée
    return new_list


