import os 
import shutil
import argparse
from os.path import isfile, join

UnsortedFolder = "PlaceFilesHere/"


class Directory():
    def __init__(self, path, fileFormat) -> None:
        self.path = path
        self.fileFormat = fileFormat

CUT_SCENES = Directory("FMOD_GOF2/CUT_SCENES/", ".wav")
MOTHERSHIP = Directory("FMOD_GOF2/CUT_SCENES/OUTRO/MOTHERSHIP/", ".wav")
MUSIK_SPACE = Directory("FMOD_GOF2/MUSIK_SPACE/", ".mp3")
MUSIK_STATION = Directory("FMOD_GOF2/MUSIK_STATION/", ".mp3")
SFX_GENERAL = Directory("FMOD_GOF2/SFX_GENERAL/", ".wav")
EXPLOSION_BOMB = Directory("FMOD_GOF2/SFX_SPACE/EXPLOSION_BOMB/", ".wav")
EXPLOSION_EMP = Directory("FMOD_GOF2/SFX_SPACE/EXPLOSION_EMP/", ".wav")
GAME_OVER = Directory("FMOD_GOF2/SFX_SPACE/GAME_OVER/", ".wav")
HANGARSFX = Directory("FMOD_GOF2/SFX_SPACE/HANGAR/", ".wav")
INTRO = Directory("FMOD_GOF2/SFX_SPACE/INTRO/" , ".wav")
LAUNCH_BOMB = Directory("FMOD_GOF2/SFX_SPACE/LAUNCH_BOMB/", ".wav")
LAUNCH_EMP = Directory("FMOD_GOF2/SFX_SPACE/LAUNCH_EMP/", ".wav")
LOUNGE = Directory("FMOD_GOF2/SFX_SPACE/LOUNGE/", ".wav")
MISSION_ACCOMPLISHED = Directory("FMOD_GOF2/SFX_SPACE/MISSION_ACCOMPLISHED/", ".wav")
PLAYER = Directory("FMOD_GOF2/SFX_SPACE/PLAYER/", ".wav")
DESTRUCTION = Directory("FMOD_GOF2/SFX_SPACE/SFX_SPACE_GENERAL/DESTRUCTION/", ".wav")
INCOMING = Directory("FMOD_GOF2/SFX_SPACE/SFX_SPACE_GENERAL/INCOMING/", ".wav")
JUMPGATE = Directory("FMOD_GOF2/SFX_SPACE/SFX_SPACE_GENERAL/JUMPGATE/", ".wav")
PLAYER_GENERAL = Directory("FMOD_GOF2/SFX_SPACE/SFX_SPACE_GENERAL/PLAYER/", ".wav")
WORMHOLE = Directory("FMOD_GOF2/SFX_SPACE/SFX_SPACE_GENERAL/WORMHOLE/", ".wav")
BOOSTER = Directory("FMOD_GOF2/SFX_SPACE/SHIP/BOOSTER/", ".wav")
ENGINE= Directory("FMOD_GOF2/SFX_SPACE/SHIP/ENGINE/", ".wav")
WEAPON_BEAM = Directory("FMOD_GOF2/SFX_SPACE/WEAPON_BEAM/", ".wav")
WEAPON_BLASTER = Directory("FMOD_GOF2/SFX_SPACE/WEAPON_BLASTER/", ".wav")
WEAPON_BLASTER_EMP = Directory("FMOD_GOF2/SFX_SPACE/WEAPON_BLASTER_EMP/", ".wav")
WEAPON_CANNON = Directory("FMOD_GOF2/SFX_SPACE/WEAPON_CANNON/", ".wav")
WEAPON_LASER = Directory("FMOD_GOF2/SFX_SPACE/WEAPON_LASER/", ".wav")
WEAPON_LAUNCH_MISSILE = Directory("FMOD_GOF2/SFX_SPACE/WEAPON_LAUNCH_MISSILE/", ".wav")
WEAPON_THERMAL = Directory("FMOD_GOF2/SFX_SPACE/WEAPON_THERMAL/", ".wav")
WEAPON_TURRET = Directory("FMOD_GOF2/SFX_SPACE/WEAPON_TURRET/", ".wav")
HANGAR = Directory("FMOD_GOF2/SFX_STATION/HANGAR/", ".wav")
LOUNGESTATION = Directory("FMOD_GOF2/SFX_STATION/LOUNGE/", ".wav")
MAINVIEW = Directory("FMOD_GOF2/SFX_STATION/MAINVIEW/", ".wav")
MAP = Directory("FMOD_GOF2/SFX_STATION/MAP/", ".wav")
ENG = Directory("FMOD_GOF2/VOICE/ENG/", ".mp3")
GENERIC = Directory("FMOD_GOF2/VOICE/GENERIC/", ".mp3")
LOUNGEVOICE = Directory("FMOD_GOF2/VOICE/LOUNGE/", ".mp3")
TIMESHIFT = Directory("FMOD_GOF2/DLC/TIMESHIFT/", ".mp3")

folders = [CUT_SCENES, MOTHERSHIP,
           MUSIK_SPACE, MUSIK_STATION,
           SFX_GENERAL,
           EXPLOSION_BOMB, EXPLOSION_EMP,
           GAME_OVER,
           HANGARSFX,
           INTRO,
           LAUNCH_BOMB, LAUNCH_EMP,
           LOUNGE,
           MISSION_ACCOMPLISHED,
           PLAYER,
           DESTRUCTION, INCOMING, JUMPGATE, PLAYER_GENERAL, WORMHOLE,
           ENGINE, BOOSTER,
           WEAPON_BEAM, WEAPON_BLASTER, WEAPON_BLASTER_EMP, WEAPON_CANNON, WEAPON_LASER, WEAPON_LAUNCH_MISSILE, WEAPON_THERMAL, WEAPON_TURRET,
           HANGAR,
           LOUNGESTATION,
           MAINVIEW,
           MAP,
           ENG,
           GENERIC,
           LOUNGEVOICE,
           TIMESHIFT]

parser = argparse.ArgumentParser()

parser.add_argument('-c', "--clear", action = "store_true", help="Clear the contents of all FMOD_GOF2 folders")

args = parser.parse_args()


if __name__ == "__main__":

    if args.clear:
        
        for i in folders:
            onlyfiles = [f for f in os.listdir(i.path) if isfile(join(i.path, f))]
            
            for j in onlyfiles:
                
                if j != "files.txt":
                    os.remove(i.path + j)
                    print("removed " + j)
    
    else:
        for i in folders:

            print("in "+i.path)

            f = open(f"{i.path}files.txt", "r", encoding="UTF-16")
            fileList = list(f.read().split("\n"))

            for j in fileList:

                fullFileName = j + i.fileFormat

                if j == "":
                    continue

                elif os.path.isfile(i.path + fullFileName):
                    print(fullFileName + " has already been moved")
                    continue

                else:
                    print(j)
                    
                    shutil.move("PlaceFilesHere/" + fullFileName, i.path)
                    print("moving " + "PlaceFilesHere/" + fullFileName + " into " + i.path)