import csv
import pickle

import CamelotLists
from tkinter import *
from tkinter import ttk
import ctypes

# sets the root for the testing window
from Location import Location
from PlaceReader import parseData

root = Tk()
root.title('Camelot Testing Environment')

cottage_locations = ["Door", "Bed", "Chair", "Table", "Shelf", "Bookshelf", "Chest"]


class TestingGui:
    def __init__(self, master):
        self.focusCharacter = "BobB"
        self.characters = ['BobA', 'BobB', 'BobC', 'BobD', 'BobE', 'BobF', 'BobG', 'BobH']
        self.locationName = "BobsHouse"
        self.characterList = list()
        self.characterList.append("BobB")
        self.trashList = list()
        self.trash = "Trashcan"
        self.currentFocusMode = ""
        self.waitTime = .5
        self.isInputEnabled = False

        self.partialTestingButton = Button(master, text="Partial Testing",
                                           command=lambda: self.createPartialTestingWindow(root))

        self.myButton = Button(master, text="Run Command", command=self.get_input)
        self.clearButton = Button(master, text="Clear", command=self.clear_output)
        self.commandBox = Text(master, height=5, width=40)
        self.outputBox = Text(master, height=12, width=40)

        self.defaultButton = Button(master, text="Default", command=lambda: self.default(self.focusCharacter))

        self.items_button = Button(master, text="Items", command=self.items)
        self.visual_effects_button = Button(master, text="Visual Effects", command=self.visual_effects)
        self.run_aroundButton = Button(master, text="Run Around", command=self.run_around)
        self.all_clothingButton = Button(master, text="All Clothing", command=self.all_clothing)
        self.inputButton = Button(master, text="Allow input", command=self.inputEnable)
        self.char2charInteractionButton = Button(master, text="Character Interaction",
                                                 command=self.test_CharacterActions)
        self.forest_button = Button(master, text="Forest Path Test",
                                    command=lambda: self.test_Place(CamelotLists.ForestPath))
        self.farm_button = Button(master, text="Farm Test",
                                  command=lambda: self.test_Place(CamelotLists.Farm))
        self.spooky_path_button = Button(master, text="Spooky Path Test",
                                         command=lambda: self.test_Place(CamelotLists.SpookyPath))

        self.camp_button = Button(master, text="Camp Test",
                                  command=lambda: self.test_Place(CamelotLists.Camp))
        self.castle_bedroom_button = Button(master, text="Castle Bedroom Test",
                                            command=lambda: self.test_Place(CamelotLists.CastleBedroom))
        self.hallway_button = Button(master, text="Hallway Test",
                                     command=lambda: self.test_Place(CamelotLists.Hallway))
        self.bridge_button = Button(master, text="Bridge Test",
                                    command=lambda: self.test_Place(CamelotLists.Bridge))
        self.castle_crossroad_button = Button(master, text="Castle Crossroads Test",
                                              command=lambda: self.test_Place(CamelotLists.CastleCrossroads))
        self.courtyard_button = Button(master, text="Courtyard Test",
                                       command=lambda: self.test_Place(CamelotLists.Courtyard))

        self.commandBox.pack()
        self.myButton.pack()
        self.outputBox.pack()
        self.clearButton.pack()
        self.inputButton.pack()
        self.defaultButton.pack()
        self.char2charInteractionButton.pack()
        self.forest_button.pack()
        self.farm_button.pack()
        self.spooky_path_button.pack()
        self.camp_button.pack()
        self.castle_bedroom_button.pack()
        self.hallway_button.pack()
        self.bridge_button.pack()
        self.castle_crossroad_button.pack()
        self.courtyard_button.pack()
        self.partialTestingButton.pack()
        self.initialize()

    @staticmethod
    def create_command(command_list):
        if len(command_list) > 1:
            new_command = command_list[0] + "("
            for i in command_list[1:]:
                new_command = new_command + i + ","
            new_command = new_command[:-1]
            new_command = new_command + ")"
        else:
            new_command = command_list[0] + "()"

        return new_command

    def createManualWindow(self, master):
        manualwindow = Toplevel(master)
        manualwindow.title("Manual Experience Manager")
        manualwindow.geometry("300x300")

        clothingWindow = Button(manualwindow, text="Clothing",
                                command=lambda: self.generateClothingWindow(manualwindow))
        hairWindow = Button(manualwindow, text="HairStyle", command=lambda: self.generateHairStyleWindow(manualwindow))

        expressionWindow = Button(manualwindow, text="Expressions",
                                  command=lambda: self.generateExpressionWindow(manualwindow))

        characterWindow = Button(manualwindow, text="Character Creator",
                                 command=lambda: self.generateCharacterWindow(manualwindow))

        clothingWindow.pack()
        hairWindow.pack()
        expressionWindow.pack()
        characterWindow.pack()

        manualwindow.mainloop()

    def createPartialTestingWindow(self, master):
        partialTestingWindow = Toplevel(master)
        partialTestingWindow.title("Partial Testing Experience Manager")
        partialTestingWindow.geometry("400x800")

        Button(partialTestingWindow, text="Selection Testing",
               command=lambda: self.createSelectingTestingWindow(partialTestingWindow)).pack()
        Button(partialTestingWindow, text="Auto Testing",
               command=lambda: self.createautoTestWindow(partialTestingWindow)).pack()

        partialTestingWindow.mainloop()

    def createautoCharacterWindow(self, master):
        autoCharacterWindow = Toplevel(master)
        autoCharacterWindow.title("Partial Testing Experience Manager")
        autoCharacterWindow.geometry("400x800")

        Button(autoCharacterWindow, text="Clothing", command=self.clothing).pack()
        Button(autoCharacterWindow, text="Eye Color", command=self.eye_color).pack()
        Button(autoCharacterWindow, text="Hair Styles", command=self.hair_style).pack()
        Button(autoCharacterWindow, text="Hair Color", command=self.hair_color).pack()
        Button(autoCharacterWindow, text="Skin Color", command=self.skin_color).pack()

        autoCharacterWindow.mainloop()

    def createautoTestWindow(self, master):
        autoTestWindow = Toplevel(master)
        autoTestWindow.title("Full Partial Experience Manager")
        autoTestWindow.geometry("400x800")

        Button(autoTestWindow, text="Auto Character",
               command=lambda: self.createautoCharacterWindow(autoTestWindow)).pack()

        autoTestWindow.mainloop()

    def createSelectingTestingWindow(self, master):
        selectionTestingWindow = Toplevel(master)
        selectionTestingWindow.title("Full Partial Experience Manager")
        selectionTestingWindow.geometry("400x800")

        manualTestButton = Button(selectionTestingWindow, text="Manual Test",
                                  command=lambda: self.createManualWindow(selectionTestingWindow))
        autoTestButton = Button(selectionTestingWindow, text="Auto Test",
                                command=lambda: self.createautoTestWindow(selectionTestingWindow))
        manualTestButton.pack()
        autoTestButton.pack()

        selectionTestingWindow.mainloop()

    def generateHairStyleWindow(self, master):
        hairStyleWindow = Toplevel(master)
        hairStyleWindow.title("Manual HairStyle Experience Manager")
        hairStyleWindow.geometry("400x800")

        Label(hairStyleWindow, text="Hair Style:").pack()
        for i in CamelotLists.Hairstyles_All_Body_Types:
            ttk.Button(hairStyleWindow, text=i, command=lambda i=i: self.manualhairstyle(i)).pack()
        if self.focusCharacter[-1] in ['A', 'C', 'E', 'G']:
            for j in CamelotLists.Hairsyles_ACEG:
                ttk.Button(hairStyleWindow, text=j, command=lambda j=j: self.manualhairstyle(j)).pack()
        if self.focusCharacter[-1] in ['B', 'D', 'F', 'H']:
            for k in CamelotLists.Hairsyles_BDFH:
                ttk.Button(hairStyleWindow, text=k, command=lambda k=k: self.manualhairstyle(k)).pack()

        Label(hairStyleWindow, text="Hair Color:").pack()
        for i in CamelotLists.Hair_Color:
            ttk.Button(hairStyleWindow, text=i, command=lambda i=i: self.manualhaircolor(i)).pack()

        hairStyleWindow.mainloop()

    def generateCharacterWindow(self, master):
        characterWindow = Toplevel(master)
        characterWindow.title("Manual Character Experience Manager")
        characterWindow.geometry("400x500")

        for i in CamelotLists.BodyTypes:
            ttk.Button(characterWindow, text=i, command=lambda i=i: self.createCharacter("Bob" + i, i)).pack()

        characterWindow.mainloop()

    def yeet(self, name):
        for i in self.characterList:
            if i not in self.trashList and name != i:
                self.trashList.append(i)
                command_list = ['SetPosition', i, self.trash]
                self.action(self.create_command(command_list))

    def createCharacter(self, name, body):
        # If character already exists
        if name not in self.characterList:
            command_list = ['CreateCharacter', name, body]
            self.action(self.create_command(command_list))
            self.characterList.append(name)
            command_list = ['SetPosition', name, self.locationName]
            self.action(self.create_command(command_list))
            command_list = ['SetCameraFocus', name]
            self.action(self.create_command(command_list))
            self.focusCharacter = name
            self.yeet(name)
        else:
            self.default(name)
            self.trashList.remove(name)
            command_list = ['SetCameraFocus', name]
            self.action(self.create_command(command_list))
            self.focusCharacter = name
            self.yeet(name)

    def generateExpressionWindow(self, master):
        expressionWindow = Toplevel(master)
        expressionWindow.title("Manual Expression Experience Manager")
        expressionWindow.geometry("400x500")

        for i in CamelotLists.Expressions:
            ttk.Button(expressionWindow, text=i, command=lambda i=i: self.manualexpression(i)).pack()

        expressionWindow.mainloop()

    def generateClothingWindow(self, master):
        clothingWindow = Toplevel(master)
        clothingWindow.title("Manual Clothing Experience Manager")
        clothingWindow.geometry("400x400")

        for i in CamelotLists.Outfits_All_Body_Types:
            ttk.Button(clothingWindow, text=i, command=lambda i=i: self.manualclothing(i)).pack()
        if self.focusCharacter[-1] in ['A', 'C', 'E', 'G']:
            for j in CamelotLists.Outfits_ACEG:
                ttk.Button(clothingWindow, text=j, command=lambda j=j: self.manualclothing(j)).pack()
        if self.focusCharacter[-1] in ['B', 'D', 'F', 'H']:
            for k in CamelotLists.Outfits_BDFH:
                ttk.Button(clothingWindow, text=k, command=lambda k=k: self.manualclothing(k)).pack()

        clothingWindow.mainloop()

    def manualclothing(self, clothingname):
        command_list = ['SetClothing', self.focusCharacter, clothingname]
        self.action(self.create_command(command_list))

    def manualhairstyle(self, hairstylename):
        command_list = ['SetHairStyle', self.focusCharacter, hairstylename]
        self.action(self.create_command(command_list))

    def manualhaircolor(self, haircolor):
        command_list = ['SetHairColor', self.focusCharacter, haircolor]
        self.action(self.create_command(command_list))

    def manualexpression(self, expression):
        command_list = ['SetExpression', self.focusCharacter, expression]
        self.action(self.create_command(command_list))

    def all_clothing(self):
        oldcharacter = self.focusCharacter
        # self.action('SetCameraMode(track)')
        for i in self.characters:
            self.characterList.append(i)
            command_list = ['CreateCharacter', i, i[-1]]
            self.action(self.create_command(command_list))
            command_list = ['SetPosition', i, self.locationName]
            self.action(self.create_command(command_list))
            command_list = ['SetCameraFocus', i]
            self.action(self.create_command(command_list))
            self.focusCharacter = i
            command_list = ['SetPosition', oldcharacter]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')
            for j in CamelotLists.Outfits_All_Body_Types:
                command_list = ['SetClothing', i, j]
                self.action(self.create_command(command_list))
                self.action('Wait(.5)')
            command_list = ['SetClothing', i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')
            if i[-1] in ['A', 'C', 'E', 'G']:
                for k in CamelotLists.Outfits_ACEG:
                    command_list = ['SetClothing', i, k]
                    self.action(self.create_command(command_list))
                    self.action('Wait(.5)')
            if i[-1] in ['B', 'D', 'F', 'H']:
                for m in CamelotLists.Outfits_BDFH:
                    command_list = ['SetClothing', i, m]
                    self.action(self.create_command(command_list))
                    self.action('Wait(.5)')
            oldcharacter = i

    def inputEnable(self):
        if self.isInputEnabled:
            self.action('DisableInput()')
            self.isInputEnabled = False
        else:
            self.action('EnableInput()')
            self.isInputEnabled = True

    def clothing(self):
        for i in CamelotLists.Outfits_All_Body_Types:
            command_list = ['SetClothing', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def hair_style(self):
        for i in CamelotLists.Hairstyles_All_Body_Types:
            command_list = ['SetHairStyle', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def eye_color(self):
        for i in CamelotLists.Eyecolor:
            command_list = ['SetEyeColor', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def default(self, name):
        self.initialize()
        command_list = ['SetCameraMode', "focus"]
        self.action(self.create_command(command_list))
        command_list = ['SetPosition', name, self.locationName]
        self.action(self.create_command(command_list))
        command_list = ['SetClothing', name]
        self.action(self.create_command(command_list))
        command_list = ['SetHairStyle', name]
        self.action(self.create_command(command_list))
        command_list = ['SetEyeColor', name]
        self.action(self.create_command(command_list))
        command_list = ['SetHairColor', name]
        self.action(self.create_command(command_list))
        command_list = ['SetSkinColor', name, str(0)]
        self.action(self.create_command(command_list))

    def hair_color(self):
        for i in CamelotLists.Hair_Color:
            command_list = ['SetHairColor', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def skin_color(self):
        for i in range(10):
            command_list = ['SetSkinColor', self.focusCharacter, str(i)]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def items(self):
        for i in CamelotLists.Items:
            command_list = ['CreateItem', i, i]
            self.action(self.create_command(command_list))
            command_list = ['SetPosition', i, self.focusCharacter]
            self.action(self.create_command(command_list))
            self.action('Wait(.75)')
            command_list = ['Pocket', self.focusCharacter, i]
            self.action(self.create_command(command_list))

    def visual_effects(self):
        for i in CamelotLists.Visual_Effects:
            command_list = ['CreateEffect', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(1)')

    def clear_output(self):
        self.outputBox.delete('1.0', END)

    def get_input(self):
        input = self.commandBox.get("1.0", 'end-1c')
        self.action(input)
        self.commandBox.delete('1.0', END)

    def run_around(self):
        for i in cottage_locations:
            command_list = ['WalkTo', self.focusCharacter, self.locationName + "." + i]
            self.action(self.create_command(command_list))
            self.action('Wait(1)')

    def test_Place(self, place: Location):
        self.action(self.create_command(["CreatePlace", place.title, place.title]))
        command_list = ['CreateItem', CamelotLists.Items[1], CamelotLists.Items[1]]
        self.action(self.create_command(command_list))
        for i in ("track", "follow", "focus"):
            self.action("SetCameraMode(" + i + ")")
            command_list = ['SetPosition', self.focusCharacter, place.title]
            self.action(self.create_command(command_list))
            command_list = ['SetClothing', self.focusCharacter, "Bandit"]
            self.action(self.create_command(command_list))
            for location in place.locs:
                print("place: " + str(place.locs[0]))
                if location[0] is not None:
                    command_list = ['WalkTo', self.focusCharacter, place.title + "." + location[0]]
                    self.action(self.create_command(command_list))
                    self.action('Wait(2)')
                    if location[1] is not None:
                        for attr in location[1]:
                            if attr == "Surface":
                                command_list = ['Put', self.focusCharacter, CamelotLists.Items[1],
                                                place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                command_list = ['Pickup', self.focusCharacter, CamelotLists.Items[1],
                                                place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                if location[2] is not None:
                                    for pos in location[2]:
                                        self.action(self.create_command(command_list))
                                        command_list = ['Put', self.focusCharacter, CamelotLists.Items[1],
                                                        place.title + "." + location[0] + "." + pos]
                                        self.action(self.create_command(command_list))
                                        command_list = ['Pickup', self.focusCharacter, CamelotLists.Items[1],
                                                        place.title + "." + location[0] + "." + pos]
                                        self.action(self.create_command(command_list))
                            if attr == "Seat":
                                command_list = ['Sit', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                self.action("Wait(1)")
                                command_list = ['WalkTo', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                if location[0] == "Bed":
                                    command_list = ['Sleep', self.focusCharacter, place.title + "." + location[0]]
                                    self.action(self.create_command(command_list))
                                    self.action("Wait(1)")
                                    command_list = ['WalkTo', self.focusCharacter, place.title + "." + location[0]]
                                    self.action(self.create_command(command_list))
                                if location[2] is not None:
                                    for pos in location[2]:
                                        command_list = ['Sit', self.focusCharacter, place.title + "." + location[0]
                                                        + "." + pos]
                                        self.action(self.create_command(command_list))
                                        self.action("Wait(1)")
                                        command_list = ['WalkTo', self.focusCharacter, place.title + "." + location[0]]
                                        self.action(self.create_command(command_list))

                            if attr == "Can Open and Close":
                                command_list = ['OpenFurniture', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                command_list = ['CloseFurniture', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))

            for portal in place.exits:
                command_list = ['WalkTo', self.focusCharacter, place.title + "." + portal]
                self.action(self.create_command(command_list))
                self.action(self.create_command(["Exit", self.focusCharacter, place.title + "." + portal, "true"]))
                self.action(self.create_command(["Enter", self.focusCharacter, place.title + "." + portal, "true"]))

    def test_CharacterActions(self):
        self.action("CreatePlace(CharacterInteraction, Farm")
        self.action("CreateCharacter(TestDummy, A)")
        for char in ("TestDummy", "BobB"):
            command_list = ['SetCameraFocus', char]
            self.action(self.create_command(command_list))
            self.action("SetCameraMode(Follow)")
            command_list = ['SetPosition', self.focusCharacter, "CharacterInteraction"]
            self.action(self.create_command(command_list))
            self.action("SetPosition(TestDummy, CharacterInteraction.Exit)")
            command_list = ['SetClothing', self.focusCharacter, "Peasant"]
            self.action(self.create_command(command_list))
            self.action("SetClothing(TestDummy, Peasant)")

            self.action("CreateItem(DummySword, Sword)")
            command_list = ["Draw", self.focusCharacter, "DummySword"]
            self.action(self.create_command(command_list))
            command_list = ["Attack", self.focusCharacter, "TestDummy", "false"]
            self.action(self.create_command(command_list))
            command_list = ["Attack", self.focusCharacter, "TestDummy", "true"]
            self.action(self.create_command(command_list))
            command_list = ["Pocket", self.focusCharacter, "DummySword"]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Cast", self.focusCharacter, "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["DanceTogether", self.focusCharacter, "TestDummy"]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Face", self.focusCharacter, "TestDummy"]
            self.action(self.create_command(command_list))
            self.action("CreateItem(DummyPotion, BluePotion)")
            command_list = ["Give", self.focusCharacter, "DummyPotion", "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["LookAt", self.focusCharacter, "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["LookAt", self.focusCharacter]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Put", "TestDummy", "DummyPotion", self.focusCharacter]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Take", "TestDummy", "DummyPotion", self.focusCharacter]
            self.action(self.create_command(command_list))

    def walkAway(self):
        command_list = ['MoveAway', self.focusCharacter]
        self.action(self.create_command(command_list))

    def initialize(self):
        self.action('CreatePlace(BobsHouse, Cottage)')
        self.action('CreatePlace(Trashcan, Cottage)')
        self.action('CreateCharacter(BobB, B)')
        self.action('SetPosition(BobB, BobsHouse.Door)')
        self.action('SetCameraFocus(BobB)')
        self.action('SetCameraMode(focus)')
        self.currentFocusMode = "focus"
        self.action('ShowMenu()')
        self.action('HideMenu()')

    def action(self, command):
        print('start ' + command)
        while True:
            i = input()
            if not i.startswith('succeeded Wait'):
                if i == 'succeeded ' + command or i.startswith("started Reset()"):
                    self.outputBox.insert(INSERT, i + '\n')
                    return True
                elif i.startswith('failed'):
                    ctypes.windll.user32.MessageBoxW(0, "failed" + str(command), "Fail Detected", 1)
                    self.outputBox.insert(INSERT, i + '\n')
                    return False
                elif i.startswith('error'):
                    self.outputBox.insert(INSERT, i + '\n')
                    ctypes.windll.user32.MessageBoxW(0, "error " + str(command), "Error Detected", 1)
                    return False
            else:
                return True


newUI = TestingGui(root)
root.mainloop()
