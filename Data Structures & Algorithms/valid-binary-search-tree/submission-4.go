/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValid(root *TreeNode, l int, r int) bool{
    if root == nil{
        return true
    }

    if !(l<root.Val && root.Val<r){
        return false
    }

    return isValid(root.Left,l,root.Val)&&isValid(root.Right,root.Val,r)
}
func isValidBST(root *TreeNode) bool {
    if root == nil{
        return true
    }

	return isValid(root,math.MinInt,math.MaxInt)

}
