**GET:**

- Used to **fetch data** from the server.
- Sends data through the **URL** (visible in the address bar).
- Can be bookmarked and cached.
- Limited in how much data it can send.
- Safe and used for read-only operations.

**Example:**  
Typing this in the browser:  
`https://example.com/search?query=books`  
This sends a GET request to search for "books".

---

**POST:**

- Used to **send data** to the server (like submitting a form).
- Sends data in the **body** of the request (not visible in URL).
- Cannot be bookmarked.
- Can send large amounts of data.
- Used for actions that **change data** on the server.

**Example:**  
Submitting a login form (with username and password) sends a POST request.

---

**Summary:**

- **GET = Get data** (read-only, visible in URL)
- **POST = Post data** (used to create or update, data hidden in body)