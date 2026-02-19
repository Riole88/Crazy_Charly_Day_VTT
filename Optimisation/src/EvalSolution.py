from opti_boxes import Box


class EvalSolution:

    def __init__(self):
        self.score : int = 0

    def evaluate(self, solution : list[Box]) -> int:
        self.score += self.r1(solution)
        self.score += self.r2(solution)
        self.score += self.r3(solution)
        self.score += self.r4(solution)
        self.score += self.r5(solution)
        self.score += self.r6(solution)
        self.score += self.r7(solution)
        self.score += self.r8(solution)
        return self.score

    def r1(self, solution) -> int:
        """
        Unicité des articles
        Chaque article ne peut apparaître que dans une seule box
        au plus. Tous les articles ne sont pas forcément utilisés.
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        raise NotImplementedError("R1")

    def r2(self, solution) -> int:
        """
        Compatibilité d’âge
        Un article ne peut être placé dans la box d’un abonné que si
        la tranche d’âge de l’article correspond exactement à la tranche d’âge de l’enfant de
        l’abonné. Par exemple, un article étiqueté PE (3-6 ans) ne peut être affecté qu’à un abonné
        ayant déclaré un enfant dans la tranche PE.
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        raise NotImplementedError("R2")

    def r3(self, solution) -> int:
        """
        Poids limité
        Le poids total des articles contenus dans une box ne doit pas
        dépasser le poids maximum Wmax défini pour la campagne.
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        raise NotImplementedError("R3")

    def r4(self, solution) -> int:
        """
        Gain par préférence de catégorie
        chaque article placé dans la box d’un abonné
        rapporte un certain nombre de points au score global. Ce nombre de points dépend de la
        position de la catégorie de l’article dans l’ordre de préférence de l’abonné
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        raise NotImplementedError("R4")

    def r5(self, solution) -> int:
        """
        Bonus d’état
        en plus des points de préférence, chaque article apporte un bonus lié à son état
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        raise NotImplementedError("R5")

    def r6(self, solution) -> int:
        """
        Utilités dégressives
        Pour encourager la variété dans les box, si plusieurs
        articles de la même catégorie sont placés dans une même box, les points diminuent pour
        chaque article supplémentaire de cette catégorie.
        :param solution: La solution proposée
        :return: Le score de la solution par rapport à cette règle
        """
        raise NotImplementedError("R6")

    def r7(self, solution) -> int:
        """
        Tout le monde est servi
        Lorsqu’un abonné participant à la campagne ne reçoit
        aucun article (box vide), la composition subit un malus global de -10
        :param solution: La solution proposée
        :return: le score de la solution par rapport à cette règle
        """
        raise NotImplementedError("R7")

    def r8(self, solution) -> int:
        """
        Equité
        orsqu’un abonné reçoit 2 articles de moins (ou plus) qu’un autre
        abonné dans la même campagne, la composition subit un malus global de -10 (appliqué
        une seule fois par abonné concerné).
        :param solution: La solution proposée
        :return: Le score de la solution proposée par rapport à cette règle
        """
        raise NotImplementedError("R8")