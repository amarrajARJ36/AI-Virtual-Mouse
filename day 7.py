import cv2

#User Input: The program prompts the user to enter the path of the image file they want to resize.
i = input("Enter the path of the image you want to resize")

#mage Loading: It reads the image from the specified path using cv2.imread().
image = cv2.imread(i)
print(image.shape)

#Resize Dimensions: The user is asked to provide the new width and height for the image.
w,h = map(int,input('Enter the new dimension: '  'width , height').split(','))

#Image Resizing: The image is resized to the specified dimensions using cv2.resize().
resized_image = cv2.resize(image,(w,h)) 

#Display:Both the original and resized images are displayed using cv2.imshow().
cv2.imshow('image',image)
cv2.imshow('resized image',resized_image)
    
#Save or Close: If the user presses the "s" key, the resized image is saved to a specified location. 
# If any other key is pressed, the program closes the display windows.
wait = cv2.waitKey()
if wait == ord('s'):
    cv2.imwrite('/Users/amarraj/Desktop/Srishti/dog_resized.jpeg', resized_image)
    print("The resized image is saved as 'dog_resized' ")

cv2.destroyAllWindows()