# SaniText Text Editor

![Output Image](https://github.com/anmolpant/SaniText/blob/master/Screenshots/sanitext.png)

SaniText is a full fledged text editing software developed in python using the tkinter framework for the GUI. Deriving it's name from the 'new normal' version of 'clean text', Santitext boasts of an interactive window where users can enter text, change text style, color and properties, create, save and edit files, in this one of a kind, all in one, versatile text editoring software. The text editor also houses six diverse color themes and hence incorporates all the functionalities a basic text editor should have and even outperforms them by taking it up a notch incorporating features like find and replace, text alignments and customizable text and background colors according to the preference of the user.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

On my local machine, I've used: 
python: 3.8, 
tkinter: 8.6,
cx_freeze: cx_Freeze-6.2-cp37-cp37m-win32.whl

### Installing

Fork this repo and clone it to your local machine, the repository contains the Windows Installer Application Setup file, namely *SaniText Text Editor-0.01-win32.msi* in the *dist* folder, running which as administrator, will install the software on your machine for testing purposes.

For development purposes, clone the repository on your local machine and install the latest python version along with tkinter. 

for installing tkinter run:

```
$directoryName/Path/ pip3 install tkinter
```

After installing python and the concerned dependencies, open and run the python file 'sanitext.py' on any IDE.

```
$directoryName/Path/ py sanitext.py
```
A development version of the software will be up and running on your system.

## Application UI

Default User Interface (Color theme, Text size and color, etc.)

![Output Image](https://github.com/anmolpant/SaniText/blob/master/Screenshots/screenshot1.PNG)

Changing font style, size, color and weight and switching the mode to dark mode.

![Output Image](https://github.com/anmolpant/SaniText/blob/master/Screenshots/screenshot2.PNG)

## Testing the application

SaniText is a simple text editor for Microsoft Windows and a basic text-editing program which enables computer users to create, edit and save documents. The application performs and should perform all the functions of a text editor adeptly. The application can hence be tested by creating and editing new files or importing already existing .txt files, changing the attributes of the text (like color, alignment, etc.) and modifying the directory structure of your files.

### Break down and analysis

The objective of this project was to create a real text editor using python programming language and tkinter GUI library. This computer software is cross platform and contains all necessary features that every text editor must have.

### Sample working and output 

![Output Image](https://github.com/anmolpant/SaniText/blob/master/Screenshots/screenshot4.PNG)
![Output Image](https://github.com/anmolpant/SaniText/blob/master/Screenshots/screenshot3.PNG)

## Deployment

To deploy and get this running on any system, just use the Windows Installer File enclosed in the repository.

## Built With

* [Python](https://www.python.org/) - The programming language used.
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python frmework used for making and working with GUIs.
* [cx_freeze](https://cx-freeze.readthedocs.io/en/latest/) - Used to convert our python code into a windows installer file.

## Contributing

Please feel free to fork the above repository and open an issue first before submitting a pull request. 

## Authors

* **Anmol Pant** - *Initial work* - (https://github.com/anmolpant)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Shoutout to https://www.freecodecamp.org/ for their tkinter tutorial on Youtube.


