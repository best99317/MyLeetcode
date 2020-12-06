class ThroneInheritance:

    def __init__(self, kingName: str):
        self.curOrder = [kingName]
        self.dic = dict()
        self.dic[kingName] = -1

    def birth(self, parentName: str, childName: str) -> None:
        ind = 0
        while self.dic[parentName] != -1:
            parentName = self.curOrder[self.dic[parentName]]
            ind = self.dic[parentName] + 1
        self.curOrder.insert(ind + 1, childName)
        self.dic[parentName] = ind + 1
        self.dic[childName] = -1

    def death(self, name: str) -> None:
        return None

    def getInheritanceOrder(self) -> [str]:
        return self.curOrder


# Your ThroneInheritance object will be instantiated and called as such:
t = ThroneInheritance("king") # order: king
t.birth("king", "andy")  # order: king > andy
t.birth("king", "bob")  # order: king > andy > bob
t.birth("king", "catherine")  # order: king > andy > bob > catherine
t.birth("andy", "matthew")  # order: king > andy > matthew > bob > catherine
t.birth("bob", "alex")  # order: king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha")  # order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder()  # return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
# t.death("bob")  # order: king > andy > matthew > bob > alex > asha > catherine
# t.getInheritanceOrder()  # return ["king", "andy", "matthew", "alex", "asha", "catherine"]