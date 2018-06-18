# TouchDesigner @ INTUS | Mexico 2018

## Hosting Studio
[INTUS Interactive Design](http://intus.tv/)

## Artist | Instructors
Matthew Ragan | [matthewragan.com](https://matthewragan.com)  
Zoe Sandoval | [zoesandoval.com](https://zoesandoval.com)  
Materializing Interactive Research | [mir.works](https://mir.works)

## Overview
A three day workshop for beginners to advanced users of Derivative's TouchDesigner.

## Day 2 | Intermediate
### Session Highlights
* What is Python and where does it fit within TouchDesigner
* Speeding up iteration and design processes with Python
* Working with the Animation COMP
* Custom Curves
* Animated Particles
* Animated Instances
* Using audio inputs to control and drive visuals 
* Outputting geometry from TouchDesigner as SVGs
* Best practices for using Python inside of TouchDesigner

# Workshop Schedule
Time | Topic | Lead Instructor
-----|-------|-----------------
10:00a | Intro, Context & Roundtable | All
10:30a | Python & References | Matt
11:00a | Python, Simple Scripts and Loops | Matt
11:30a | Python & the Replicator COMP | Matt
12:30p | Animation Comp | Zoe
1:00p | Break for Lunch | All
2:00p | Animation Comp & Instances | Zoe
3:00p | Animation Comp & Particles | Matt
4:00p | Audio Inputs & Visual Control | Matt
5:00p | Posting to Instagram | Zoe
6:00p | Wrap | All

# Dependencies
**TouchDesigner 099** - https://www.derivative.ca/099/Downloads/  

## **SVG Write**
[svgwrite](https://pypi.python.org/pypi/svgwrite/)  

### Adding Dependencies to TouchDesigner
If you'd like to add the modules directly to your TouchDesigner folder you can do that with the following commands

### **Windows**
First install [Python 3.5.1](https://www.python.org/downloads/release/python-351/)  
From the command line `pip install --target=/path/to/your/packages/directory/for/TD package_to_install`  

There's a good chance that looks like:  
From the command line `pip install --target="C:\Program Files\Derivative\TouchDesigner099\bin\Lib\site-packages" svgwrite`

### **MacOS**
First install [Python 3.5.1](https://www.python.org/downloads/release/python-351/)  
From a Terminal window  
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`  
`python3 get-pip.py`  
`python3 -m pip install --target=/Applications/TouchDesigner099.app/Contents/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages svgwrite`

## **InstagramApi**
[InstagramApi](https://github.com/LevPasha/Instagram-API-python)  

### Adding Dependencies to TouchDesigner
If you'd like to add the modules directly to your TouchDesigner folder you can do that with the following commands

### **Windows**
From the command line `pip install --target=/path/to/your/packages/directory/for/TD package_to_install`  

There's a good chance that looks like:  
From the command line `pip install --target="C:\Program Files\Derivative\TouchDesigner099\bin\Lib\site-packages" InstagramAPI`

### **MacOS**
From a Terminal window  
`python3 -m pip install --target=/Applications/TouchDesigner099.app/Contents/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages InstagramAPI`