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

- In Python, arrays are called lists.

# Tooling 

- https://code.visualstudio.com/docs/python/jupyter-support-py#_jupyter-code-cells
- https://code.visualstudio.com/docs/languages/java#_install-a-java-development-kit-jdk