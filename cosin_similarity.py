from PIL import Image
from numpy import average, linalg, dot
import matplotlib
import matplotlib.pyplot as plt


def get_thumbnail(image, size=(180, 120), greyscale=False):
    image = image.resize(size, Image.ANTIALIAS)  # antialias抗锯齿
    if greyscale:
        image = image.convert('L')
    return image


def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thumbnail(image1)
    image2 = get_thumbnail(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    res = dot(a / a_norm, b / b_norm)
    return res


if __name__ == '__main__':

    pictures = []
    count = 0

    for i in range(150):
        image1 = Image.open('pictures/{}.jpg'.format(i))
        image2 = Image.open('pictures/{}.jpg'.format(i + 1))
        cosin = image_similarity_vectors_via_numpy(image1, image2)
        print(cosin)
        pictures.append(cosin)

        if cosin<0.88:
            count = count+1

        if i == 148:
            break
    print(pictures)

    figure1 = plt.figure(num='cosin_similarity')
    ax1 = figure1.add_subplot()
    ax1.set_title('cosin')
    plt.xlabel('x')
    plt.ylabel('y')
    # x = list(range(len(pictures)))
    # y = pictures
    # 散点图
    # ax1.scatter(x, y, c = 'g', marker = 'o')
    # plt.plot(x, y, 'ro')

    x = pictures
    # 直方图
    plt.hist(x, bins=150)
    plt.show()
    print(count)


# 最后可以选择阈值为0.88, count为58，原帧数为150