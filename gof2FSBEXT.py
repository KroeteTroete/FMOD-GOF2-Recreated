import subprocess as sp
import time
import tkinter, tkinter.filedialog

root = tkinter.Tk()


PlaceHere = tkinter.filedialog.askdirectory(parent=root, initialdir="/", title = "Please select the 'PlaceFilesHere' folder inside FMOD_GOF2_Recreated")

GameSound = tkinter.filedialog.askdirectory(parent=root, initialdir="/", title = "Please select GOF2's sound folder")


ima_adpcm_banks = ["FMOD_GOF2_CUTSCENES.fsb", "FMOD_GOF2_SFX_GENERAL.fsb", "FMOD_GOF2_SFX_SPACE.fsb",
                    "FMOD_GOF2_SFX_STATION_HANGAR.fsb", "FMOD_GOF2_SFX_STATION_LOUNGE.fsb", "FMOD_GOF2_SFX_STATION_MAINVIEW.fsb"]

mp3_banks = ["FMOD_GOF2_GENERIC_eng.fsb", "FMOD_GOF2_LOUNGE_eng.fsb", "FMOD_GOF2_VOICE_eng.fsb", "FMOD_GOF2_MUSIC.fsb"]


print("PROCESSING IMA ADPCM BANKS")
time.sleep(3)
for i in ima_adpcm_banks:

    fsbext = sp.Popen(['./fsbext', '-A', '-d', PlaceHere, GameSound+f"/{i}"])

    fsbext_status = fsbext.wait()

print("PROCESSING MP3 BANKS")
time.sleep(3)

for i in mp3_banks:
    fsbext = sp.Popen(['./fsbext', '-d', PlaceHere, GameSound+f"/{i}"])

    fsbext_status = fsbext.wait()

