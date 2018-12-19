import numpy as np
import cv2

# import an image
def imprt_image():
	license_plate_image = cv2.imread('license_plate_1')
	return license_plate_image


def show_image(license_plate_image):
	cv2.imshow('License Plate',license_plate_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def create_csv_file():
	


def main():
	

if __name__ == "__main__":
	main()