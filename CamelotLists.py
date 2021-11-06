from Location import Location
from PlaceReader import parseData
Items = ["Apple", "Bag", "BlueBook", "BlueCloth", "BlueKey", "BluePotion", "Bottle", "Bread", "ChickenLeg",
         "Coin", "Compass", "Cup", "EvilBook", "GoldCup", "GreenBook", "GreenKey", "GreenPotion", "Hammer",
         "Helmet", "InkandQuill", "JewelKey", "LitTorch", "Lock", "MagnifyingGlass", "OpenScroll", "PurpleBook",
         "PurpleCloth", "PurpleKey", "PurplePotion", "Rags", "RedBook", "RedCloth", "RedKey", "RedPotion",
         "Scroll", "Skull", "SpellBook", "Sword", "Torch"]

Visual_Effects = ["Aura", "Blackflame", "Blood", "Brew", "Campfire", "Death", "Diamond", "Explosion",
                  "Force", "Heart", "Heartbroken", "Magic", "Poison", "Poof", "Resurrection", "Skulls",
                  "Spiralflame", "Wildfire"]

Hair_Color = ["gray", "black", "brown", "red", "blonde"]

Hairstyles_All_Body_Types = ["Long", "Spiky", "Short", "Short_Beard", "Short_Full"]

BodyTypes = ["A", "B", "C", "D", "E", "F", "G", "H"]

Expressions = ["neutral", "happy", "sad", "angry", "disgusted", "scared", "surprised", "asleep"]

Hairsyles_ACEG = ["Ponytail", "Straight"]

Hairsyles_BDFH = ["Mage", "Mage_Beard", "Mage_Full", "Musketeer", "Musketeer_Beard", "Musketeer_Full"]

Outfits_All_Body_Types = ["Bandit", "Beggar", "HeavyArmour", "LightArmour", "Merchant", "Naked",
                          "Noble", "Peasant", "Priest"]

Eyecolor = ["white", "black", "blue", "red", "brown", "green"]

Outfits_ACEG = ["Queen", "Witch"]

Outfits_BDFH = ["King", "Warlock"]

SoundEffects_Actions = ["Clap", "Draw", "Eat", "Hammer", "Lock", "Pocket", "Sheathe", "Unlock",
                        "Unpocket", "Write"]
SoundEffects_Ambient = ["Forest_Day", "Forest_Night", "Port", "River", "Spooky", "Town_Day", "Town_Night"]

SoundEffects_Characters = ["Attack1", "Attack2", "Cry1", "Cry2", "Death1", "Death2", "EvilLaugh1", "EvilLaugh2",
                           "Hit1", "Hit2", "Laugh1", "Laugh2", "Scream"]

SoundEffects_Effects = ["Brew", "DarkMagic", "Fireball", "MixPotion", "Potion", "Spell", "Spell2", "Spell3"]

SoundEffects_Furniture = ["Book", "CloseChest", "CloseDoor1", "CloseDoor2", "Fireplace", "Horse", "OpenChest",
                          "OpenDoor1", "OpenDoor2", "SecretDoor"]

SoundEffects_Music = ["Danger1", "Danger2", "Danger3", "Dramatic", "Explorer", "Grief", "Kingdom", "LivelyMusic",
                      "Ominous", "Peaceful", "Serenade", "Serenity", "Tavern"]

SoundEffects_UI = ["Button", "Error", "Flute1", "Flute2", "Menu"]

CharToCharActions = ["Attack", "Bash", "Cast", "DanceTogether", "Face", "Give", "LookAt", "Take"]

ForestPath = parseData("PlaceCSVs\\ForestPath.csv", "ForestPath")

Farm = parseData("PlaceCSVs\\Farm.csv", "Farm")

SpookyPath = parseData("PlaceCSVs\\SpookyPath.csv", "SpookyPath")

Camp = parseData("PlaceCSVs\\Camp.csv", "Camp")

CastleBedroom = parseData("PlaceCSVs\\CastleBedroom.csv", "CastleBedroom")

Hallway = parseData("PlaceCSVs\\Hallway.csv", "Hallway")
