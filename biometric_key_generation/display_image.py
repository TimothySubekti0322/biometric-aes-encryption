import matplotlib.pyplot as plt

# Fungsi untuk menampilkan gambar
def display_image(title, image):
    plt.figure()
    plt.title(title)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()