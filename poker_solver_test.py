import unittest

from poker_solver import PokerSolver

class PokerSolverTest(unittest.TestCase):
    
    def setUp(self):
        self.solver = PokerSolver()
    
    def test_solve_withSimilarHand(self):
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH'), 'tie')
    
    def test_solve_withHighCard(self):
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S 9C AD  White: 2D 3H 5C 9S KH'), 'Black')
        
    def test_solve_withOnePair(self):
        self.assertEquals(self.solver.solve('Black: 2H 2D 5S 9C KD  White: 2D 3H 5C 9S KH'), 'Black')
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 5S KH'), 'White')
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S KC KD  White: 2D 3H 9C 9S KH'), 'Black')
        self.assertEquals(self.solver.solve('Black: 2H 3D 5S KC KD  White: 2D 3H 5C KS KH'), 'tie')
    
    def test_solve_withTwoPair(self):
        self.assertEquals(self.solver.solve('Black: 2H 2D 5S 5C KD  White: 2D 3H 5C 9S KH'), 'Black')
        self.assertEquals(self.solver.solve('Black: 2H 2D 5S 5C KD  White: 2D 3H 5C KS KH'), 'Black')
        self.assertEquals(self.solver.solve('Black: 2H 2D 5S 5C KD  White: 2D 5H 5C KS KH'), 'White')
        self.assertEquals(self.solver.solve('Black: 2H 5D 5S KC KD  White: 2D 5H 5C KS KH'), 'tie')
        
    def test_solve_withThreeOfAKind(self):
        self.assertEquals(self.solver.solve('Black: 2H 2D 2S 9C KD  White: 3D 3H 5C 9S KH'), 'Black')
        self.assertEquals(self.solver.solve('Black: 2H 2D 2S 9C KD  White: 3D 3H 3C 9S KH'), 'White')

    def test_solve_withStraight(self):
        self.assertEquals(self.solver.solve('Black: 2H 3D 4S 5C 6D  White: 2D 3H 5C 9S KH'), 'Black')
        self.assertEquals(self.solver.solve('Black: 9H 6D 7S 8C 5D  White: 3D 4H 5C 6S 7H'), 'Black')

    def test_solve_withFlush(self):
        self.assertEquals(self.solver.solve('Black: 2H 3D 4S 5C 6D  White: 2H 3H 5H 9H KH'), 'White')
        self.assertEquals(self.solver.solve('Black: 2D 3D KD AD TD  White: 2H 3H QH JH KH'), 'Black')

    def test_solve_withFullHouse(self):
        self.assertEquals(self.solver.solve('Black: 2H 2D 4S 4C 4D  White: 2H 3H 5H 6H 7H'), 'Black')
        self.assertEquals(self.solver.solve('Black: 2H 2D 4S 4C 4D  White: 7H 7S 5H 5H 5H'), 'White')
        self.assertEquals(self.solver.solve('Black: 2H 2D 4S 4C 4D  White: 7H 7S 3H 3H 3H'), 'Black')
        self.assertEquals(self.solver.solve('Black: 7H 7D 4S 4C 4D  White: 2H 2S 4H 4H 4H'), 'Black')

    def test_solve_withFourOfAKind(self):
        self.assertEquals(self.solver.solve('Black: 2H 2D 2S 2C KD  White: 3D 3H 5C 9S KH'), 'Black')
        self.assertEquals(self.solver.solve('Black: 2H 2D 2S 2C KD  White: 3D 3H 3C 3S KH'), 'White')
        self.assertEquals(self.solver.solve('Black: 2H 2D 2S 2C KD  White: 2D 2H 2C 2S AH'), 'White')

    def test_solve_withStraightFlush(self):
        self.assertEquals(self.solver.solve('Black: 2H 3D 4S 5C 6D  White: 2H 3H 4H 5H 6H'), 'White')
        self.assertEquals(self.solver.solve('Black: 7S 8S 9S TS JS  White: 2H 3H 4H 5H 6H'), 'Black')
        
    def test_solve_withOtherName(self):
        self.assertEquals(self.solver.solve('Nicolas: 2H 3D 4S 5C 6D  Sebastien: 2H 3H 4H 5H 6H'), 'Sebastien')

if __name__ == '__main__':
    unittest.main()
