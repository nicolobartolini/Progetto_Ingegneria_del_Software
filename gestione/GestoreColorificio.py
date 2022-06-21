from Colorante import Colorante


class GestoreColorificio:

    prezzo_al_litro_coloranti = 7.5  # VEDIAMO
    colorante_blu = Colorante('Blu', 10.0)
    colorante_giallo = Colorante('Giallo', 15.0)
    colorante_rosso = Colorante('Rosso', 12.5)

    def __init__(self):
        pass

    @staticmethod
    def get_prezzo_al_litro_coloranti() -> float:
        return GestoreColorificio.prezzo_al_litro_coloranti
