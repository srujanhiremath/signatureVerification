import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

file1 = 'sign1.jpeg'
file2 = 'sign4.jpeg'

img1 = cv2.imread(file1)
img2 = cv2.imread(file2)

if img1 is None or img2 is None:
    print('Error: One or both files could not be read. ' \
    'Please check the filenames and try again.')
    exit(1)

# Convert to grayscale
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Resize images to the same size
height = min(img1_gray.shape[0], img2_gray.shape[0])
width = min(img1_gray.shape[1], img2_gray.shape[1])
img1_resized = cv2.resize(img1_gray, (width, height))
img2_resized = cv2.resize(img2_gray, (width, height))

# Compute SSIM
similarity, _ = ssim(img1_resized, img2_resized, full=True)

print(f'Similarity score: {similarity:.2f}')

# Threshold for verification
THRESHOLD = 0.75
if similarity >= THRESHOLD:
    print('Result: Original and Verified')
else:
    print('Result: Forged')