import tkinter

class UnitConverterGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title("Unit Converter")
        self.main_window.geometry('500x500')

        # Create frames
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Conversion type options
        self.conversion_type = tkinter.StringVar()
        self.conversion_type.set("Kilometers to Miles")
        self.options = [
            "Kilometers to Miles",
            "Gallons to Liters",
            "Acres to Hectares"
        ]

        self.dropdown = tkinter.OptionMenu(self.top_frame, self.conversion_type, *self.options, command=self.update_prompt)
        self.dropdown.pack(side='top', pady=5)

        # Input label and entry
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in kilometers:')
        self.input_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.input_entry.pack(side='left')

        # Output label
        self.descr_label = tkinter.Label(self.mid_frame, text='Converted to miles:')
        self.value = tkinter.StringVar()
        self.result_label = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.descr_label.pack(side='left')
        self.result_label.pack(side='left')

        # Buttons
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def update_prompt(self, selection):
        if selection == "Kilometers to Miles":
            self.prompt_label.config(text="Enter a distance in kilometers:")
            self.descr_label.config(text="Converted to miles:")
        elif selection == "Gallons to Liters":
            self.prompt_label.config(text="Enter volume in gallons:")
            self.descr_label.config(text="Converted to liters:")
        elif selection == "Acres to Hectares":
            self.prompt_label.config(text="Enter area in acres:")
            self.descr_label.config(text="Converted to hectares:")

    def convert(self):
        try:
            value = float(self.input_entry.get())
            conversion = self.conversion_type.get()

            if conversion == "Kilometers to Miles":
                result = value * 0.6214
            elif conversion == "Gallons to Liters":
                result = value * 3.78541
            elif conversion == "Acres to Hectares":
                result = value * 0.404686
            else:
                result = 0

            self.value.set(f"{result:.2f}")
        except ValueError:
            self.value.set("Invalid input")

# Run the program
if __name__ == '__main__':
    UnitConverterGUI()