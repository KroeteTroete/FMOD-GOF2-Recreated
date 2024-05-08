# FMOD-GOF2-Recreated

A replica of Galaxy On Fire 2's FMOD Designer Project file. Intended to allow more complex sound and event modifications.
The project is **not fully finished and will probably feature discrepencies in comparison with the original file**.

The .fdp file was created for the **PC/Steam version of Galaxy On Fire 2**, thus the DLC content is missing and I don't know how any .fev or .fsb files built with that .fdp will behave on other platforms.

### Current issues that are still being worked on:

- I turned the volume down in a lot of cases and I'm still not completely satisfied with it. I would really appreciate some other approaches to mimicking the original volume level of GOF2.
- 3D Rolloff. In some cases, such as weapons sounds, I managed to get pretty close to the original 3D rolloff used in the game. However some sounds which feature 3D rolloff are still unfinished or untested.
- Missing localization. At the moment the german sound banks and localization are still missing.
- There are probably even more issues which I haven't found yet.

# FMOD Designer project file (.fdp)

The FMOD Designer project can be found in the "Projects" folder. To open it you have to use the program FMOD Designer. I recommend using the version 4.30.06.
That version can't be found on FMOD's website anymore, however you can download it off the Internet Archive. The download link can also be found [here](https://archive.org/details/fmod-4.30.06).
FMOD Designer also comes with FMOD Event Player, which can be used to view either the vanilla or modded .fev files.
After opening the file in FMOD Designer, you can edit it to your desire and then build your own .fev and .fsb files for Galaxy On Fire, which can then be placed in GOF2's sound folder (data/assets/main/sound/).

The .fdp file can also be opened as a text file using notepad++ or any other editor/IDE.

# Setting up the project

I chose not to include the games audio files in this repository. Instead you will have to extract them yourself using fsbext and then sort them into the various folders using SortSound.py
You will need to have python Installed for this process:

1. Download fsbext from Luigi Auriemma's Website: http://aluigi.altervista.org/search.php?src=fsbext
2. Place the gof2FSBEXT.py in the same folder as fsbext.exe
3. Run gof2FSBEXT.py. In the first directory selection window, select FMOD-GOF2-Recreated's "PlaceFilesHere" folder. In the second directory selection window, select Galaxy On Fire 2's sound folder (Galaxy On Fire 2/data/assets/main/sound).
4. Go into FMOD-GOF2-Recreated and run SortSound.py. If all goes well, the "PlaceFilesHere" folder should now be empty. To verify if the sounds have been sorted correctly, open the project in FMOD Designer 4.30, go into "Wave Banks" and scroll through the lists of waveforms and check for any marked red.

# Templates

The other file in that folder is the template file (.fdt), which stores all the templates I created to make the replication process easier.
These templates were only created to make the creation of other events easier. **They are not essential for the project and even a bit repetetive**. The templates are:

- Launch_Missile_EMP_GL1: Template used for the missiles. The most important aspects are the user property "0" and the 3D mode
- Destruction_Ship_Big: Template used for all the ship explosions. The most important aspects are the user property "0" and the 3D mode
- Standard: Template used for most 2D sounds, with the Volume turned down by 20db. The max playback behaviour "Just fail" is also really important here
- Standard_Laser: Template used for all weapons. The 3D mode and Rolloff settings are really important. They influence how the sounds behave at a distance
- StationMusic: Template used for all music that's playing inside the space stations. It's biggest feature is the location parameter and the settings for the highpass filter, lowpass filter and echo effect
- SpaceMusic: Music for all the music that can play while in space. It automatically lowers the volume by 5 db.

  ### If you have any questions you can contact me or other modders on the Kaamo Club Discord. The link can be found on the [Wiki's frontpage](https://galaxyonfire.wiki.gg/wiki/Galaxy_on_Fire_Wiki).


