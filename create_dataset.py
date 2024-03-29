import cv2

# Image label
labels = map(lambda x: x[2:-1], open("labels.txt", "r").readlines())

for label in labels:
    camera = cv2.VideoCapture(0)
    # cv2.namedWindow(f"Image Capture: {label}")
    image_count = 0
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture frame")
            break
        cv2.imshow(f"Image Capture: {label}", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            #   Press Esc
            print(f"Complete {label}")
            break
        elif k%256 == 32:
    #         Press Space
            image_name = f"dataset/{label}_{image_count}.png"
            cv2.imwrite(image_name, frame)
            print(f"{image_name} written ...")
            image_count += 1
    camera.release()
    cv2.destroyAllWindows()


