[![PyPI version](https://badge.fury.io/py/base-agent.svg)](https://badge.fury.io/py/base-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/base-agent)](https://pepy.tech/project/base-agent)

# BaseAgent

`BaseAgent` is an abstract base class designed to support the development of various agent-based systems. It provides a structured approach to creating agents with initialization, execution, and cleanup phases.

## Installation

To install `BaseAgent`, you can use pip directly from GitHub:

```bash
pip install git+https://github.com/chigwell/BaseAgent.git
```

## Usage

`BaseAgent` is intended to be subclassed by other classes that implement specific agent behaviors. Here's an example of how to create a concrete agent:

```python
from base_agent import BaseAgent

class MyAgent(BaseAgent):
    def initialize(self, config):
        print("Initializing with config:", config)

    def execute(self, task):
        print("Executing task:", task)
        return "Task Completed"

    def finalize(self):
        print("Cleaning up resources.")

# Example usage
if __name__ == "__main__":
    agent = MyAgent()
    agent.initialize(config={"setting": "value"})
    result = agent.execute(task="Example Task")
    print(result)
    agent.finalize()
```

This example demonstrates the basic structure of an agent that can be built using the `BaseAgent` framework.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/BaseAgent/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
