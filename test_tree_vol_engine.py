r"""Unit test for sharma_2021_25_tree_vol
2024-04-13 20:34:23
"""

import unittest
from sharma_2021_25_tree_vol_engine.tree_vol_engine import sharma2021


class TestSharma2021(unittest.TestCase):
    r"""This is the unittest testcase for volume_Sharma_2021, Sharma2021
    Arrange
    Act
    Assert
    """

    def test_init(self):
        r"""Test the assignment of the class attributes"""
        # Arrange
        dbhcm = 19.10
        dbhm = dbhcm / 100

        tree = sharma2021(height=20.10, dbh=dbhm, species_code=3)

        # Act and Assert
        self.assertEqual(20.10, tree.height)
        self.assertEqual(0.1910, tree.dbh)
        self.assertEqual(3, tree.species_code)

    def test_inside_bark_eq_coef(self):
        r"""Test the assignment of the inside bark equation coefficients"""
        tree = sharma2021(height=20.10, dbh=0.1910, species_code=3)

        self.assertEqual(
            [0.00675, 0.1972, 1.8654, 5.6033, 1.4648, 0.00020, "jack pine"],
            tree.inside_bark_vol[tree.species_code],
        )

    def test_inside_bark_eq_return(self):
        r"""Test the results of the inside bark equation"""
        tree = sharma2021(height=20.10, dbh=0.1910, species_code=3)

        self.assertEqual(["jack pine", 0.27736558264374644], tree.inside_bark_eq())

    def test_outside_bark_eq_coef(self):
        r"""Test the assignment of the outside bark equation coefficients"""
        tree = sharma2021(height=20.10, dbh=0.1910, species_code=3)

        self.assertEqual(
            [0.00145, 0.2047, 1.8529, 4.4525, 0.00001, 0.00073, "jack pine"],
            tree.outside_bark_vol[tree.species_code],
        )

    def test_outside_bark_eq_return(self):
        r"""Test the results of the outside bark equation"""
        tree = sharma2021(height=20.10, dbh=0.1910, species_code=3)

        self.assertEqual(["jack pine", 0.29919245591286986], tree.outside_bark_eq())

    def test_merchantable_eq_coef(self):
        r"""Test the assignment of the merchantable equation coefficients"""
        tree = sharma2021(height=20.10, dbh=0.1910, species_code=3)

        self.assertEqual(
            [-0.00592, 0.2015, 1.8737, 1.4828, 0.0007, None, "jack pine"],
            tree.merchantable_vol[tree.species_code],
        )

    def test_merchantable_eq_return(self):
        r"""Test the results of the merchantable equation"""
        tree = sharma2021(height=20.10, dbh=0.1910, species_code=3)

        self.assertEqual(["jack pine", 0.2601139055138578], tree.merchantable_eq())

    def test_merchantable_eq_cf_nrcan_calc(self):
        r"""Test the results are approximately equal to the results of the
        the NRCan taper calculator

        https://apps-scf-cfs.rncan.gc.ca/calc/en/volume-calculator

            The calculated volume is:
                Volume = 0.232 m3
            Parameters used:
                DBH: 19.10 cm (at 1.3 m)
                Total height: 20.1 m
                Stump height: 0.1 m
                Limit - Diameter: 10.0 cm
        """

        # Arrange
        tree = sharma2021(height=20.10, dbh=0.1910, species_code=3)

        species = "jack pine"
        nrcan_vol = 0.232
        result = [species, nrcan_vol]

        decimal_places = 1
        
        # Act and Assert
        self.assertAlmostEqual(
            first=result[1], second=tree.merchantable_eq()[1], places=decimal_places
        )

    def test_merchantable_eq_cf_maurer_dbh19(self):
        r"""Comparison of calculations with Neil Maurer's 
        Jack Pine Site Class X, dbhcm 19, p. 50
        Maurer 1993-Local_tree_volume_tables_for_northeastern_Ontario-NEST_FG-002.pdf
        """
        # Arrange
        tree = sharma2021(height=19.0, dbh=0.19, species_code=3)

        # Jack Pine Site Class X, p. 50
        species = "jack pine"
        vol = 0.206  # Gross Merchantable Volume
        result = [species, vol]

        decimal_places = 1
        
        # Act and Assert
        self.assertAlmostEqual(
            first=result[1], second=tree.merchantable_eq()[1], places=decimal_places
        )
        
    def test_merchantable_eq_cf_maurer_dbh70(self):
        r"""Comparison of calculations with Neil Maurer's 
        Jack Pine Site Class X, dbhcm 70, p. 50
        Maurer 1993-Local_tree_volume_tables_for_northeastern_Ontario-NEST_FG-002.pdf
        """
        # Arrange
        tree = sharma2021(height=27.7, dbh=0.70, species_code=3)

        # Jack Pine Site Class X, p. 51
        species = "jack pine"
        vol = 4.300  # Gross Merchantable Volume
        result = [species, vol]

        decimal_places = 1
        
        # Act and Assert
        self.assertAlmostEqual(
            first=result[1], second=tree.merchantable_eq()[1], places=decimal_places
        )

if __name__ == "__main__":
    unittest.main()
