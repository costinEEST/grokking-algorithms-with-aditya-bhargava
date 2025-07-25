# Gotchas 

| Gotcha                   | Python                                 | Java                                                                         | JavaScript                              |
| ------------------------ | -------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------- |
| **Integer Division**     | `(low + high) // 2`                    | `(low + high) / 2` ⚠️ **Overflow risk!**<br/>Better: `low + (high - low) / 2` | `Math.floor((low + high) / 2)`          |
| **Array Length**         | `len(arr)`                             | `arr.length`                                                                 | `arr.length`                            |
| **Function Definition**  | `def binary_search():`                 | `public static Integer binarySearch()`                                       | `function binarySearch()`               |
| **Variable Declaration** | `low = 0`                              | `int low = 0;`                                                               | `let low = 0;`                          |
| **Equality Check**       | `==`                                   | `==` (primitives)<br/>`equals()` (objects)                                   | `===` (strict)<br/>`==` (loose, avoid!) |
| **Null/None Value**      | `None`                                 | `null`                                                                       | `null`                                  |
| **Return Type**          | Dynamic                                | Must declare `Integer` (not `int`) to return `null`                          | Dynamic                                 |
| **Naming Convention**    | `snake_case`                           | `camelCase`                                                                  | `camelCase`                             |
| **Division Behavior**    | `/` returns float<br/>`//` returns int | `/` returns int for integers<br/>float for mixed types                       | `/` always returns float                |
| **Semicolons**           | Optional (not used)                    | Required `;`                                                                 | Optional but recommended `;`            |

# Syntax 

- In Python, arrays are called [lists](https://docs.python.org/3/library/stdtypes.html#lists).
- [`range(start, stop[, step])`](https://docs.python.org/3/library/stdtypes.html#range)

# Theory 

-  Algorithm times are measured in terms of growth of an algorithm.
-  Algorithm times are written in [big O notation](https://en.wikipedia.org/wiki/Big_O_notation).
-  Common big O run times, sorted from fastest to slowest:
   -  `O(log n)`, also known as [logarithmic time](https://en.wikipedia.org/wiki/Time_complexity#Logarithmic_time) (binary search).
   -  `O(n)`, also known as linear time (simple search).
   -  `O(n * log n)`, a fast sorting algorithm (quicksort).
   -  `O(n*n)`, a slow sorting algorithm (selection sort).
   -  `O(n!)`, a really slow algorithm (traveling salesperson).
- Lists are better if you want to insert elements into the middle.
- Linked lists allow fast inserts an deletes. 
- Random access (offered by arrays), means you can jump directly to a specific element.
- Arrays are faster because they can use caching. 
- Insertions and deletions are `O(1)`, or constant time, only if you can instantly access the element to be deleted.


# Tooling 

- https://code.visualstudio.com/docs/python/jupyter-support-py#_jupyter-code-cells
- https://code.visualstudio.com/docs/languages/java#_install-a-java-development-kit-jdk
- Execute a Typescript file from CLI: `node --experimental-transform-types 01_binarySearch.ts` 