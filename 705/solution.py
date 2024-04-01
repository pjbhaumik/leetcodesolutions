class MyHashSet(object):

    def __init__(self):
        self.list = []

        
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            self.list.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            self.list = [x for x in self.list if x != key]
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.list: return True
        else: return False
        