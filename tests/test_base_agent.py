import unittest
from base_agent import BaseAgent


class TestBaseAgent(unittest.TestCase):
    def test_base_agent_cannot_instantiate(self):
        with self.assertRaises(TypeError):
            agent = BaseAgent()

    def test_subclass_must_implement_abstract_methods(self):
        class ConcreteAgent(BaseAgent):
            def initialize(self, config):
                pass

            def execute(self, task):
                pass

            # 'finalize' method is not implemented here

        with self.assertRaises(TypeError):
            agent = ConcreteAgent()

if __name__ == '__main__':
    unittest.main()
