import cv2


def preprocessing2(receipt_path, output_path_preprocessed):
    # Read Image
    receipt = cv2.cvtColor(cv2.imread(receipt_path), cv2.COLOR_BGR2RGB)
    # Grayscale
    receipt_processed = cv2.cvtColor(receipt, cv2.COLOR_RGB2GRAY)
    # Gaussian blur
    receipt_processed2 = cv2.GaussianBlur(receipt_processed, (5, 5), 0)
    # Threshold
    receipt_processed3 = cv2.adaptiveThreshold(
        receipt_processed2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 30
        )
    # Write Image
    cv2.imwrite(output_path_preprocessed, receipt_processed3) 