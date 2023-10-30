# import Tkinter to create our GUI.
from tkinter import Tk, Label, Button
# import openCV for receiving the video frames
import cv2
# make imports from the Pillow library for displaying the video stream with Tkinter.
from PIL import Image, ImageTk


# Class for controlling the drone via keyboard commands
class DroneController:
    def __init__(self):

        # Initialize the Tkinter window, give it a title, and define its minimum size on the screen.
        self.root = Tk()
        self.root.title("Drone Keyboard Controller - Tkinter")
        self.root.minsize(800, 600)

        self.cap = cv2.VideoCapture(0)

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

            # Call the video stream method
            self.video_stream()

            # Start the tkinter main loop
            self.root.mainloop()

        except Exception as e:
            print(f"Error running the application: {e}")
        finally:
            # When the root window is exited out of ensure to clean up any resources.
            self.cleanup()

    # Method to display video stream
    def video_stream(self):
        # Read a frame from our drone
        ret, frame = self.cap.read()

        # Convert the current frame to the rgb colorspace
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        # Convert this to a Pillow Image object
        img = Image.fromarray(cv2image)

        # Convert this then to a Tkinter compatible PhotoImage object
        imgtk = ImageTk.PhotoImage(image=img)

        # Place the image label at the center of the window
        self.cap_lbl.pack(anchor="center", pady=15)

        # Set it to the photo image
        self.cap_lbl.imgtk = imgtk

        # Configure the photo image as the displayed image
        self.cap_lbl.configure(image=imgtk)

        # Update the video stream label with the current frame 
        # by recursively calling the method itself with a delay.
        self.cap_lbl.after(5, self.video_stream)

    # Method for cleaning up resources
    def cleanup(self) -> None:
        try:
            # Release any resources
            print("Cleaning up resources...")
            self.cap.release()
            self.root.quit()  # Quit the Tkinter main loop
            exit()
        except Exception as e:
            print(f"Error performing cleanup: {e}")


if __name__ == "__main__":
    # Initialize the GUI
    gui = DroneController()
    # Call the run_app method to run tkinter mainloop
    gui.run_app()
