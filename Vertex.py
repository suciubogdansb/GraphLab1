class Vertex:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("A vertex must be compared to a vertex")
        return self.__id == other.id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("A vertex must be compared to a vertex")
        return self.__id < other.id

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("A vertex must be compared to a vertex")
        return self.__id > other.id

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __hash__(self):
        return hash(self.__id)

    def __repr__(self):
        return f"{self.__id}"
