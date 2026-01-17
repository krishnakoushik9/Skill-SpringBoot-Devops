**Tomcat & Controller – Quick Overview**

- **Inbuilt Tomcat** means no need to install it separately. It starts automatically when you run your Spring Boot app.
    
- Tomcat is a **web server + servlet container** that handles HTTP requests and sends responses.
    
- A **Controller** handles those HTTP requests (like GET, POST) using annotations like `@RestController`.


---

**Steps to Initialize a REST App with Inbuilt Tomcat in VS Code**

1. **Install Requirements**
    
    - Install [Java JDK 17+](https://adoptium.net/)
        
    - Install [VS Code](https://code.visualstudio.com/)
        
    - Install VS Code Extensions:
        
        - _Extension Pack for Java_
            
        - _Spring Boot Extension Pack_
            
        - _Maven for Java_ (optional but helpful)
            
2. **Generate Spring Boot Project**
    
    - Use [https://start.spring.io/](https://start.spring.io/)
        
    - Select:
        
        - Project: Maven
            
        - Language: Java
            
        - Dependencies: Spring Web
            
    - Download and unzip the project.
        
    - Open it in VS Code.
        
3. **Structure**
    
    - `src/main/java/.../DemoApplication.java` → Main file to run
        
    - `src/main/java/.../controller/HelloController.java` → Your controller
        
4. **Add a Controller**