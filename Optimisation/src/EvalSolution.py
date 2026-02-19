from opti_boxes import Box, Child

class EvalSolution:

    def __init__(self):
        self.score : int = 0

    def evaluate(self, solution : list[Box]) -> int:
        if not self.r1(solution) or not self.r2(solution) or not self.r3(solution):
            return -9999

        self.r4(solution)
        self.r5(solution)
        self.r6(solution)
        self.r7(solution)
        self.r8(solution)
        return self.score

    def r1(self, solution : list[Box]) -> bool:
        """
        Unicité des articles
        Chaque article ne peut apparaître que dans une seule box
        au plus. Tous les articles ne sont pas forcément utilisés.
        :param solution: La solution proposée
        :return: True si la solution est valide, False sinon
        """
        duplicates = set()
        for box in solution:
            for toy in box.toys:
                if toy in duplicates:
                    return False
                duplicates.add(toy)

        return True

    def r2(self, solution : list[Box]) -> bool:
        """
        Compatibilité d’âge
        Un article ne peut être placé dans la box d’un abonné que si
        la tranche d’âge de l’article correspond exactement à la tranche d’âge de l’enfant de
        l’abonné. Par exemple, un article étiqueté PE (3-6 ans) ne peut être affecté qu’à un abonné
        ayant déclaré un enfant dans la tranche PE.
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        for box in solution:
            for toy in box.toys:
                if not box.childBelonging.belongsToAge(toy.age):
                    return False

        return True

    def r3(self, solution : list[Box]) -> bool:
        """
        Poids limité
        Le poids total des articles contenus dans une box ne doit pas
        dépasser le poids maximum Wmax défini pour la campagne.
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        for box in solution:
            if box.totalMass > box.maximumMass:
                return False

        return True

    def r4(self, solution : list[Box]) -> None:
        """
        Gain par préférence de catégorie
        chaque article placé dans la box d’un abonné
        rapporte un certain nombre de points au score global. Ce nombre de points dépend de la
        position de la catégorie de l’article dans l’ordre de préférence de l’abonné
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        for box in solution:
            for toy in box.toys:
                try:
                    index = box.childBelonging.preferences.index(toy.category)
                    match index:
                        case 0: self.score += 10
                        case 1: self.score += 8
                        case 2: self.score += 6
                        case 3: self.score += 4
                        case 4: self.score += 2
                        case 5: self.score += 1
                        case _: continue
                except ValueError:
                    continue

    def r5(self, solution : list[Box]) -> None:
        """
        Bonus d’état
        en plus des points de préférence, chaque article apporte un bonus lié à son état
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        for box in solution:
            for toy in box.toys:
                match toy.state:
                    case "N": self.score += 2
                    case "TB": self.score += 1
                    case _: continue


    def r6(self, solution : list[Box]) -> None:
        """
        Utilités dégressives
        Pour encourager la variété dans les box, si plusieurs
        articles de la même catégorie sont placés dans une même box, les points diminuent pour
        chaque article supplémentaire de cette catégorie.
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        count_category = {
            "SOC": 0,
            "FIG": 0,
            "CON": 0,
            "EXT": 0,
            "EVL": 0,
            "LIV": 0
        }
        for box in solution:
            count_category.clear()
            for toy in box.toys:
                count_category[toy.category] += 1

            for cat, count in count_category.items():
                if count > 1:
                    index = box.childBelonging.preferences.index(cat) + count - 1
                    match index:
                        case 1: self.score += 8
                        case 2: self.score += 6
                        case 3: self.score += 4
                        case 4: self.score += 2
                        case _: self.score += 1


    def r7(self, solution : list[Box]) -> None:
        """
        Tout le monde est servi
        Lorsqu’un abonné participant à la campagne ne reçoit
        aucun article (box vide), la composition subit un malus global de -10
        :param solution: La solution proposée
        :return: le score de la solution par rapport à cette règle
        """
        raise NotImplementedError("R7")

    def r8(self, solution : list[Box]) -> None:
        """
        Equité
        orsqu’un abonné reçoit 2 articles de moins (ou plus) qu’un autre
        abonné dans la même campagne, la composition subit un malus global de -10 (appliqué
        une seule fois par abonné concerné).
        :param solution: La solution proposée
        :return: Le score de la solution proposée par rapport à cette règle
        """
        raise NotImplementedError("R8")