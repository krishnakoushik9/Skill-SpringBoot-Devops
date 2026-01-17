[[Day 2 Homework]]
- So this is related to Code which uses Post instead of GET cause POST let's read and write also now the file content in .txt has to be read and shown to user at that specific URL location
![[Pasted image 20250705224017.png]]
==Below is our code==
![[Pasted image 20250705224036.png]]
```package com.legion.learning.demo;  
import org.springframework.web.bind.annotation.PostMapping;  
import org.springframework.web.bind.annotation.RequestParam;  
import org.springframework.web.bind.annotation.RestController;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.IOException;  
  
@RestController  
  
public class FileUploader {  
        @PostMapping("/upload")  
        public String uploadFile(@RequestParam MultipartFile file) throws IOException {  
            return new String(file.getBytes());  
        }}
```
**==So i call this a success==**
