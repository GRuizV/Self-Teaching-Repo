from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

# BLANK = object()

class HashTable:

    def __init__(self, capacity=int()):

        self.pairs = capacity * [None]


    def __len__(self):

        return len(self.pairs)


    def _index(self, key):

        return hash(key) % len(self)


    def __setitem__(self, key, value):
        
        self.pairs[self._index(key)] = Pair(key, value)

    
    def __getitem__(self, key):
        
        pair = self.pairs[self._index(key)]

        if pair is None:
            raise KeyError(key)

        return pair.value
    

    def __contains__(self,key):

        try:
            self[key]
        
        except KeyError:
            return False
        
        else:
            return True


    def get(self, key, default=None):

        try:
            return self[key]
        
        except KeyError:
            return default


    def __delitem__(self, key):
        
        # #Initially
        # self.pairs[self._index(key)] = None

        if key in self:

            #Refactored
            self[key] = None

        #This is possible because by assigning with ['key'] it
        #delegates the assignment to the __setitem__() directly

        else:

            raise KeyError(key)























