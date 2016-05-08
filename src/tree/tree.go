package tree

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func Deserialize(str string) *TreeNode {
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

func FindDepth(node *TreeNode, depth int) int {

	current_depth := depth

	if node.Left != nil {
		current_depth = int(math.Max(float64(FindDepth(node.Left, depth+1)), float64(depth)))
	}

	if node.Right != nil {
		current_depth = int(math.Max(float64(FindDepth(node.Right, depth+1)), float64(current_depth)))
	}

	return current_depth

}

func GetDepth(root *TreeNode) int {

	if root == nil {
		return 0
	}

	return FindDepth(root, 1)

}

func CalcIndents(root *TreeNode) []int {
	numLevels := GetDepth(root)

	var (
		indents []int
		cnt     int
	)

	if numLevels >= 1 {
		indents = append(indents, 0)
	}

	if numLevels >= 2 {
		indents = append([]int{1}, indents...)
	}

	if numLevels > 2 {
		cnt = numLevels - 2
		x := 1
		var otherIndents []int

		for cnt > 0 {
			x = 2 * (x + 1)
			otherIndents = append([]int{x}, otherIndents...)
			cnt -= 1
		}
		indents = append(otherIndents, indents...)
	}
	return indents
}

func InitStrSlice(size int, str string) []string {
	strSlice := make([]string, size)
	for idx, _ := range strSlice {
		strSlice[idx] = str
	}
	return strSlice
}

func PrintTree(root *TreeNode) {

	if root != nil {
		indents := CalcIndents(root)

		currLevel := []*TreeNode{root}
		emptyLevel := false
		levelNum := 0

		for !emptyLevel {
			var nextLevel []*TreeNode
			var levelVal []string
			indentSlice := []string{""}
			emptyLevel = true

			if indents[levelNum] != 0 {
				indentSlice = InitStrSlice(indents[levelNum], " ")
			}

			levelVal = append(indentSlice, levelVal...)
			for _, node := range currLevel {
				if node == nil {
					if levelNum >= 1 {
						spaceSlice := InitStrSlice(indents[levelNum-1]+1, " ")
						levelVal = append(levelVal, "*", strings.Join(spaceSlice, ""))
					} else {
						levelVal = append(levelVal, "*")
					}
					nextLevel = append(nextLevel, nil, nil)
				} else {
					if levelNum >= 1 {
						spaceSlice := InitStrSlice(indents[levelNum-1]+1, " ")
						levelVal = append(levelVal, strconv.Itoa(node.Val), strings.Join(spaceSlice, ""))
					} else {
						levelVal = append(levelVal, strconv.Itoa(node.Val))
					}

					nextLevel = append(nextLevel, node.Left, node.Right)
				}
			}

			fmt.Println(strings.Join(levelVal, ""))

			for _, val := range nextLevel {
				emptyLevel = emptyLevel && (val == nil)
			}

			currLevel = nextLevel
			levelNum += 1
		}

	}
}
