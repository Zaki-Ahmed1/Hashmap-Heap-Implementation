# Course: CS261 - Data Structures
# Assignment: 5
# Student: Zaki Ahmed
# Description: Hash map data structure implementation.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Parameters: n/a
        Returns: n/a
        Description: Clear out the contents of the hash map.
        """
        for i in range(self.capacity):
            self.buckets.set_at_index(i, LinkedList())

        self.size = 0

    def get(self, key: str) -> object:
        """
        Parameters: String
        Returns: Value
        Description: Gets the value associated with a input string.
        """
        i = self.hash_function(key) % self.capacity
        node = self.buckets.get_at_index(i).contains(key)
        if node is None:
            return None
        else:
            return node.value

    def put(self, key: str, value: object) -> None:
        """
        Parameters: String, Object
        Returns: n/a
        Description: Inserts a key/value pair into the hash map.
        """
        # Hash the key to get the index
        i = self.hash_function(key) % self.capacity

        # If the key is already present in the map
        if self.contains_key(key):
            # Remove the exisiting (key, value) pair
            self.remove(key)

        # Insert the (key, value) pair in the i th bucket
        self.buckets.get_at_index(i).insert(key, value)

        # increase the size
        self.size += 1

    def remove(self, key: str) -> None:
        """
        Parameters: String
        Returns: n/a
        Description: Removes a particular key and its associated value from hash table.
        """
        i = self.hash_function(key) % self.capacity

        if self.contains_key(key):
            self.size -= 1
            self.buckets.get_at_index(i).remove(key)

    def contains_key(self, key: str) -> bool:
        """
        Parameters: String
        Returns: Boolean
        Description: Tells you if the hash table contains an input key.
        """
        # Iterate through all the buckets
        for i in range(self.capacity):
            if self.buckets.get_at_index(i).contains(key):
                return True
        return False

    def empty_buckets(self) -> int:
        """
        Parameters: n/a
        Returns: Integer
        Description: Tells you how many empty buckets are in a hash table.
        """
        count = 0
        for i in range(self.capacity):
            if self.buckets.get_at_index(i).length() == 0:
                count += 1
        return count

    def table_load(self) -> float:
        """
        Parameters: n/a
        Returns: Float
        Description: Tells you the load factor of the hash table.
        """
        m = self.capacity
        sum = 0
        for i in range(self.capacity):
            count = self.buckets.get_at_index(i).length()
            sum += count
        return sum / m

    def resize_table(self, new_capacity: int) -> None:
        """
        Parameters: Integer
        Returns: n/a
        Description: Resizes the hash table to an input capacity.
        """
        if new_capacity < 1:
            return
        new_buckets = DynamicArray()

        for _ in range(new_capacity):
            new_buckets.append(LinkedList())

        for i in range(self.capacity):
            ll = self.buckets.get_at_index(i)
            for node in ll:
                j = self.hash_function(node.key) % new_capacity
                new_buckets.get_at_index(j).insert(node.key, node.value)

        self.buckets = new_buckets
        self.capacity = new_capacity

    def get_keys(self) -> DynamicArray:
        """
        Parameters: n/a
        Returns: Dynamic Array
        Description: Returns all the keys in the hash table.
        """
        da = DynamicArray()
        for i in range(self.capacity):
            ll = self.buckets.get_at_index(i)
            for node in ll:
                da.append(node.key)
        return da


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
