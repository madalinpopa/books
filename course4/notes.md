## Program Memory

- Stack
    - In stack values are stored sequentialy in order that they were received
    - Those values are added and removed last in, first out
    - The stack holds also information that the program needs, for example calling functions
    - The stack is growing and shrinking as the program executes. 
    - The advantage of stack is push and pop very quckly. 
    - The limitation is that is very small (few mb)
    - Analogy: Boxes (variables) are piled up one each other when they are declared. 
- Heap
    - The data is stored into a specific location in memory that has an address.
    - That address is called pointer
    - Accessing data in the heap is slower than the stack
    - Adding data in the heap is also slower because it has to search for an available space in the memrory
    - The heap can add and remove data duynamically 
    - The heap provides more memory space to be used
