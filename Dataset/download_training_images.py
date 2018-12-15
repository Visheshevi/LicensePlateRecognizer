import urllib.request
import json


def display_message(message):
	print(message)

def load_data():
	with open('Indian_Number_plates.json') as f:
		data = [json.loads(line) for line in f]
	return data

def download_dataset(data):
	count = 0
	for car_data in data:
		car_image_link = car_data["content"]
		count = count + 1
		current_info = "Downloading image " + str(count)
		display_message(current_info)
		image_name = "license_plate_" + str(count)
		urllib.request.urlretrieve(car_image_link,image_name)
	display_message("All images downloaded downloaded. Rest of the application is for you to implement. Good Day or night.")



def main():
	dataset = load_data()
	download_dataset(dataset)

if __name__ == "__main__":
	main()