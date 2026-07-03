import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from duplicate_finder import DuplicateFinderEngine

# Configure default global application theme styles
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class DuplicateFinderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure layout window parameters
        self.title("Smart Duplicate File Finder")
        self.geometry("600x450")
        self.resizable(False, False)
        
        # Load the backend fingerprint calculation engine
        self.engine = DuplicateFinderEngine()
        self.found_duplicates = {}

        # ----------------- GRAPHICAL UI COMPONENT LAYOUT -----------------
        
        # Header Branding Label
        self.header_label = ctk.CTkLabel(
            self, text="⚡ Smart Duplicate Finder", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.header_label.pack(pady=20)
        
        # Folder Path Tracking Row Frame
        self.path_frame = ctk.CTkFrame(self)
        self.path_frame.pack(pady=10, padx=40, fill="x")
        
        self.path_entry = ctk.CTkEntry(
            self.path_frame, placeholder_text="Select a folder to deep-scan...", 
            width=340
        )
        self.path_entry.pack(side="left", padx=10, pady=10)
        
        self.browse_btn = ctk.CTkButton(
            self.path_frame, text="Browse", width=80, command=self.browse_folder
        )
        self.browse_btn.pack(side="right", padx=10, pady=10)
        
        # Live Operational Display Feedback Box
        self.display_box = ctk.CTkTextbox(self, width=520, height=180, font=ctk.CTkFont(size=12))
        self.display_box.pack(pady=15)
        self.display_box.insert("0.0", "System Status: Idle.\nSelect a target directory folder and click 'Scan Folder' to find hidden file duplicates using digital fingerprinting.")
        self.display_box.configure(state="disabled")
        
        # Bottom Execution Action Buttons Frame
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=15, fill="x", padx=40)
        
        self.scan_btn = ctk.CTkButton(
            self.btn_frame, text="🔍 Scan Folder", width=240, height=40,
            font=ctk.CTkFont(size=14, weight="bold"), command=self.start_scan
        )
        self.scan_btn.pack(side="left", padx=10)
        
        self.purge_btn = ctk.CTkButton(
            self.btn_frame, text="🗑️ Purge Duplicates", width=240, height=40,
            fg_color="#D9534F", hover_color="#C9302C", # Professional red warning colors
            font=ctk.CTkFont(size=14, weight="bold"), command=self.start_purge
        )
        self.purge_btn.pack(side="right", padx=10)
        self.purge_btn.configure(state="disabled")

    # ----------------- APPLICATION LOGIC OPERATIONS -----------------

    def browse_folder(self):
        """Launches a native point-and-click Windows directory selector window."""
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, selected_dir)

    def start_scan(self):
        """Triggers the background MD5 hashing scanner loop loop on the target folder."""
        target_dir = self.path_entry.get().strip()
        if not target_dir or not os.path.exists(target_dir):
            messagebox.showerror("Error", "Please select a valid folder path directory target first!")
            return
            
        # Unlock textbox to update tracking summary text
        self.display_box.configure(state="normal")
        self.display_box.delete("0.0", "end")
        self.display_box.insert("0.0", f"Analyzing digital fingerprints inside:\n{target_dir}...\n\nPlease wait...")
        self.update()
        
        # Execute the directory hash loop scan
        self.found_duplicates, total_count, total_mb = self.engine.scan_directory(target_dir)
        
        self.display_box.delete("0.0", "end")
        if total_count == 0:
            self.display_box.insert("0.0", "✨ Scan Complete: Perfect Optimization!\nNo true duplicate files or matching digital fingerprints were found inside this directory.")
            self.purge_btn.configure(state="disabled")
        else:
            summary_text = f"🚨 Scan Complete: Found {total_count} Duplicate Files!\n"
            summary_text += f"📦 Total hidden space waste: {total_mb} Megabytes.\n\n"
            summary_text += "Click the red 'Purge Duplicates' button below to safely delete these duplicate copies from your hard drive, keeping the original versions secure."
            self.display_box.insert("0.0", summary_text)
            self.purge_btn.configure(state="normal")
            
        self.display_box.configure(state="disabled")

    def start_purge(self):
        """Iterates through and safely drops duplicate file references."""
        # Convert tracked dict items to an unrolled execution path list
        all_purge_paths = []
        for paths in self.found_duplicates.values():
            all_purge_paths.extend(paths)
            
        if not all_purge_paths:
            return
            
        confirm = messagebox.askyesno(
            "Confirm Purge", 
            f"Are you sure you want to permanently delete all {len(all_purge_paths)} duplicate files?\n\nThis will instantly free up disk space while keeping your original source files safe."
        )
        
        if confirm:
            deleted = self.engine.purge_duplicates(all_purge_paths)
            messagebox.showinfo("Success", f"Cleanup complete! Successfully deleted {deleted} duplicate files from your computer storage drive.")
            
            # Reset visual display box states
            self.display_box.configure(state="normal")
            self.display_box.delete("0.0", "end")
            self.display_box.insert("0.0", "System Status: Idle.\nStorage optimization completed successfully.")
            self.display_box.configure(state="disabled")
            self.path_entry.delete(0, "end")
            self.purge_btn.configure(state="disabled")

if __name__ == "__main__":
    app = DuplicateFinderApp()
    app.mainloop()
