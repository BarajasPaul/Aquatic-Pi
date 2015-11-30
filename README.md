Aquatic-Pi
==========

An autonomous aquatic vehicle to facilitate sampling stage in a field of shrimp
and various marine animals

The idea is to build a project

Basic configuration
======================

Aquatipi works under rapsbian distribution

Obtain image and flash it.
Tutorial is in the next link:
http://www.raspberrypi.org/documentation/installation/installing-images/README.md


First step

    -enable ssh connection(You will need it if you don't have HDMI Monitor)
    -enable camera hardware( For development purpose )
    -enable I2c, spi and UART( GPIO control )

Make sure, you have access to the internet to download the latest version of 
raspbian software, It’s very important to update operative system, because 
many bugs and issues were fixed by a open source community or by a 
free collaboration, perhaps Raspbian was whom resolved it.

-sudo apt-get update
-sudo apt-get upgrade
-reboot system

Understanding basic linux commands
http://linuxcommand.org/tlcl.php

In this project, we use the review tool (Github), It you’re not familiarized 
with a version control,
I recommend you to learn about Git version Control, It’s necessary that you 
learn about it, because, we will maintain all the source code in Github. 
In consequent, you won't be able to contribute to aquatic pi project :( 
http://conociendogithub.readthedocs.org/en/latest/data/introduccion/

If you're using Windows or IOS operative system, you must search through 
the internet to configure git in your system. 
However,In GNU/Linux operating system is installed by default

Once, you’ve been introducing to git version control system, 
you need to set up your ssh key in the raspberry to connect it to 
the Github review tool and obtain the source code
ssh-keygen configuration:
https://help.github.com/articles/generating-ssh-keys/

Aquatic PI repository:
https://github.com/BarajasPaul/Aquatic-Pi

And ready to contribute to Aquatic PI :D
