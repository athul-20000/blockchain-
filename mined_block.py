import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Incremented to find a valid hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Combine block data, timestamp, nonce, and previous hash to generate a hash
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Target hash must start with 'difficulty' number of zeros
        target = '0' * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


# Example usage
difficulty = 2  # Define the difficulty level (number of leading zeros required in the hash)
block = Block(1, "Transaction Data", "Previous_Hash")
block.mine_block(difficulty)

print(f"Mined Block Hash: {block.hash}")
print(f"Nonce: {block.nonce}")