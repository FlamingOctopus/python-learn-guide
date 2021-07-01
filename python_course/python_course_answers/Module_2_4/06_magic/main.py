class Storm:
    pass


class Steam:
    pass


class Dirt:
    pass


class Lightning:
    pass


class Dust:
    pass


class Lava:
    pass


class Water:
    def __add__(self, obj):
        if isinstance(obj, Air):
            return Storm()
        elif isinstance(obj, Fire):
            return Steam()
        elif isinstance(obj, Earth):
            return Dirt()
        else:
            print("Несовместимые элементы")
        return


class Air:
    def __add__(self, obj):
        if isinstance(obj, Fire):
            return Lightning()
        elif isinstance(obj, Earth):
            return Dust()
        else:
            print("Несовместимые элементы")
        return


class Fire:
    def __add__(self, obj):
        if isinstance(obj, Earth):
            return Lava()
        else:
            print("Несовместимые элементы")
        return


class Earth:
    pass


water = Water()
air = Air()
fire = Fire()
earth = Earth()
print(water + air)
print(water + fire)
print(water + earth)
