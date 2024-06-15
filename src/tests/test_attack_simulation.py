import unittest
import subprocess

class TestDDosAttack(unittest.TestCase):

    def test_compile_java(self):
        result = subprocess.run(['sh', 'src/attack_simulation/compile.sh'])
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()