- This datatype basically represents what is the type of data stored inside the Array
- Array = Collection of similar datatypes
- We cannot include both Int & String into same Array's
- All the data should be same inside a Array they cannot be mixure
![[Pasted image 20250708104335.png]]
One such shit example by me 🤣🤣🤣
**It's different for C,C++ and Java**
- The basic difference because non existence of Pointer and all the allocation's are always continuous but in Java it's based on JVM so i chooses how to save it either continuous or not (cell's) and it's for sure that Heap Objects are not continuous Blocks in Java.
![[Pasted image 20250708113627.png]]
- DMA = Array object's may or may not be continuous (internally)
- JVM handling of Memory is different to that of C,C++
Index of an Array(Position of Array Content)
![[Pasted image 20250708121111.png]]
![[Pasted image 20250708113816.png]]
```
int[] rollno = new int[5];
```
==new is used to create an Object in the Heap Memory using DMA==
![[Pasted image 20250708114156.png]]
==VS==
null
when i explicitly mention = **System.out.println(arr[1]);**

-------

==Input of Array dynamically and Print it ==
So to the basic output and array cannot be printed instead
- It needs to converted from Arrayto.String(arr)
  Then the output will be visible
![[Pasted image 20250708114944.png]]
Following the same and printing using FOR EACH LOOP
![[Pasted image 20250708115851.png]]
[[Array Of Objects]]
[[2D Array]]

--------

Maximum of an array:
![[Pasted image 20250708220953.png]]
```
package krishnayt;  
  
public class maxArray {  
    public static void main(String[] args) {  
        int[] arr = {1,22,5,18,9,27};  
        int max = arr[0];  
        for(int i = 1;i<arr.length;i++)  
        {            if(arr[i]>max)  
            {                max=arr[i];  
            }  
        }        System.out.println(max);  
    }}
```
