import unittest
import boggle


class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid), 0)
            
    def test_grid_coordinatges(self):
        """
        Test to ensure that all of the coordinates 
        inside of the grid can be accessed. 
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        
        
        
        
        
        
        