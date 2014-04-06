Elastix Video Agent Console WebRTC
==============

This is a beta module for the Elastix Call Center Module. This module provides a Video Agent Console using the SIPML5 WebRTC API



##Features:##

* Embedded SIP Phone for make and receive calls.
* Chat Window based on SIP.
* Video capabilities.


##Prerequistes##
The WebRTC Agent Console Addon is required. You can install it from the Addon Menu of your elastix(http://addons.elastix.org/index.php?lang=en).

##Installation:##

1. Download the code and use the RPM in the RPM folder(You can download directly the RPM from here http://goo.gl/h198Fb):
  * As root run the next command in the linux shell:

      `yum install --nogpgcheck -y elastix-video_agent_console_webrtc-0.1-1.noarch.rpm`


2. Configure FreePBX for Video:
  * Go to Unembedded FreePBX --> Tools --> Asterisk SIP Settings, and enable the video support select all codecs. 

  * Save the changes and reload

  * Configure the SIP peers to use Video codecs, the easiest way is to set the fields *disallow* and *allow* to *all*


3. Reconfigure the Webrtc2SIP media gateway:

  * Change to asterisk user running the next command:
      
	`su asterisk`

  * Start the null script:

	`script /dev/null`

  * Connect to the gateway and stop it:

        `screen -r`

        `quit`

  * Reconfigure the settings of the webrtc2sip media gateway by replacing this line:

        `<codecs>pcma;pcmu;gsm;h264-bp;h264-mp;h263;h263+,h264</codecs>` 

    with

        `<codecs>pcma;pcmu;gsm;h264-bp;h264-mp;h263;h263+;h264;vp8</codecs>`

  * Restart the webrtc2sip media gateway:

        `screen -S wrtc`

    then inside the screen session execute:

        `webrtc2sip`

    exit the screen session by typing:

        `CTRL+A+D`

  * Exit from the asterisk's user shell:

	`exit`
    the last exit will stop the null script now tyepe again:

        `exit`
     with the last exit now you are in the root's shell. 
 
         

4. Enjoy and please report bugs and of features.
  

##ScreenShots##

*Video Agent Console WebRTC*
![](http://dl.dropbox.com/u/1277237/AddomDM/VACW.png)

####NOTES####
1. The resolution of the video can be changed by editing the config.xml file.
2. The sip peer must have configured the h263p codec to allow resizing of the video.
3. Depending on the Machine capabilities the Video transcoding(usually from VP8 to h263p) will show the quality. 
4. The screenshot was taken from a Virtualbox Machine i386 1 processor 512 of RAM.
5. Higher hardware specs will allow you better Video Quality
6. **THIS CONSOLE ONLY WILL WORK WITH VIDEO CALLS** For audio calls only use the normal webrtc agent console.


by navaismo@gmail.com
