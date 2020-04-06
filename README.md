## INSTALLATION GUIDE

1. Make sure `Python 3.x` and `pip` are installed. To check run the following commands:
	* `python3 --version`
	* `pip --version`
    If they do not output a version, install whichever is not installed.

2. Make sure `virtualenv` is installed. To install run the following commands and create a vritualenv to run the code:
	* `sudo apt install virtualenv`
	* `virtualenv --version`
	* `cd <the path of the project directory>`
	* `virtualenv -p $(which python3) ./`
	* `source ./bin/activate`
3. To run the program correctly, install all the requirements indicated in `requirements.txt` file with the following command:
	* `pip install -r requirements.txt`
4. To predict an image, we need weights for our model. We have a file `disease.json` which is our trained weights. We specify the weights file using `-w`. The image is specified using `-i`.
	* `python3 main.py -w <weights file> -i <image>`
