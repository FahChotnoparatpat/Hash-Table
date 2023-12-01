from collections.abc import MutableMapping
from collections import namedtuple

HashPair = namedtuple('HashPair', ['key', 'val', 'valid'])
class Hashtable(MutableMapping):
    # polynomial constant, used for _hash
    P_CONSTANT = 37

    def __init__(self, capacity, default_value, load_factor, growth_factor):
        self._items = Hashtable._create_empty_table(capacity)
        self.capacity = capacity
        self.default_value = default_value
        self.load_factor = load_factor
        self.growth_factor = growth_factor
        self.count = 0

    @staticmethod
    def _create_empty_table(capacity):
        """
        A static method to initialize an "empty" hashtable.
        The keys will be initialized from 0 to (capacity - 1) and the value will be initialized to None
        with validity of data as False.
        """
        items = [HashPair(key=None, val=None, valid=False)] * capacity
        return items

    def _hash(self, key):
        """
        This method takes in a string and returns an integer value
        between 0 and self.capacity.

        This particular hash function uses Horner's rule to compute a large polynomial.

        See https://www.cs.umd.edu/class/fall2019/cmsc420-0201/Lects/lect10-hash-basics.pdf
        """
        val = 0
        for letter in key:
            val = self.P_CONSTANT * val + ord(letter)
        return val % self.capacity

    def __setitem__(self, key, val):
        self._setitem_norehash(key, val)
        
        if len(self) / self.capacity >= self.load_factor:
            self._rehash()

    def _setitem_norehash(self, key, val):
        key_hash = self._hash(key)
        
        for offset in range(self.capacity):
            # Performs linear probing, starting with the original hash
            test_index = (key_hash + offset) % self.capacity        
            # If the slot is filled with deleted item, overwrite key, value and increment the count          
            if not self._items[test_index][2]:      # Check if bool value is False
                self._items[test_index] = HashPair(key, val, True)
                self.count += 1
            # If the key already exists, rewrite the key, value
            if self._items[test_index][0] == key:       # Check if key = key
                self._items[test_index] = HashPair(key, val, True)
                break       # Successfully inserted - break out of the loop
    
    def __getitem__(self, key):
        key_hash = self._hash(key)
        for offset in range(self.capacity):
            # Performs linear probing, starting with the original hash
            test_index = (key_hash + offset) % self.capacity    
            # If bool value is True and key exists, return value 
            if self._items[test_index][2] and self._items[test_index][0] == key:
                return self._items[test_index][1]
            # Return a default value once an empty slot is found (key = None)
            elif self._items[test_index][1] is None:
                return self.default_value
                

    def __delitem__(self, key):
        key_hash = self._hash(key)
        for offset in range(self.capacity):
            # Performs linear probing, starting with the original hash
            test_index = (key_hash + offset) % self.capacity   
            # If bool value is True and key = key, change bool value to False and decrement the count 
            if self._items[test_index][2] and self._items[test_index][0] == key:
                self._items[test_index] = HashPair(key, self._items[test_index][1], False)
                self.count -= 1
                return
            #If an empty slot is found (key = None), raise error
            elif self._items[test_index][1] is None:
                raise KeyError(f"Error: The specified key {key} does not exist in the hashtable.")
        
    def __len__(self):
        return self.count

    def __iter__(self):
        """
        You do not need to implement __iter__ for this assignment.
        This stub is needed to satisfy `MutableMapping` however.)

        Note, by not implementing __iter__ your implementation of Markov will
        not be able to use things that depend upon it,
        that shouldn't be a problem but you'll want to keep that in mind.
        """
        raise NotImplementedError("__iter__ not implemented")

    def _rehash(self):
        new_table = Hashtable(self.growth_factor * self.capacity, self.default_value, self.load_factor, self.growth_factor)
        for item in self._items:
            if item[0] != None:
                new_table._setitem_norehash(item[0], item[1])
        
        self.capacity = new_table.capacity
        self._items = new_table._items


