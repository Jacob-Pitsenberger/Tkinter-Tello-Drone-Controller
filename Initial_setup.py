# import Tkinter to create our GUI.
from tkinter import Tk, Label, Button

# Class for controlling the drone via keyboard commands
class DroneController:
    def __init__(self):

        # Initialize the Tkinter window, give it a title, and define its minimum size on the screen.
        self.root = Tk()
        self.root.title("Drone Keyboard Controller - Tkinter")
        self.root.minsize(800, 600)

        # Label for displaying video stream
        self.cap_lbl = Label(self.root)

        # Create a button to send takeoff and land commands to the drone
        self.takeoff_land_button = Button(self.root, text="Takeoff/Land", command=lambda: None)

    # Method to run the application
    def run_app(self):
        try:
            # Add the button and video stream label to the window
            self.takeoff_land_button.pack(side='bottom', pady=10)
            self.cap_lbl.pack(anchor="center")

            # Start the tkinter main loop
            self.root.mainloop()

        except Exception as e:
            print(f"Error running the application: {e}")
        finally:
            # When the root window is exited out of ensure to clean up any resources.
            self.cleanup()

    # Method for cleaning up resources
    def cleanup(self) -> None:
        try:
            # Release any resources
            print("Cleaning up resources...")
            self.root.quit()  # Quit the Tkinter main loop
            exit()
        except Exception as e:
            print(f"Error performing cleanup: {e}")


if __name__ == "__main__":
    # Initialize the GUI
    gui = DroneController()
    # Call the run_app method to run tkinter mainloop
    gui.run_app()
