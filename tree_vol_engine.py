# -----------------------------------------------------------------------------
# Name:        volumes_Sharma_2021
# Purpose:     Calculate the volumes of Sharma 2021-Total_and_merchantable...
#              paper
#
# Author:      triklit
#
# Created:     12-12-2021
# Copyright:   (c) Todd 2021
# Licence:     <your licence>
# -----------------------------------------------------------------------------


class sharma2021:
    r"""Calculate the inner and outer bark volumes and merchantable volumes
    from Sharma's 2021 paper
    """

    # Class variable
    # Inside bark volume coefficients Sharma 2021, Table 2
    #       GY Program standard species code:
    #          alpha,    beta,   gamma,  phi,    sigmae, sigmab, species
    inside_bark_vol = {
        3: [0.00675, 0.1972, 1.8654, 5.6033, 1.4648, 0.00020, "jack pine"],
        1: [0.00024, 0.2056, 1.8864, 5.7062, 1.6284, 0.00016, "white pine"],
        2: [0.000506, 0.1760, 1.8340, 1.8906, 0.00079, None, "red pine"],
        99: [0.000238, 0.2293, 1.8952, 5.2728, 1.9901, None, "lodgepole pine"],
        13: [0.00097, 0.2699, 1.9431, 5.1064, 1.0221, None, "black spruce"],
        12: [0.000367, 0.1890, 1.8619, 4.9711, 1.1377, None, "white spruce"],
        14: [0.00014, 0.2430, 1.8974, 1.8336, 0.0006, None, "red spruce"],
        98: [0.000378, 0.1240, 1.7773, 1.9353, 0.0009, None, "Engelmann spruce"],
        20: [0.001305, 0.3532, 2.0050, 1.9936, 0.0007, None, "balsam fir"],
        38: [0.00203, 0.2772, 1.9611, 4.5170, 0.7862, None, "paper birch"],
        37: [0.00686, 0.1765, 1.8754, 4.7059, 0.6886, 0.00032, "yellow birch"],
        30: [0.00207, 0.2390, 1.9451, 0.5934, 0.0006, None, "sugar maple"],
        75: [0.00010, 0.3175, 1.9817, 5.1072, 1.6622, None, "Populus sp"],
        73: [0.00015, 0.09378, 1.7360, 3.6593, 0.425, None, "balsam poplar"],
        74: [0.00038, 0.1685, 1.8649, 2.4636, 0.0009, None, "trembling aspen"],
        70: [0.00020, 0.3047, 1.9938, 2.4937, 0.0007, None, "large-tooth aspen"],
        46: [0.00089, 0.1634, 1.8784, 2.2544, 0.0012, None, "white ash"],
        22: [0.01518, 0.9485, 2.2870, 3.0772, 0.0007, None, "eastern white cedar"],
        100: [0.001838, 0.1316, 1.7820, 5.8382, 1.9182, None, "cedar sp"],
        101: [00.005468, 0.3545, 2.0540, 2.1526, 0.0007, None, "western larch"],
        26: [0.02890, 0.7331, 2.2227, 1.2994, 0.0003, None, "European larch"],
        58: [0.00271, 0.1257, 1.8044, 0.1758, 0.0003, None, "black cherry"],
        44: [0.00020, 0.1572, 1.8422, 4.3307, 0.6370, None, "American beech"],
        51: [0.00029, 0.2710, 1.9887, 5.8579, 10.9818, 0.00033, "American basswood"],
        41: [0.002617, 0.1119, 1.7637, 3.2168, 0.0675, None, "red oak"],
    }

    # Class variable
    # Outside bark volume coefficients Sharma 2021, Table 3
    #       GY Program standard species code:
    #          alpha,    beta,   gamma,  phi,    sigmae, sigmab, species
    outside_bark_vol = {
        3: [0.00145, 0.2047, 1.8529, 4.4525, 0.00001, 0.00073, "jack pine"],
        1: [0.00429, 0.3801, 2.0166, 5.0449, 0.00001, 0.00058, "white pine"],
        2: [0.002002, 0.2133, 1.8505, 1.7698, 0.00093, None, "red pine"],
        99: [0.001438, 0.2651, 1.9095, 5.4547, 3.5581, None, "lodgepole pine"],
        13: [0.002755, 0.2691, 1.9174, 4.1445, 0.3226, None, "black spruce"],
        12: [0.001078, 0.1792, 1.8261, 4.6454, 0.8569, None, "white spruce"],
        14: [0.000479, 0.3119, 1.9279, 1.9562, 0.0009, None, "red spruce"],
        98: [0.001463, 0.1003, 1.7093, 1.9030, 0.0010, None, "Engelmann spruce"],
        20: [0.001619, 0.4148, 2.0152, 2.0515, 0.0009, None, "balsam fir"],
        38: [0.00288, 0.3306, 1.9756, 4.6274, 0.9907, None, "paper birch"],
        37: [0.00846, 0.2568, 1.9386, 4.8721, 1.0349, 0.00028, "yellow birch"],
        30: [0.00285, 0.3176, 1.9853, 0.6112, 0.0008, None, "sugar maple"],
        75: [0.00104, 0.3117, 1.9477, 4.9836, 1.3612, None, "Populus sp"],
        73: [0.001095, 0.1740, 1.8287, 3.86173, 0.2266, None, "balsam poplar"],
        74: [0.00039, 0.1731, 1.8408, 6.4200, 17.8453, None, "trembling aspen"],
        70: [0.000952, 0.2466, 1.9154, 2.2766, 0.0010, None, "large-tooth aspen"],
        46: [0.00142, 0.2157, 1.9032, 5.1083, 2.5381, None, "white ash"],
        22: [0.02196, 0.6797, 2.1667, 3.7882, 0.0011, None, "eastern white cedar"],
        100: [0.002455, 0.2188, 1.8734, 5.8241, 2.4155, None, "cedar sp"],
        101: [0.1454, 0.1481, 1.8363, 2.2982, 0.0011, None, "western larch"],
        26: [0.4685, 1.0823, 2.2723, 1.7556, 0.0005, None, "European larch"],
        58: [0.00221, 0.1396, 1.8018, 0.4692, 0.0008, None, "black cherry"],
        44: [0.00020, 0.1519, 1.8200, 4.4480, 0.9685, None, "American beech"],
        51: [0.00075, 0.3202, 1.9868, 9.1932, 24.7618, 0.00053, "American basswood"],
        41: [0.004630, 0.1049, 1.7239, 3.4654, 0.1359, None, "red oak"],
    }

    # Class variable
    # Merchantable volume coefficients Sharma 2021, Table 4
    #       GY Program standard species code:
    #          alpha,    beta,    gamma,  phi,    sigmae, sigmab, species
    merchantable_vol = {
        3: [-0.00592, 0.2015, 1.8737, 1.4828, 0.0007, None, "jack pine"],
        1: [-0.00689, 0.1727, 1.8525, 1.6942, 0.0014, None, "white pine"],
        2: [-0.00838, 0.1603, 1.8159, 1.5847, 0.0010, None, "red pine"],
        99: [-0.01230, 0.2046, 1.8712, 4.1662, 0.5132, None, "lodgepole pine"],
        13: [-0.00650, 0.26621, 1.9458, 3.8646, 0.1910, None, "black spruce"],
        12: [-0.00274, 0.1848, 1.8664, 4.0182, 0.3434, None, "white spruce"],
        14: [-0.00648, 0.2382, 1.9009, 1.2973, 0.0006, None, "red spruce"],
        98: [-0.00610, 0.1198, 1.7751, 1.7295, 0.0011, None, "Engelmann spruce"],
        20: [-0.00529, 0.3135, 1.9876, 1.2835, 0.0007, None, "balsam fir"],
        38: [-0.00718, 0.1821, 1.8754, 3.8797, 0.3155, None, "paper birch"],
        37: [-0.00418, 0.1151, 1.7836, 1.7338, 0.0019, None, "yellow birch"],
        30: [-0.00519, 0.2702, 1.9821, 0.6019, 0.0007, None, "sugar maple"],
        75: [-0.01060, 0.2599, 1.9387, 4.7496, 1.0729, None, "Populus sp"],
        73: [-0.01312, 0.1608, 1.8351, 2.7787, 0.0084, None, "balsam poplar"],
        74: [-0.01339, 0.1301, 1.8967, 4.8477, 1.2085, None, "trembling aspen"],
        70: [-0.00885, 0.2334, 1.9377, 1.7908, 0.0008, None, "large-tooth aspen"],
        46: [-0.00835, 0.1951, 1.9277, 2.2796, 0.0123, None, "white ash"],
        22: [-0.00021, 0.5431, 2.1441, 2.7489, 0.0006, None, "eastern white cedar"],
        100: [-0.00538, 0.2055, 1.9006, 1.9552, 0.1101, None, "cedar sp"],
        101: [-0.00101, 0.6226, 2.1812, 1.7970, 0.0008, None, "western larch"],
        26: [-0.00019, 0.3479, 2.0431, 0.3302, 0.0005, None, "European larch"],
        58: [-0.01272, 0.0992, 1.7514, 0.9577, 0.0004, None, "black cherry"],
        44: [-0.01211, 0.1114, 1.7662, 3.6768, 0.2099, None, "American beech"],
        51: [-0.00127, 5.2555, 2.7049, 5.3493, 11.7260, None, "American basswood"],
        41: [-0.00858, 0.07959, 1.6952, 3.2073, 0.1096, None, "red oak"],
    }

    def __init__(self, height, dbh, species_code):
        r"""Class constructor"""
        self.height = height
        self.dbh = dbh

        # Ensure that the species code provided has coefficients
        if species_code not in (sharma2021.inside_bark_vol.keys()):
            raise KeyError(
                f"Species code not present! The species code "
                f"'{species_code}' is not a key in the 'inside "
                f"bark' coefficient dict."
            )
        elif species_code not in (sharma2021.outside_bark_vol.keys()):
            raise KeyError(
                f"Species code not present! The species code "
                f"'{species_code}' is not a key in the 'outside "
                f"bark' coefficient dict."
            )
        elif species_code not in (sharma2021.merchantable_vol.keys()):
            raise KeyError(
                f"Species code not present! The species code "
                f"'{species_code}' is not a key in the "
                f"'merchantable' coefficient dict."
            )
        else:
            self.species_code = species_code

    def equation10(
        self,
        height: float,
        dbh: float,
        alpha: float,
        beta: float,
        gamma: float,
        phi: float,
        sigmae=None,
        sigmab=None,
        species_code: int = None,
        random_effect=None,
        species: str = None,
    ):
        r"""Parameters:
            height = tree height in metres (m)
            dbh = diameter at breast height in metres (m)
            alpha, beta, gamma, phi = parameter for Dr. Mahadev Sharma paper
            sigmae, sigmab = variance of the model from Dr. Mahadev Sharma's paper
            species = species code to call the coefficients
            random_effects = random effects.

        Returns:
            List, species name and volume in cubic metres.
        """

        if random_effect is None:
            vol = alpha + beta * dbh ** (gamma) * height ** (3 - (gamma))
        elif random_effect is not None:
            vol = alpha + beta * dbh ** (gamma + random_effect) * height ** (
                3 - (gamma + random_effect)
            )
        else:
            print("What?!")

        # At small height and dbh the merchantable volumes can be negative
        if vol <= 0:
            vol = 0
        else:
            vol

        return [species, vol]

    def inside_bark_eq(self):
        r"""Calculated the inside bark volume with equation 10"""
        (
            self.alpha,
            self.beta,
            self.gamma,
            self.phi,
            self.sigmae,
            self.sigmab,
            self.species,
        ) = sharma2021.inside_bark_vol[self.species_code]

        return self.equation10(
            height=self.height,
            dbh=self.dbh,
            alpha=self.alpha,
            beta=self.beta,
            gamma=self.gamma,
            phi=self.phi,
            sigmae=self.sigmae,
            sigmab=self.sigmab,
            species_code=self.species_code,
            random_effect=None,
            species=self.species,
        )

    def outside_bark_eq(self):
        r"""Calculated the outside bark volume with equation 10"""
        (
            self.alpha,
            self.beta,
            self.gamma,
            self.phi,
            self.sigmae,
            self.sigmab,
            self.species,
        ) = sharma2021.outside_bark_vol[self.species_code]

        return self.equation10(
            height=self.height,
            dbh=self.dbh,
            alpha=self.alpha,
            beta=self.beta,
            gamma=self.gamma,
            phi=self.phi,
            sigmae=self.sigmae,
            sigmab=self.sigmab,
            species_code=self.species_code,
            random_effect=None,
            species=self.species,
        )

    def merchantable_eq(self):
        r"""Calculated the merchantable volume with equation 10"""
        (
            self.alpha,
            self.beta,
            self.gamma,
            self.phi,
            self.sigmae,
            self.sigmab,
            self.species,
        ) = sharma2021.merchantable_vol[self.species_code]

        return self.equation10(
            height=self.height,
            dbh=self.dbh,
            alpha=self.alpha,
            beta=self.beta,
            gamma=self.gamma,
            phi=self.phi,
            sigmae=self.sigmae,
            sigmab=self.sigmab,
            species_code=self.species_code,
            random_effect=None,
            species=self.species,
        )


if __name__ == "__main__":

    pass

