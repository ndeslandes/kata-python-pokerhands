import unittest

from poker_solver import PokerSolver

class PokerSolverTest(unittest.TestCase):
    
    def setUp(self):
        self.solver = PokerSolver()
    
    def test_solve_withSimilarHand(self):
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH'), 'tie')
    
    def test_solve_withHighCard(self):
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S 9C AD  White: 2D 3H 5C 9S KH'), 'black')
        
    def test_solve_withOnePair(self):
        self.assertEquals(self.solver.solve('Black: 2H 2D 5S 9C KD  White: 2D 3H 5C 9S KH'), 'black')
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 5S KH'), 'white')
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S KC KD  White: 2D 3H 9C 9S KH'), 'black')
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S KC KD  White: 2D 3H 5C KS KH'), 'tie')
    
    def test_solve_withTwoPair(self):
        self.assertEquals(self.solver.solve('Black: 2H 2D 5S 5C KD  White: 2D 3H 5C 9S KH'), 'black')
        self.assertEquals(self.solver.solve('Black: 2H 2D 5S 5C KD  White: 2D 3H 5C KS KH'), 'black')
        self.assertEquals(self.solver.solve('Black: 2H 2D 5S 5C KD  White: 2D 5H 5C KS KH'), 'white')
        self.assertEquals(self.solver.solve('Black: 2H 5D 5S KC KD  White: 2D 5H 5C KS KH'), 'tie')
        
    def test_solve_withThreeOfAKind(self):
        self.assertEquals(self.solver.solve('Black: 2H 2D 2S 9C KD  White: 3D 3H 5C 9S KH'), 'black')
        self.assertEquals(self.solver.solve('Black: 2H 2D 2S 9C KD  White: 3D 3H 3C 9S KH'), 'white')

    def test_solve_withStraight(self):
        self.assertEquals(self.solver.solve('Black: 2H 3D 4S 5C 6D  White: 2D 3H 5C 9S KH'), 'black')

if __name__ == '__main__':
    unittest.main()
