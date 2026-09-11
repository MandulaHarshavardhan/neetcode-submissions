class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> [prev_key, next_key, value]

        self.LEFT, self.RIGHT = -1, -2   # sentinel keys (never real keys)
        self.cache[self.LEFT] = [None, self.RIGHT, None]
        self.cache[self.RIGHT] = [self.LEFT, None, None]

    def _remove(self, key):
        prev_k, next_k, _ = self.cache[key]
        self.cache[prev_k][1] = next_k
        self.cache[next_k][0] = prev_k

    def _insert(self, key):
        prev_k = self.cache[self.RIGHT][0]
        self.cache[prev_k][1] = key
        self.cache[self.RIGHT][0] = key
        self.cache[key][0] = prev_k
        self.cache[key][1] = self.RIGHT

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key][2]
        self._remove(key)
        self._insert(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(key)
        self.cache[key] = [None, None, value]
        self._insert(key)

        if len(self.cache) - 2 > self.cap:  # -2 excludes the two sentinels
            lru_key = self.cache[self.LEFT][1]
            self._remove(lru_key)
            del self.cache[lru_key]