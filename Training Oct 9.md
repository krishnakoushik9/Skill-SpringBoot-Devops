[[Training]]
Array Sorted (Increasing Order)
- To Insert Minimum Element - O(n) 
- To Access - O(1)
Binary Search Tree 
- Minimum Element Access - O(log n)
- Insertion of Minimum Element - O(log n)
- Insertion at Maximum Position - O(log n)
- Deletion of Minimum Position Value - O(log n)
![[Pasted image 20251009093336.png]]
Example with a BST

----
# Binary Tree

![[Pasted image 20251009095834.png]]

---
## How to find if a tree is Complete Binary Tree
```
class GfG {
    boolean isCompleteBT(Node root) {
        // add code here.
        int countNode = noOfNode(root);
        int pos = 0;
        boolean ans = isComplete(root,pos,countNode);
        return ans;
    }
    public static boolean isComplete(Node root,int pos,int countNode){
        if(root == null){
            return true;
        }
        if(pos>=countNode){
            return false;
        }
        return (isComplete(root.left,2*pos+1,countNode) && isComplete(root.right,2*pos+2,countNode));
    }
    public static int noOfNode(Node root){
	    if(root == null){
	        return 0;
	    }
	    return (1 + noOfNode(root.left) + noOfNode(root.right));
	}
}
```
![[Pasted image 20251009122406.png]]
---
