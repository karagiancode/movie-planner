import customtkinter as ctk
import firebase_admin
from firebase_admin import credentials, db
from tkinter import messagebox
import threading

# --- Σύνδεση με Firebase ---
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://movie-picker-c2bb3-default-rtdb.europe-west1.firebasedatabase.app'
})

ref = db.reference('movies')


class MovieApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cloud Movie Planner 🎬")
        self.geometry("400x600")

        self.movies = []


        self.label = ctk.CTkLabel(self, text="Προσθήκη στη Λίστα", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.entry_name = ctk.CTkEntry(self, placeholder_text="Όνομα Ταινίας", width=300)
        self.entry_name.pack(pady=10)

        self.entry_director = ctk.CTkEntry(self, placeholder_text="Σκηνοθέτης/Παραγωγή", width=300)
        self.entry_director.pack(pady=10)

        self.add_button = ctk.CTkButton(self, text="Αποστολή ", command=self.add_movie_to_cloud)
        self.add_button.pack(pady=20)

        self.list_display = ctk.CTkTextbox(self, width=350, height=250)
        self.list_display.pack(pady=10)
        self.list_display.configure(state="disabled")

        # ακουσμα βασης
        threading.Thread(target=self.listen_for_changes, daemon=True).start()

    def add_movie_to_cloud(self):
        name = self.entry_name.get()
        director = self.entry_director.get()

        if name == "":
            messagebox.showwarning("Προσοχή", "Συμπλήρωσε τα πεδία!")
            return

        # Σπρώχνουμε τα δεδομένα στο Firebase
        ref.push({
            "title": name,
            "director": director
        })

        self.entry_name.delete(0, 'end')
        self.entry_director.delete(0, 'end')

    def listen_for_changes(self):
        """Αυτή η συνάρτηση τρέχει συνέχεια και περιμένει νέα δεδομένα από το Firebase"""

        def callback(event):
            # Όταν αλλάζει κάτι στη βάση, παίρνουμε όλη τη λίστα
            data = ref.get()
            self.movies = []
            if data:
                for key, value in data.items():
                    self.movies.append(value)

            # Ενημέρωση του UI (χρησιμοποιούμε after για να είναι thread-safe)
            self.after(0, self.update_list_view)

        ref.listen(callback)

    def update_list_view(self):
        self.list_display.configure(state="normal")
        self.list_display.delete("1.0", "end")
        for m in self.movies:
            self.list_display.insert("end", f"🎥 {m['title']} - {m['director']}\n")
        self.list_display.configure(state="disabled")


if __name__ == "__main__":
    app = MovieApp()
    app.mainloop()