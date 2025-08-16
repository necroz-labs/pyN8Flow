# 🚀 pyN8Flow

**Define n8n workflows, the Pythonic way.**

pyN8Flow is a Python library that allows you to create, configure, and manage your n8n workflows entirely from Python code. Say goodbye to manual JSON editing and hello to programmatic, version-controllable, and reusable workflow definitions.

## ✨ Core Features

*   **Python-First Workflow Definition**: Use intuitive Python classes to define your n8n nodes and their parameters.
*   **Fluent Connection Chaining**: Easily connect nodes to build complex workflows.
*   **Automatic JSON Generation**: The library handles the serialization of your Python objects into the n8n-compatible JSON format.
*   **Version Control Friendly**: Manage your workflows in Git with clean, human-readable Python code.
*   **IDE Support**: Leverage autocompletion, type checking, and other IDE features to build workflows faster and with fewer errors.

## 💡 Example Usage

Here's a sneak peek at how you could define a simple workflow with `pyN8Flow`:

```python
from pyn8flow import Workflow, Node

# 1. Create a new workflow
wf = Workflow(name="My Awesome Python-Defined Workflow")

# 2. Define the nodes
start_node = Node(node_type="n8n-nodes-base.start")
http_node = Node(
    node_type="n8n-nodes-base.httpRequest",
    parameters={"url": "https://api.example.com/data"}
)
code_node = Node(
    node_type="n8n-nodes-base.code",
    parameters={"jsCode": "return item;"}
)

# 3. Add and connect the nodes
wf.chain(start_node, http_node, code_node)

# 4. Generate and save the n8n JSON
wf.save("my_awesome_workflow.json")

print("Workflow created successfully!")
```

## 🔭 Vision

The vision for `pyN8Flow` is to become the go-to tool for n8n power users and teams who want to apply software engineering best practices to their workflow automation pipelines. Future plans include:

*   Direct integration with the n8n API for instant deployment.
*   A registry of reusable workflow components and patterns.
*   Advanced tools for workflow validation and testing.

---
