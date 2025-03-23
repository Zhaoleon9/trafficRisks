import customtkinter as ctk
from request_weather_info import Weather  # Import the weather module
from fuzzy_logic import myFuzzy  # Import the fuzzy logic function

# Initialize weather instance to get current weather info
weather = Weather()

class RiskAssessmentApp(ctk.CTk):
    """GUI for driving risk assessment"""
    def __init__(self):
        super().__init__()

        # Configure window properties
        self.title("Driving Risk Evaluation")
        self.geometry("600x300")
        
        
        # get current weather data
        self.current_snow = weather.get_snow_precipitation() 
        self.current_wind = weather.get_wind_speed() 

        # Title Label
        self.label_title = ctk.CTkLabel(self, text="Driving Risk Evaluation", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=10)

        # Snowfall Input
        self.label_snow = ctk.CTkLabel(self, text="Snow Precipitation(mm) in recent 1 hour:")
        self.label_snow.pack()
        self.entry_snow = ctk.CTkEntry(self, width=200)
        self.entry_snow.insert(0, str(self.current_snow))  # Set default value
        self.entry_snow.pack(pady=5)

        # Wind Speed Input
        self.label_wind = ctk.CTkLabel(self, text="Wind Speed (km/h):")
        self.label_wind.pack()
        self.entry_wind = ctk.CTkEntry(self, width=200)
        self.entry_wind.insert(0, str(self.current_wind))  # Set default value
        self.entry_wind.pack(pady=5)

        # Submit Button
        risk = myFuzzy(self.current_wind,self.current_snow)
        self.button_submit = ctk.CTkButton(self, text="Evaluate Driving Risk", command=self.evaluate_risk)
        self.button_submit.pack(pady=10)

        # Show Result Label
        self.label_result = ctk.CTkLabel(self, text=f"Current Risk Evaluation Results: {risk:.2f}%", font=("Arial", 14))
        self.label_result.pack(pady=10)

    def evaluate_risk(self):
        """Handle input values, evaluate risk using fuzzy logic, and display the result."""
        try:
            # Get user input values
            snow = float(self.entry_snow.get())  
            wind = float(self.entry_wind.get())  
            
            # check input values
            if snow < 0 or wind < 0:
                self.label_result.configure(text="Invalid input! Please input positive values.", fg_color="red")
                return

            # Evaluate risk using my fuzzy logic
            risk = myFuzzy(wind, snow)
            
            # Display driving assessment result
            self.label_result.configure(text=f"Current Risk Evaluation Results: {risk:.2f}%")
        
        except ValueError:
            self.label_result.configure(text="Invalid input! Please enter numbers.", fg_color="red")


# Display the window, program start.
if __name__ == "__main__":
    app = RiskAssessmentApp()
    app.mainloop()
