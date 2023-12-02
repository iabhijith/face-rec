import base64


def image_to_b64(img_path):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


def save_b64(image_b64, filename):
    with open(filename, "wb") as fh:
        fh.write(image_b64)


if __name__ == "__main__":
    img1_path = "../data/train/image1.jpeg"
    img2_path = "../data/train/image2.jpeg"

    test_img_path = "../data/test/image1.jpeg"

    img1_b64 = image_to_b64(img1_path)
    img2_b64 = image_to_b64(img2_path)
    test_b64 = image_to_b64(test_img_path)

    save_b64(img1_b64, "../data/b64/img1_b64.txt")
    save_b64(img2_b64, "../data/b64/img2_b64.txt")
    save_b64(test_b64, "../data/b64/test_b64.txt")
