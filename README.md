# Activity 5: Stacks and Queues Implementation

This repository contains modular implementations of Stacks and Queues from first principles in Python, featuring array-based and linked-list architectures, explicit underflow/overflow error checking, and practical applications.

## Repository Structure
- `node.py`: Shared singly linked list Node class.
- `array_stack.py`: Fixed-capacity array implementation of a Stack with boundary checks.
- `linked_stack.py`: Dynamic singly linked list implementation of a Stack operating at the head.
- `array_queue.py`: Fixed-capacity circular array implementation of a Queue using modulo arithmetic.
- `linked_queue.py`: Dynamic singly linked list implementation of a Queue with head and rear references.
- `applications.py`: Real-world applications including balanced parentheses checking and a print spooler simulation.
- `main.py`: Interactive and automated driver test program.
- `analysis.md`: Written analysis for data structure design choices.

## How to Run
Execute the driver script to verify functionality and test error exceptions:
```bash
python main.py