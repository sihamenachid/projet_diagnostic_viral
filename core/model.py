from abc import ABC, abstractmethod


class Model(ABC):
    """Classe abstraite : tous les modèles doivent respecter cette interface."""

    @abstractmethod
    def train(self, X, y):
        pass

    @abstractmethod
    def predict(self, patient_data):
        """Retourne une probabilité d'infection entre 0 et 1."""
        pass
