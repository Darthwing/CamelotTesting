import Location

Items = ["Apple", "Bag", "BlueBook", "BlueCloth", "BlueKey", "BluePotion", "Bottle", "Bread", "ChickenLeg",
         "Coin", "Compass", "Cup", "EvilBook", "GoldBook", "GreenBook", "GreenKey", "GreenPotion", "Hammer",
         "Helmet", "InkandQuill", "JewelKey", "LitTorch", "Lock", "MagnifyingGlass", "OpenScroll", "PurpleBook",
         "PurpleCloth", "PurpleKey", "PurplePotion", "Rags", "RedBook", "RedCloth", "RedKey", "RedPotion",
         "Scroll", "Skull", "SpellBook", "Sword", "Torch"]

Visual_Effects = ["Aura", "Blackflame", "Blood", "Brew", "Campfire", "Death", "Diamond", "Explosion",
                  "Force", "Heart", "Heartbroken", "Magic", "Poison", "Poof", "Resurrection", "Skulls",
                  "Spiralflame", "Wildfire"]

Hairstyles_All_Body_Types = ["Long", "Spiky", "Short", "Short_Beard", "Short_Full"]

BodyTypes = ["A", "B", "C", "D", "E", "F", "G", "H"]

Hairsyles_ACEG = ["Ponytail", "Straight"]

Hairsyles_BDFH = ["Mage", "Mage_Beard", "Mage_Full", "Musketeer", "Musketeer_Beard", "Musketeer_Full"]

Outfits_All_Body_Types = ["Bandit", "Beggar", "HeavyArmour", "LightArmour", "Merchant", "Naked",
                          "Noble", "Peasant", "Priest"]

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

ForestPath = Location.Location("ForestPath", ["EastEnd", "Well", "Plant", "DirtPile", "PathBlock", "WestEnd"],
                               [None, None, None, None, None, None],
                               [None, None, None, None, "PathBlock", None],
                               ["EastEnd", "WestEnd"])

Farm = Location.Location("Farm", ["Exit", "Haypiles", None, "Anvil", "Door", "Well"],
                         [None, None, None, ["Surface"], ["Can Open and Close"], None],
                         [None, "Haypiles", None, None, None, None],
                         ["Exit", "Door"])

SpookyPath = Location.Location("SpookyPath", ["WestEnd", "DirtPile", "Plant", "Well", "PathBlock", "EastEnd"],
                               [None, None, None, None, None, None],
                               [None, None, None, None, "PathBlock", None],
                               ["WestEnd", "EastEnd"])