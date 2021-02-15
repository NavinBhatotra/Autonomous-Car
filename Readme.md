Author Name:- Navin Bhatotra

Features of Autonomous Car:-
1) Self driving between lane
2) Traffic Signal rule base system
3) Automatic Head Light On and Off on the basic of the Light in surrounding
4) Collision Avoidance
5) Stop at the Stop Sign

Change IP Address as your Computer IP Address where it is written like this "192.168.31.120" in code.

Folder Description:-
1)computer :- In "computer" folder contain file which is to be run in computer/laptop.
2)raspberryPi :- In "raspberryPi" folder contain file which is to be run in raspberry Pi 3 b+ which is used.
3)computer/cascade_xml :- In this folder "cascade_xml" which have a cascade file for stop sign and trafic light.
4)computer/saved_model :- In this folder "saved_model" which have a neural network trained model which is use for self driving in action.
5)computer/training_data :- In this folder "training_data" which have a collected training data with extion of .npz files.

For Collecting Data:-
Step For Collecting Data
1)run "collect_training_data.py" in computer
2)run "stream_client.py" in raspberryPi and then run "client.py" in raspberryPi

For Neural Network Model Training:-
Step For Model Training
1)run Run "model_training.py" to train a neural network model.
After training, model will be saved into newly created folder in save_model

Full Self Driving:-
Step For Fully Self Driving
1)run "rc.py" file in computer 
2)run "launch.py" in raspberry Pi 
