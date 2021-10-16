import CamelotLists
from tkinter import *
from tkinter import ttk

# sets the root for the testing window
import Location

root = Tk()
root.title('Camelot Testing Environment')

Hair_Color = ["gray", "black", "brown", "red", "blonde"]
cottage_locations = ["Door", "Bed", "Chair", "Table", "Shelf", "Bookshelf", "Chest"]


class TestingGui:
    def __init__(self, master):
        self.focusCharacter = "BobB"
        self.characters = ['BobA', 'BobB', 'BobC', 'BobD', 'BobE', 'BobF', 'BobG', 'BobH']
        self.locationName = "BobsHouse"
        self.waitTime = .5
        self.isInputEnabled = False
        self.myButton = Button(master, text="Run Command", command=self.get_input)
        self.clearButton = Button(master, text="Clear", command=self.clear_output)
        self.commandBox = Text(master, height=5, width=40)
        self.outputBox = Text(master, height=12, width=40)
        self.clothingBoxButton = Button(master, text="Clothing", command=self.clothing)
        self.eyeColorButton = Button(master, text="Eye Color", command=self.eye_color)
        self.hairStylesButton = Button(master, text="Hair Styles", command=self.hair_style)
        self.defaultButton = Button(master, text="Default", command=self.default)
        self.hair_colorButton = Button(master, text="Hair Color", command=self.hair_color)
        self.skin_colorButton = Button(master, text="Skin Color", command=self.skin_color)
        self.items_button = Button(master, text="Items", command=self.items)
        self.visual_effects_button = Button(master, text="Visual Effects", command=self.visual_effects)
        self.run_aroundButton = Button(master, text="Run Around", command=self.run_around)
        self.all_clothingButton = Button(master, text="All Clothing", command=self.all_clothing)
        self.inputButton = Button(master, text="Allow input", command=self.inputEnable)
        self.openManualWindowButton = Button(master, text="Open Manual", command=self.createManualWindow)
        self.forest_button = Button(master, text="Forest Path Test",
                                    command=lambda: self.test_Place(CamelotLists.ForestPath))
        self.farm_button = Button(master, text="Farm Test",
                                  command=lambda: self.test_Place(CamelotLists.Farm))
        self.spooky_path_button = Button(master, text="Spooky Path Test",
                                         command=lambda: self.test_Place(CamelotLists.SpookyPath))

        self.commandBox.pack()
        self.myButton.pack()
        self.outputBox.pack()
        self.clearButton.pack()
        self.clothingBoxButton.pack()
        self.eyeColorButton.pack()
        self.hairStylesButton.pack()
        self.hair_colorButton.pack()
        self.skin_colorButton.pack()
        self.items_button.pack()
        self.visual_effects_button.pack()
        self.run_aroundButton.pack()
        self.all_clothingButton.pack()
        self.inputButton.pack()
        self.defaultButton.pack()
        self.openManualWindowButton.pack()
        self.forest_button.pack()
        self.farm_button.pack()
        self.spooky_path_button.pack()
        self.defaultButton.pack()

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

    def createManualWindow(self):
        manualwindow = Toplevel(root)
        manualwindow.title("Manual Experience Manager")
        manualwindow.geometry("300x300")

        clothingWindow = Button(manualwindow, text="Clothing",
                                command=lambda: self.generateClothingWindow(manualwindow))
        hairWindow = Button(manualwindow, text="HairStyle", command=lambda: self.generateHairStyleWindow(manualwindow))

        clothingWindow.pack()
        hairWindow.pack()

        manualwindow.mainloop()

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
        for i in Hair_Color:
            ttk.Button(hairStyleWindow, text=i, command=lambda i=i: self.manualhaircolor(i)).pack()

        hairStyleWindow.mainloop()

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

    def all_clothing(self):
        oldcharacter = self.focusCharacter
        # self.action('SetCameraMode(track)')
        for i in self.characters:

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
        for i in CamelotLists.Eye_Color:
            command_list = ['SetEyeColor', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def default(self):
        command_list = ['SetPosition', self.focusCharacter, self.locationName]
        self.action(self.create_command(command_list))
        command_list = ['SetClothing', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetHairStyle', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetEyeColor', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetHairColor', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetSkinColor', self.focusCharacter, str(0)]
        self.action(self.create_command(command_list))

    def hair_color(self):
        for i in Hair_Color:
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

    def test_Place(self, place: Location.Location):
        self.action("SetCameraMode(track)")
        self.action(self.create_command(["CreatePlace", place.title, place.title]))
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
                        command_list = ['CreateItem', CamelotLists.Items[1], CamelotLists.Items[1]]
                        self.action(self.create_command(command_list))
                        command_list = ['Put', self.focusCharacter, CamelotLists.Items[1],
                                        place.title + "." + location[0]]
                        self.action(self.create_command(command_list))
                    if attr == "Can Open and Close":
                        command_list = ['OpenFurniture', self.focusCharacter, place.title + "." + location[0]]
                        self.action(self.create_command(command_list))
                        command_list = ['CloseFurniture', self.focusCharacter, place.title + "." + location[0]]
                        self.action(self.create_command(command_list))
        for portal in place.exits:
            command_list = ['WalkTo', self.focusCharacter, place.title + "." + portal]
            self.action(self.create_command(command_list))
            self.action(self.create_command(["Exit", self.focusCharacter, place.title + "." + portal]))
            self.action(self.create_command(["Enter", self.focusCharacter, place.title + "." + portal]))

    def initialize(self):
        self.action('CreatePlace(BobsHouse, Cottage)')
        self.action('CreateCharacter(BobB, B)')
        self.action('SetPosition(BobB, BobsHouse.Door)')
        self.action('SetCameraFocus(BobB)')
        self.action('SetCameraMode(focus)')
        self.action('ShowMenu()')
        self.action('HideMenu()')

    def action(self, command):
        print('start ' + command)
        while True:
            i = input()
            if not i.startswith('succeeded Wait'):
                if i == 'succeeded ' + command:
                    self.outputBox.insert(INSERT, i + '\n')
                    return True
                elif i == 'failed ' + command:
                    self.outputBox.insert(INSERT, i + '\n')
                    return False
                elif i.startswith('error'):
                    self.outputBox.insert(INSERT, i + '\n')
                    return False
            else:
                return True


newUI = TestingGui(root)
root.mainloop()
