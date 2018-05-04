import unittest #Imports unittest framework
import boggle #imports from boggle.py


class TestBoggle(unittest.TestCase): #Creates the TestBoggle class, test suite for Boggle. 
    """
    Our test suite for boggle solver
    """
    def test_can_create_an_empty_grid(self): #Method to create an empty grid, self parameter. 
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0, 0) #Variable grid, calls the make.grid method in the boggle.py
        self.assertEqual(len(grid), 0) #Assertion test to test the length of the grid. 
            
    def test_grid_coordinatges(self): #Method to test different coordinates on the grid. 
        """
        Test to ensure that all of the coordinates 
        inside of the grid can be accessed. 
        """
        grid = boggle.make_grid(2, 2) #Another local grid variable, calls make_grid from boggle.py
        self.assertIn((0, 0), grid) #Assertion tests to test grid positions. 
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid) #Assertion test to test that some coordinates are NOT in the grid. 
        
        
        
        
        
        
        