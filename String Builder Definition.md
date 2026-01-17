### `StringBuilder`:

- `StringBuilder` is **mutable**, which means you can change its content without creating a new object.
    
- Methods like `.append()`, `.insert()`, `.delete()` allow you to manipulate strings **in-place**.
    
- This makes `StringBuilder` **much faster** and **more memory-efficient** for tasks involving **frequent string modifications** (e.g., loops or dynamic content).
    
- It is **not thread-safe**, meaning it's not safe to use across multiple threads without synchronization.
    
- Best used when you need to build or modify large strings dynamically.

> [!NOTE] Below are Few StringBuilder Methods
> .append()
.insert()
.delete()
.deleteCharAt()
.replace()
.reverse()
.charAt()
.setCharAt()
.length()
.capacity()
.ensureCapacity()
.indexOf()
.lastIndexOf()
.substring()
.toString()

