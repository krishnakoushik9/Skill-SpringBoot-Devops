[[Kunal Kushwaha]]
Basic Definitions to memorize
### 🧮 **Array – Definition**

> An **Array** is a linear data structure that stores a **fixed-size sequence of elements** of the **same data type**, accessible by an **index**.

- In Java: `int[] arr = new int[5];`
    
- Indexed from `0` to `n-1`
    
- Stored in **contiguous memory**
    
- Efficient for lookup (`O(1)`), but resizing is not dynamic
    

🔸 Use when:

- You know the number of elements beforehand
    
- All elements are of the same type
----
### 🔤 **char – Definition**

> `char` (short for **character**) is a **primitive data type** in Java and other languages that represents a **single 16-bit Unicode character**.

- Example: `char letter = 'A';`
    
- Can hold letters, symbols, digits, even escape characters like `'\n'`
    
- In memory, it's stored as a **numeric code (ASCII or Unicode)**
    

🔸 Used for:

- Individual character operations
    
- Character-based input/output
----
### 🧵 **String**

> A **String** is a **sequence of characters** stored together as one data type, often used to represent **words, sentences, or text**. In many languages like Java, a String is an **object**, not a primitive type. It is **immutable**, meaning once created, its value cannot be changed.

#### 🧠 Internals (Java-specific):

- Strings are internally stored as a **character array (`char[]`)**
    
- Every time you perform an operation like `str1 + str2`, a **new String object** is created (unless using `StringBuilder`)
    
- Java stores String literals in a **String pool** to optimize memory

#### 🔒 Immutability:

- Helps with **thread safety**
    
- Prevents accidental modification
    
- Improves caching (e.g., HashMaps use Strings as keys)
![[Pasted image 20250713122614.png]]
![[Recording 20250713122745.m4a]]
#### 🧰 Common Uses:

- Usernames, messages, file paths, JSON, API keys
    
- Text parsing, file reading, UI rendering

#### ✨ Features:

- Built-in methods like `.length()`, `.substring()`, `.charAt()`, `.equals()`
    
- Can be split, joined, converted to numbers, etc.

#### ⚠️ Tip:

If you’re doing **many string edits** (like in loops), use **`StringBuilder`** instead of `+` for better performance.

![[Pasted image 20250713120356.png]]
![[Pasted image 20250713120450.png]]
### What is a **String Pool** in Java?

The **String Pool** is a special memory area in Java inside the **heap** where **String literals** are stored. It is part of the **Java String interning** mechanism that helps **save memory** and improve **performance**.
When you create a string like:
String s1 = "hello";
String s2 = "hello";
- Both `s1` and `s2` **refer to the same object** in the string pool — **only one "hello" object is created**.
- No duplicate is created unless explicitly forced.
- But if you write:
- String s3 = new String("hello");
This creates a **new object in heap** (outside the pool), **even if** "hello" already exists in the pool.
![[Recording 20250713121048.m4a]]
![[Recording 20250713121555.m4a]]
Please Listen to the Voice note : "Recording 20250713121048.m4a" and "Recording 20250713121555.m4a"
![[Pasted image 20250713123520.png]]
![[Recording 20250713123626.m4a]]
![[Pasted image 20250713123702.png]]

==String Comparisons==
![[Pasted image 20250713144650.png]]

![[Pasted image 20250713145109.png]]

- The above Code indicates that String a & String b are pointed towards the Pool of the Object(Krishna) but it came out has a false when checking name 1 & name 2 cause they are new Strings explicitly maintained outside of that Pool of Similar data in Java
![[Recording 20250713145623.m4a]]

----
But we have a Java feature called .equals()
![[Recording 20250713145902.m4a]]
### Let's see that in action

![[Pasted image 20250713145957.png]]
Now both the checks are true cause .equals() check if the values are similiar or not instead of checking of they are pointing at different objects or not is ignored

> [!NOTE] To Print Specific Char with Correspondence to Index Value
> 
>![[Pasted image 20250713150836.png]]

### What Are Command-Line Arguments?

Command-line arguments are parameters **passed to a Java program when it is run from the terminal or command prompt**. These arguments are received in the `main` method through the array
- public static void main(String[] args)
- `String[] args` is an **array of `String` values**, where each value represents one argument entered by the user.
### 🧠 Notes:

- Arguments are **always Strings**. If you want numbers, you must convert using `Integer.parseInt(args[0])`, etc.
- Useful in CLI apps, configuration passing, automation scripts, etc.

---
![[Pasted image 20250713184608.png]]
### `System.out.println('a' + 'b');`

- `'a'` and `'b'` are `char` types.
- In Java, `char` is internally stored as an **integer ASCII value**.
    - `'a'` = 97, `'b'` = 98 → `97 + 98 = 195`  
        ✅ **Output:** `195`
### `System.out.println("a" + "b");`

- `"a"` and `"b"` are both `String` literals.
    
- `+` is used for **string concatenation** here.  
    ✅ **Output:** `ab`
### `System.out.println((char)('a' + 3));`

- `'a'` = 97 → `97 + 3 = 100`
    
- `(char)100` is `'d'` (ASCII of 100)  
    ✅ **Output:** `d`
### `System.out.println("a" + 1);`

- `"a"` is a `String`, `1` is an `int`
    
- Java converts `1` into `"1"` using **autoboxing + `toString()`**
    
- Then it performs **string concatenation**: `"a" + "1"` = `"a1"`  
    ✅ **Output:** `a1`
---
