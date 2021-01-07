# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        level_left = list()
        level_right = list()

        def dfs(level, pos, root):
            if not root:
                return
            if len(level_left) <= level:
                level_left.append(pos)
            else:
                level_left[level] = min(level_left[level], pos)
            if len(level_right) <= level:
                level_right.append(pos)
            else:
                level_right[level] = max(level_right[level], pos)
            dfs(level + 1, pos - 1 / (2 ** level), root.left)
            dfs(level + 1, pos + 1 / (2 ** level), root.right)

        dfs(0, 0, root)
        return max([int((level_right[i] - level_left[i]) / 2 ** (2 - i)) + 1 for i in range(len(level_left))])


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);

            ret = Solution().widthOfBinaryTree(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()