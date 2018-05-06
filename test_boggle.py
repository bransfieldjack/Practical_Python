import unittest #Imports unittest framework
import boggle #imports from boggle.py
from string import ascii_uppercase #Imports the ascii characters a-z


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
    
    def test_grid_is_filled_with_letters(self): #Function to confirm that the frid is filled with letters. 
        """
        Ensure that each of the coordinates on the grid 
        contains letters.
        """
        grid = boggle.make_grid(2, 3) #Local grid variable, calls make_grid from boggle.py. Passes arguments (2, 3)
        for letter in grid.values(): #For loop to check for and return letters in the grid. 
            self.assertIn(letter, ascii_uppercase) #Seertion test to confirm that letter is an Ascii character.  
            
    def test_neighbours_of_a_position(self):
        """
        Ensure that a position has 8 neighbours
        """
        coords = (1, 2) #Variable coords set to (1, 2)
        neighbours = boggle.neighbours_of_a_position(coords) #Neighbours variable calls function from boggle.py
        self.assertIn((0, 1), neighbours) #Tests positions on the grid
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        
    def test_all_grid_neighbours(self):
        """
        Ensure that all of the grid positions have neighbours
        """
        grid = boggle.make_grid(2, 2) #Grid variable, makes a 2 x 2 grid (Neighbours of any position are the other two positions in the grid)
        neighbours = boggle.all_grid_neighbours(grid) #Creates a dictionary
        self.assertEqual(len(neighbours), len(grid)) #Asserts the correct lenght of the neighbours dctionary. 
        for pos in grid: #For loop iterates through the grid.
            others = list(grid) #Creates a list which is the full grid minus the position in question. 
            others.remove(pos) #Removes the position in question from the others list. 
            self.assertListEqual(sorted(neighbours[pos]), sorted(others)) #Asserts that the positions are the neighbours of the position being checked. 
            
            
            
            
            
        
        
        
        