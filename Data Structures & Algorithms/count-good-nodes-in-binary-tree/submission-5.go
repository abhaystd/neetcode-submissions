/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Pair struct {
    Node  *TreeNode
    V     int
}

type Queue struct{
    element []Pair
}

func (q *Queue) enqueue(p Pair){
    q.element = append(q.element,p)
}

func (q *Queue) dequeue() Pair{
    if len(q.element) == 0{
        return Pair {}
    }

    res :=q.element[0]
    q.element=q.element[1:]
    return res
}

func (q *Queue) queSize() int{
    return len(q.element)
}

func goodNodes(root *TreeNode) int {
    if root == nil{
        return 0
    }
    var res int
    q := Queue{}

    q.enqueue(Pair{Node:root,V:math.MinInt})

    for q.queSize()>0{

        front:=q.dequeue()
        curr, maxVal:=front.Node, front.V

        if curr.Val >= maxVal{
            res++
            maxVal = curr.Val
        }
        if curr.Left != nil{
            q.enqueue(Pair{Node:curr.Left,V:maxVal})
        }
        if curr.Right !=nil{
            q.enqueue(Pair{Node:curr.Right,V:maxVal})
        }
        
    }
    return res
}
