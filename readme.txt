#Prepare the setup.sh to enable exectuion
chmod +x setup.sh

#Run the setup file
bash setup.sh

#Enable a virtual environment
source licenceplate_env/bin/activate
python3 -m venv licenceplate_env


#Use the below approach run the model and to provide an image as an argument.
python3 recognize_plate.py /home/admin/tesla_car.jpg

#Include the optional confidence threshold.
python3 recognize_plate.py /home/admin/tesla_car.jpg 0.6
