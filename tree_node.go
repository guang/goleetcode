package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deserialize(str string) *TreeNode {
	if strings.HasPrefix(str, "[") && strings.HasSuffix(str, "]") {
		strArr := strings.Split(str[1:len(str)-1], ",")

		var nodes []*TreeNode
		var kids []*TreeNode
		for _, val := range strArr {
			if val != "nil" {
				intVal, _ := strconv.Atoi(val)
				currNode := &TreeNode{Val: intVal, Left: nil, Right: nil}

				nodes = append(nodes, currNode)
				kids = append([]*TreeNode{currNode}, kids...)
			} else {
				nodes = append(nodes, nil)
				kids = append([]*TreeNode{nil}, kids...)
			}
		}

		var root *TreeNode
		root, kids = kids[len(kids)-1], kids[:len(kids)-1]

		for _, node := range nodes {
			if node != nil {
				if len(kids) != 0 {
					node.Left, kids = kids[len(kids)-1], kids[:len(kids)-1]
				}
				if len(kids) != 0 {
					node.Right, kids = kids[len(kids)-1], kids[:len(kids)-1]
				}
			}
		}
		return root
	} else {
		fmt.Println("String input must be encapsulated by [ and ] e.g. [1,2,3]")
		os.Exit(1)
	}
	return nil
}

func printTree(root *TreeNode) {
	if root != nil {
		currLevel := []*TreeNode{root}
		emptyLevel := false

		for !emptyLevel {
			var nextLevel []*TreeNode
			var levelVal []string
			emptyLevel = true

			for _, node := range currLevel {
				if node == nil {
					levelVal = append(levelVal, "nil")
					nextLevel = append(nextLevel, nil, nil)
				} else {
					levelVal = append(levelVal, strconv.Itoa(node.Val))
					nextLevel = append(nextLevel, node.Left, node.Right)
					emptyLevel = false
				}
			}

			if !emptyLevel {
				fmt.Println(strings.Join(levelVal, " "))
			}

			currLevel = nextLevel
		}
	}
}

func main() {
	root := deserialize("[1,2,3,4,nil,6,7,8,9,10]")
	printTree(root)
}
