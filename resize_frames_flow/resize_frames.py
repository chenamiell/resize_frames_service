import time

import cv2

import settings


def resize_image(image):
    """
    :param image:
    :return json report of the resized image:
    """
    start_time = time.time()
    scale_percent = settings.SCALE_PERC
    width = int(image.img.shape[1] * scale_percent / 100)
    height = int(image.img.shape[0] * scale_percent / 100)
    dim = (width, height)
    image_umat = cv2.UMat(image.img)
    resized_umat = cv2.resize(image_umat, dim, interpolation=cv2.INTER_AREA)
    resized_image = resized_umat.get()
    cv2.imwrite(f'{settings.RESIZED_IMAGES_PATH}\{str(image)}_resized.jpg', resized_image)
    end_time = time.time()
    return {
        'image_name':  str(image),
        'time_to_process': end_time - start_time,
        'path_to_resized_frame': settings.RESIZED_IMAGES_PATH,
        'original_dim': image.img.shape,
        'resized_dim': resized_image.shape
    }




