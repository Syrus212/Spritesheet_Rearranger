import cv2
from PIL import Image, ImageDraw
from math import ceil

def create_sheet(PathToSpritesheet, anchor, path, order):

    if not(PathToSpritesheet):
        return

    # Load the image
    image = cv2.imread(PathToSpritesheet)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold to create binary mask
    _, threshold = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through contours and get bounding box coordinates
    bounding_boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        bounding_boxes.append((x, y, x + w, y + h))  # Format: (x1, y1, x2, y2)

    # Draw bounding boxes on the original image (optional)
    for x1, y1, x2, y2 in bounding_boxes:
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green rectangle
        #print(x1, y1, x2, y2)

    # Save or display the image with bounding boxes
    #cv2.imwrite(f'{path}Debug.png', image)

    # Caculate new image dimensions
    max_x = 0
    max_y = 0

    for x1, y1, x2, y2 in bounding_boxes:
        if (x2 - x1 ) > max_x:
            max_x = x2 - x1
        if (y2 - y1 ) > max_y:
            max_y = y2 - y1
    #print(max_x, max_y)

    # Specify image dimensions
    width = max_x * len(bounding_boxes)
    height = max_y

    # Create a new image with white background
    source_image = Image.open(PathToSpritesheet)

    new_image = Image.new("RGBA", (width + 2, height + 2), (0, 0, 0, 0))

    if order:
        sorted_bounding_boxes = sorted(bounding_boxes, key=lambda item: ((item[1] + (item[3] - item[1]) // 2), (item[0] + (item[2] - item[0]) // 2)))
    else:
        sorted_bounding_boxes = sorted(bounding_boxes, key=lambda item: ((item[0] + (item[2] - item[0]) // 2), (item[1] + (item[3] - item[1]) // 2)))
    c = -1

    for x1, y1, x2, y2 in sorted_bounding_boxes:
        c += 1

        adjusted_x = adjusted_y = 0

        if (x2 - x1) < max_x:
            match anchor:
                
                case 2 | 5 | 8:
                    adjusted_x = (max_x - (x2 - x1)) // 2

                case 3 | 6 | 9:
                    adjusted_x = max_x - (x2 - x1)

        if (y2 - y1) < max_y:
            match anchor:
                
                case 4 | 5 | 6:
                    adjusted_y = (max_y - (y2 - y1)) // 2
                    print(adjusted_y)

                case 7 | 8 | 9:
                    adjusted_y = max_y - (y2 - y1)

        region = source_image.crop((x1, y1, x2, y2))
        new_image.paste(region, (max_x * c + adjusted_x + 1, adjusted_y + 1))

    # Save the new image
    new_image.save(f'{path}Result.png')