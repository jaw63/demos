import cv2
import matplotlib.pyplot as plt

def pixelate_image(image_path, x_pixels, y_pixels, output_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Get the dimensions of the image
    height, width, _ = image.shape
    
    # Resize the image to the desired pixel size
    image2 = cv2.resize(image, (x_pixels, y_pixels), interpolation=cv2.INTER_LINEAR)
    
    # Resize the image back to its original size
    pixelated_image = cv2.resize(image2, (width, height), interpolation=cv2.INTER_NEAREST)
    
    # Save the pixelated image to a file
    cv2.imwrite(output_path, pixelated_image)
    
    # Display both images side by side using Matplotlib
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original Image')
    axs[0].axis('off')
    axs[1].imshow(cv2.cvtColor(pixelated_image, cv2.COLOR_BGR2RGB))
    axs[1].set_title('Pixelated Image')
    axs[1].axis('off')
    plt.show()
    
    return pixelated_image

pixelated_image = pixelate_image('flowers.jpg', 19, 19, 'flowers2.jpg')
