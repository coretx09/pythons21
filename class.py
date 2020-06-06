class Droite:
    """
    la class droite a 3 attributs (self.x, y, nom)
     et 2 methodes : tracer(), deplace()  
    """
    nombre_Droite = 0   #attribut de classe

    def __init__(self, abs, ord, nomDroite):   # constructeur
        """ Constructeur de notre classe. Chaque attribut va être instancié
                avec une valeur par défaut... original"""
        self.x = abs    #abscisse
        self.y = ord    #ordonne
        self.nom = nomDroite  # nom de la droite
        Droite.nombre_Droite += 1   #  calcule le nombre de droite creer

    def tracer(self):  # methode pour tracer
        print(f"les coordonnees de la droite {self.nom} : ")
        print(f"  X = {self.x}    et   Y = {self.y}")

    def deplace(self, dx, dy):  # methode pour deplacer
        """
        :param dx: nombre de point de x a deplacer
        :param dy: nombre de point de y a deplacer
        :return: deplace la ligne
        """
        self.x += dx
        self.y += dy

    @classmethod
    def get_nombre_Droite(cls):  # method de class , affiche le nombre de droite creer
        return print(f"nombre de droite {Droite.nombre_Droite}")

# programme principal

droite1 = Droite(8, 3, " de l'eclipse")  # droite1 instance de class Droite
droite1.tracer()
droite1.deplace(-2, 3)
droite1.tracer()

droite2 = Droite(3, 0.8, "perpondiculaire")
droite2.tracer()

Droite.get_nombre_Droite()  # appel methode de class qui affiche le nombre de droite creer