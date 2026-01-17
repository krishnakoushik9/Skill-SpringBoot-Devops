- You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.
---
==**Leet-Code Hard**==
it's Cyclic Sort
**Example 2:**
**Input:** nums = [3,4,-1,1]
**Output:** 2
**Explanation:** 1 is in the array but 2 is missing.

Solution Approach should be :-
- Ignore any negative numbers and think once again what is the smallest integer which is positive?
- It's integer "1" right so what so let's just say that the given array is [1,2,0] that sounds like 1 to 3 (1 to n) is the way cyclic sort works so number 3 is missing so just return that output
- Start checking from 1 and move on to next 
- Again for example nums = [7,8,9,11,12] the smallest integer 1 doesn't exist so return 1.
- Ignore any number greater than n also

---
![[Pasted image 20250713090224.png]]

---
![[Pasted image 20250713091147.png]]

---
```
class Solution {

public int firstMissingPositive(int[] arr){

int i = 0;

int n = arr.length;

while(i < n){

int correct = arr[i]-1;

if(arr[i] > 0 && arr[i]<= n && arr[i] != arr[correct]){

swap(arr,i,correct);

}else{

i++;

}

}

for(int index = 0;index< arr.length;index++){

if(arr[index] != index + 1){

return index + 1;

}

}

return arr.length + 1;

}

public static void swap(int[] arr, int a, int b){

int temp = arr[a];

arr[a] = arr[b];

arr[b] = temp;

}

}
```

**LeetCode Hard Solved with little changes to Cyclic Sort**
![[Pasted image 20250713091335.png]]
