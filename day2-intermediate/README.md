# TouchDesigner at INTUS | Mexico 2018

## Hosting Studio
[INTUS Interactive Design](http://intus.tv/)

## Artist | Instructors
Matthew Ragan | [matthewragan.com](https://matthewragan.com)  
Zoe Sandoval | [zoesandoval.com](https://zoesandoval.com)  
Materializing Interactive Research  | [mir.works](https://mir.works)

## Overview
A three day workshop for beginners to advanced users of Derivative's TouchDesigner.

## Day 2 | Intermediate
### Session Overview
* What is Python and where does it fit within TouchDesigner
* Speeding up iteration and design processes with Python
* Working with the Animation COMP
* Custom Curves
* Animated Particles
* Animated Instances
* Using audio inputs to control and drive visuals 
* Outputting geometry from TouchDesigner as SVGs
* Best practices for using Python inside of TouchDesigner

# Day 2 Workshop Schedule
Time | Topic | Lead Instructor
-----|-------|-----------------
10:00am | Intro, Context & Roundtable | Zoe / Matt
10:30am | Python - References | Zoe / Matt
11:00am | Python - Simple Scripts and Loops | Zoe / Matt
11:30am | Python and the Replicator COMP | Zoe / Matt
12:30pm | Python vs. Chops | Zoe / Matt
1:00p | Break for Lunch | Zoe / Matt
2:00p | Animation Comp  | Zoe / Matt
2:30p | Animation and Particles | Zoe / Matt
3:00p | Animation and Instances | Zoe / Matt
3:30p | Posting to Instagram | Zoe / Matt
4:30p | Ouputting SVGs | Zoe / matt
6:00p | Wrap | Zoe / Matt

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