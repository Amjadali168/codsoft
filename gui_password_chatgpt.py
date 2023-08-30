import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("420x500")
        self.root.configure(bg="white")

        self.heading_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold", "underline"), bg="white", fg="dark blue")
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=2)

        self.username_label = tk.Label(root, text="Enter User Name:", font=("Arial", 14, "bold"), fg="black", bg="white")
        self.username_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")

        self.username_entry = tk.Entry(root, font=("Arial", 14), relief="ridge")
        self.username_entry.grid(row=1, column=1, pady=15, padx=10, sticky="w")

        self.length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 14, "bold"), fg="black", bg="white")
        self.length_label.grid(row=2, column=0, pady=10, padx=10, sticky="e")

        self.length_entry = tk.Entry(root, font=("Arial", 14), relief="ridge")
        self.length_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        # Add a label for the "Generate Password" field
        self.generated_password_label = tk.Label(root, text="Generate Password:", font=("Arial", 14, "bold"), fg="black", bg="white")
        self.generated_password_label.grid(row=3, column=0, pady=10, padx=10, sticky="e")

        # Add an entry field for the generated password
        self.generated_password_entry = tk.Entry(root, font=("Arial", 14), relief="ridge")
        self.generated_password_entry.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, fg="dark blue", bg="white", font=("Arial", 14))
        self.generate_button.grid(row=4, column=1, pady=10, padx=10)

        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password, font=("Arial", 12), bg="white",fg="dark blue")
        self.accept_button.grid(row=5, column=1, pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_password, font=("Arial", 12), bg="white",fg="dark blue")
        self.reset_button.grid(row=6, column=1, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = 3

            if length <= 0:
                raise ValueError("Invalid length. Please enter a positive integer.")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.generated_password_entry.delete(0, tk.END)  # Clear the entry field
            self.generated_password_entry.insert(0, password)  # Insert the generated password
        except ValueError as e:
            self.generated_password_entry.delete(0, tk.END)  # Clear the entry field
            self.generated_password_entry.insert(0, str(e))  # Display error message

    def accept_password(self):
        generated_password = self.generated_password_entry.get()
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password_entry.delete(0, tk.END)
        print("Accepted Password:", generated_password)

    def reset_password(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
