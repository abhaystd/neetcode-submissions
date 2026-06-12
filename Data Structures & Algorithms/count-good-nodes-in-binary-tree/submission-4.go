/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func countGoodNode(root *TreeNode, v int) int {
    if root == nil{
        return 0
    }
    var res int
    if root.Val>=v{
        res=1
    }
    v=max(root.Val,v)
    res += countGoodNode(root.Left,v)
    res += countGoodNode(root.Right,v)
    return res
}

func goodNodes(root *TreeNode) int {
    if root == nil{
        return 0
    }

    return countGoodNode(root,root.Val)
}
