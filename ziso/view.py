import cv2

"""
function to print RGB images
"""
def color(image_or_frame):
    colot_image = cv2.cvtColor(image_or_frame, cv2.COLOR_BGR2RGB)# coverting from BGR scheme to RGB color format
    plt.axis("off")       # so as not to have the axis that show the scale of the images
    plt.imshow(RGB_image) # this is for displaying the image
    # [we didnt add plt() because we used the magic function %pylab inline]