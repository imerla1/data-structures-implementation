Hash tables, also known as hash maps, are data structures that store key-value pairs. They use a hash function to compute an index into an array (called a hash table) where the corresponding value is stored. The key advantage of hash tables is their ability to provide fast access to values, often with an average time complexity of O(1) for insertions, deletions, and lookups, under the assumption of a good hash function and a low load factor.

Here's how they work:
1. **Hash Function**: Given a key, the hash function computes an index (hash code) in the hash table where the value associated with the key can be found. The hash function should ideally distribute keys uniformly across the hash table to minimize collisions (two keys mapping to the same index).
2. **Collision Handling**: Collisions occur when two keys hash to the same index. Hash tables use various strategies to handle collisions, such as chaining (using linked lists or other data structures to store multiple values at the same index) or open addressing (finding an alternative location in the hash table to store the value).
3. **Key-Value Pair Storage**: Hash tables store key-value pairs. Given a key, the hash table computes the index using the hash function and stores or retrieves the corresponding value at that index.

Hash tables are useful for several reasons:
- **Fast Lookup**: Hash tables offer fast lookup, insertion, and deletion operations with an average time complexity of O(1), making them efficient for many applications.
- **Flexibility**: They can store any type of data as values, providing flexibility in how data is organized and accessed.
- **Dynamic Sizing**: Hash tables can dynamically resize themselves to accommodate more key-value pairs, which is useful when the number of items stored changes over time.
- **Widely Used**: Hash tables are used in various programming languages and libraries due to their efficiency and versatility.

Overall, hash tables are a fundamental data structure in computer science, offering a balance of efficiency and flexibility for storing and accessing key-value pairs.