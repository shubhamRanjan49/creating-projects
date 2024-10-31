import cv2

# Load the image
image = cv2.imread("rand.jpeg", cv2.IMREAD_UNCHANGED)

# Display the original image
cv2.imshow("Original Image", image)

# Resize the image
scale_percent = 50  # percentage of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dsize = (width, height)

# Resize the image
output = cv2.resize(image, dsize)

# Save the resized image
cv2.imwrite(r'C:\Users\HP\Downloads\creating-projects\image resizer\rand_resized.jpeg', output)

# Display the resized image
cv2.imshow("Resized Image", output)

# Wait until a key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
