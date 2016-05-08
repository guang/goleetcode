package main

import (
	"fmt"
	"math"

	"tree"
)

func trackDepth(node *tree.TreeNode, depth int) int {

	current_depth := depth

	if node.Left != nil {
		current_depth = int(math.Max(float64(trackDepth(node.Left, depth+1)), float64(depth)))
	}

	if node.Right != nil {
		current_depth = int(math.Max(float64(trackDepth(node.Right, depth+1)), float64(current_depth)))
	}

	return current_depth
}

func maxDepth(root *tree.TreeNode) int {

	if root == nil {
		return 0
	}

	return trackDepth(root, 1)
}

func main() {
	c := tree.TreeNode{Val: 14, Left: nil, Right: nil}
	b := tree.TreeNode{Val: 13, Left: &c, Right: nil}
	a := tree.TreeNode{Val: 12, Left: nil, Right: nil}

	root := tree.TreeNode{Val: 11, Left: &a, Right: &b}

	fmt.Println(maxDepth(&root))
}
