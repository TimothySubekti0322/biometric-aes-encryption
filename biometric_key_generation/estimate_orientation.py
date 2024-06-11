import numpy as np
import math

def estimate_orientation(normalized_image, block_size=16):
    rows, cols = normalized_image.shape
    orientation_image = np.zeros_like(normalized_image, dtype=float)
    
    for i in range(0, rows, block_size):
        for j in range(0, cols, block_size):
            block = normalized_image[i:i+block_size, j:j+block_size]
            vx, vy = 0, 0
            
            if block.shape[0] < block_size or block.shape[1] < block_size:
                continue
            
            for u in range(block_size - 1):
                for v in range(block_size - 1):
                    vx += 2 * (int(block[u, v+1]) - int(block[u, v])) * (int(block[u+1, v]) - int(block[u, v]))
                    vy += (int(block[u, v+1]) - int(block[u, v])) ** 2 - (int(block[u+1, v]) - int(block[u, v])) ** 2
            
            if vx != 0:
                orientation_image[i:i+block_size, j:j+block_size] = 0.5 * math.atan2(vy, vx)
                
    return orientation_image