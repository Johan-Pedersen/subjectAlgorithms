import unittest
import ncpc2014Aflevering as sol
class Test_NCPC(unittest.TestCase):
    def test_D_2014(self):
            self.assertEqual(sol.D_2014([1,4,1,4], [1,6,1,6]), "Emma")
            self.assertEqual(sol.D_2014([1,8,1,8], [1,10,2,5]), "Tie")
            self.assertEqual(sol.D_2014([2,5,2,7], [1,5,2,5]), "Gunnar")
    
    def test_G_2014(self):
        self.assertEqual(sol.G_2014(4, 4, [1, 2, 3, 4]), 4)
        self.assertEqual(sol.G_2014(12, 3, [2, 3, 4, 5, 6, 7, 4, 7, 8, 8, 12, 12]), 2)
        self.assertEqual(sol.G_2014(5, 4, [2, 3, 1, 5, 4]), 3)
    
    def test_I_2014(self):
        self.assertEqual(sol.I_2014(10, [[0, 0, 1, 0],[0, 1, 1, 1],[0, 2, 2, 2],[0, 0, 0, 4],[1, -1, 1, 0],[2, -2, 2, 2],[1, 1, 2, 2],[1, 1, 0, 2],[3, 1, 2, 2],[1, 3, 0, 2]]), 6)
        

if __name__ == '__main__':
    unittest.main()