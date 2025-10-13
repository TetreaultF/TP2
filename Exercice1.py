"""
TP2 - Exercice 1 : Gestion du Menu
"""

def analyser_menu(menu):
    """
    Analyse le menu du restaurant pour extraire des statistiques importantes.
    
    Args:
        menu (dict): Dictionnaire avec nom_plat: (prix, temps_preparation, popularité)
    
    Returns:
        dict: Dictionnaire contenant:
            - 'plat_plus_rentable': Le plat avec le meilleur ratio popularité/temps
            - 'prix_moyen': Le prix moyen de tous les plats
            - 'temps_moyen': Le temps de préparation moyen
    """
    stats = {}
    
    # TODO: Calculer le plat le plus rentable (ratio popularité/temps_preparation)
    # Attention: gérer le cas où temps_preparation pourrait être 0
    

    
    meilleur_plat = None
    meilleur_ratio = -1
    prix_total = 0
    temps_total = 0
    
    for plat, (prix, temps_preparation, popularité) in menu.items():
        prix_total += prix
        temps_total += temps_preparation
        ratio = popularité / temps_preparation if temps_preparation > 0 else float("inf")
        if ratio > meilleur_ratio :
            meilleur_ratio = ratio
            meilleur_plat = plat

    # TODO: Calculer le prix moyen du menu
    # TODO: Calculer le temps de préparation moyen
    if len(menu) == 0:
        prix_moyen = 0
        temps_moyen = 0
        meilleur_plat = None
    else:
        prix_moyen = prix_total / len(menu)
        temps_moyen = temps_total / len(menu)

    stats["plat_plus_rentable"] = meilleur_plat
    stats["prix_moyen"] = prix_moyen
    stats["temps_moyen"] = temps_moyen

    return stats


def filtrer_menu_par_categorie(menu, categories):
    """
    Filtre le menu par catégories de plats.
    
    Args:
        menu (dict): Menu complet
        categories (dict): Dictionnaire nom_plat: catégorie
    
    Returns:
        dict: Menu organisé par catégories
    """
    menu_filtre = {}
    
    # TODO: Organiser les plats par catégorie
    # Exemple: {'entrées': [...], 'plats': [...], 'desserts': [...]}
    
    menu_filtre = {"entrées":[], "plats": [], "desserts": []}
    
    for plat, infos in menu.items(): 
        categorie = categories.get(plat,False)
        if categorie in menu_filtre:
            menu_filtre[categorie].append((plat,infos))
        else:
            menu_filtre[categorie] = []
    
    return menu_filtre

def calculer_profit(menu, ventes_jour):
    """
    Calcule le profit total de la journée.
    
    Args:
        menu (dict): Menu avec prix
        ventes_jour (dict): Nombre de ventes par plat
    
    Returns:
        float: Profit total
    """
    profit = 0
    
    # TODO: Calculer le profit total
    # profit = somme(prix_plat * nombre_ventes) pour chaque plat vendu
    for plat in ventes_jour:
        if plat in menu:
            prix_plat = menu[plat][0]
            nombre_ventes = ventes_jour.get(plat,0)
            profit += (prix_plat * nombre_ventes)
    return profit


if __name__ == '__main__':
    # Test de la fonction analyser_menu
    menu_test = {
        'Pizza Margherita': (12.50, 15, 8),
        'Pâtes Carbonara': (14.00, 12, 9),
        'Salade César': (9.50, 5, 6),
        'Tiramisu': (6.00, 3, 10),
        'Burger Classique': (11.00, 10, 7),
        'Soupe du jour': (5.50, 8, 5)
    }
    
    resultats = analyser_menu(menu_test)
    print("Analyse du menu:")
    print(f"  Plat le plus rentable: {resultats.get('plat_plus_rentable')}")
    print(f"  Prix moyen: {resultats.get('prix_moyen'):.2f}€")
    print(f"  Temps de préparation moyen: {resultats.get('temps_moyen'):.1f} min")
    
    # Test de la fonction filtrer_menu_par_categorie
    categories_test = {
        'Pizza Margherita': 'plats',
        'Pâtes Carbonara': 'plats',
        'Salade César': 'entrées',
        'Tiramisu': 'desserts',
        'Burger Classique': 'plats',
        'Soupe du jour': 'entrées'
    }
    
    menu_filtre = filtrer_menu_par_categorie(menu_test, categories_test)
    print("\nMenu par catégories:")
    for categorie, plats in menu_filtre.items():
        print(f"  {categorie}: {plats}")
    
    # Test de la fonction calculer_profit
    ventes_test = {
        'Pizza Margherita': 15,
        'Pâtes Carbonara': 20,
        'Salade César': 10,
        'Tiramisu': 25
    }
    
    profit_jour = calculer_profit(menu_test, ventes_test)
    print(f"\nProfit du jour: {profit_jour:.2f}€")
