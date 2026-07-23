

What are Shallow and Deep Copy?

When you copy an object in Python, the behavior depends on whether it's a shallow copy or deep copy:

Assignment (=) → NOT a copy — creates another reference to the SAME object
Shallow copy → Creates a new object, but nested objects are shared (still reference same inner objects)
Deep copy → Creates a completely independent copy — new object AND all nested objects

Real life example:

Assignment → giving someone your apartment key — same apartment, two keys

Shallow copy → photocopying a folder — new folder, but the papers inside are the originals

Deep copy → photocopying both the folder AND every paper inside — completely independent

===============================================================================================================
Core idea:

import copy

original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ref      = original            # same object
shallow  = copy.copy(original) # new list, same inner lists
deep     = copy.deepcopy(original)  # new list, new inner lists

original[0][0] = 999

print(ref[0][0])     # 999 — same object!
print(shallow[0][0]) # 999 — inner list shared!
print(deep[0][0])    # 1   — completely independent!

==============================================================================================================

Why Understand Copy Behavior?
Without understanding:

  ❌ Modify "copy" accidentally changes original
    
  ❌ Functions mutate arguments unexpectedly
  
  ❌ Hard-to-find bugs in data processing
  
  ❌ Unexpected shared state between objects
  
  ❌ Cache objects getting corrupted

With understanding:

  ✅ Safely transform data without side effects
  
  ✅ Functions that don't modify their inputs
  
  ✅ Undo/redo functionality
  
  ✅ Configuration with safe defaults
  
  ✅ Snapshot/history systems

================================================================================

How Python Memory Works with Copies
Assignment (=):
  original = [[1,2], [3,4]]
  ref = original

  Memory:
  original ──────┐
                 ▼
                 LIST ──► [1,2]
                      ──► [3,4]
                 ▲
  ref  ──────────┘
  (same object!)

Shallow Copy:
  shallow = copy.copy(original)

  Memory:
  original ──► LIST1 ──► [1,2]  ◄── shared!
                     ──► [3,4]  ◄── shared!

  shallow  ──► LIST2 ──► [1,2]  ◄── same inner objects
                     ──► [3,4]  ◄── same inner objects

Deep Copy:
  deep = copy.deepcopy(original)

  Memory:
  original ──► LIST1 ──► [1,2]  (original)
                     ──► [3,4]  (original)

  deep     ──► LIST2 ──► [1,2]  (NEW copy)
                     ──► [3,4]  (NEW copy)

======================================================================================
