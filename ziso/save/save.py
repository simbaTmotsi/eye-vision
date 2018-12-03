def save(filename, file):
"""
------------------------
module for saving images
------------------------
"""

def save(filename, file):
    try:
        saved_file = cv2.imwrite(str(filename),file)
    except:
        print ("Please check the file path/name, there seems to be an error")
    """
    error checking
    """
    # in the event of an invalid file path this will be executed
    try:
        assert (saved_file) == None
        print ("Please check the file path/name, there seems to be an error saving the image")
    except Exception as errors:
        pass
    # returning the variable for re-use
    return saved_file