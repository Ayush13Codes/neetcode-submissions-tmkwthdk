class TrieNode:
    def __init__(self):
        self.children = {}  # char -> child node
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            # Base case: reached end of word
            if i == len(word):
                return node.is_word

            c = word[i]
            # Char is regular
            if c != ".":
                if c not in node.children:
                    return False
                else:
                    return dfs(i + 1, node.children[c])
            # Wildcard-Try all possible children
            else:
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

        return dfs(0, self.root)
