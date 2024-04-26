from abc import ABC, abstractmethod


class BaseAgent(ABC):
    @abstractmethod
    def initialize(self, config):
        """Initialize agent with config."""
        pass

    @abstractmethod
    def execute(self, task):
        """Execute a given task based on agent capabilities."""
        pass

    @abstractmethod
    def finalize(self):
        """Cleanup resources if needed."""
        pass
