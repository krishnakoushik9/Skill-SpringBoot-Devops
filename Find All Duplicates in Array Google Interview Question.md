![[Pasted image 20250713064655.png]]
Link:https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/1695763623/

![[Pasted image 20250713064759.png]]

```
class Solution {

public List<Integer> findDuplicates(int[] nums) {

List<Integer> result = new ArrayList<>();

  

int i = 0;

while (i < nums.length) {

int correct = nums[i] - 1;

if (nums[i] != nums[correct]) {

swap(nums, i, correct);

} else {

i++;

}

}

  

for (int j = 0; j < nums.length; j++) {

if (nums[j] != j + 1) {

result.add(nums[j]);

}

}

  

return result;

}

public void swap(int[] arr, int a, int b) {

int temp = arr[a];

arr[a] = arr[b];

arr[b] = temp;

}

}
```
