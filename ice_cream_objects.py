class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops(*flavor1):
    scoops = []
    for arg in flavor1:
        scoops.append(Scoop(arg))

    for scoop in scoops:
        print(scoop.flavor)

create_scoops('vanilla', 'chocolate', 'epic flavor', 'pineapple', 'lemon', 'joghurt', 'strawberry')