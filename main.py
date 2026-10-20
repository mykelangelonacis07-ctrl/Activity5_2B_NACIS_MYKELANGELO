from array_stack import ArrayStack
from array_queue import ArrayQueue
from applications import check_balanced_parentheses, simulate_print_queue

def main():
    print("=== Module 5: Stacks and Queues Verification Suite ===")
    
    # 1. Test ArrayStack and Overflow/Underflow exceptions
    print("\n[Testing ArrayStack]")
    stack = ArrayStack(2)
    stack.push("Apple")
    stack.push("Banana")
    print("Pushed 2 items. Is stack full?", stack.is_full())
    try:
        stack.push("Cherry") # Should raise OverflowError
    except OverflowError as e:
        print("Caught expected error:", e)
        
    print("Popped item:", stack.pop())
    print("Popped item:", stack.pop())
    try:
        stack.pop() # Should raise IndexError
    except IndexError as e:
        print("Caught expected error:", e)

    # 2. Test Circular ArrayQueue & Wrap-around
    print("\n[Testing Circular ArrayQueue]")
    queue = ArrayQueue(2)
    queue.enqueue(10)
    queue.enqueue(20)
    print("Dequeued:", queue.dequeue()) # Free up space at index 0
    queue.enqueue(30) # Tests wrap-around index computation
    print("Dequeued (wrap-around test):", queue.dequeue())
    print("Dequeued final item:", queue.dequeue())

    # 3. Test Applications
    print("\n[Testing Applications]")
    test_str = "{[()()]}"
    print(f"Is expression '{test_str}' balanced? ->", check_balanced_parentheses(test_str))
    
    simulate_print_queue()

if __name__ == "__main__":
    main()