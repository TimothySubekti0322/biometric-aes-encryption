import numpy as np

# Segmentasi dan Normalisasi Citra Sidik Jari
def segment_and_normalize(image, block_size=16, threshold=0.10):
    rows, cols = image.shape
    segmented_image = np.zeros_like(image)
    normalized_image = np.zeros_like(image)
    
    for i in range(0, rows, block_size):
        for j in range(0, cols, block_size):
            block = image[i:i+block_size, j:j+block_size]
            variance = np.var(block)
            
            if variance < threshold:
                segmented_image[i:i+block_size, j:j+block_size] = 0
            else:
                segmented_image[i:i+block_size, j:j+block_size] = block
                
    mean = np.mean(segmented_image)
    stddev = np.std(segmented_image)
    
    # Normalisasi menggunakan mean dan stddev
    normalized_image = ((segmented_image - mean) / stddev) * 128 + 128
    normalized_image = np.clip(normalized_image, 0, 255)
    normalized_image = normalized_image.astype(np.uint8)
    
    return segmented_image, normalized_image