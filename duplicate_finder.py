import os
import hashlib

class DuplicateFinderEngine:
    def __init__(self):
        self.fingerprints = {}
        self.duplicate_count = 0
        self.space_savable = 0

    def calculate_md5_hash(self, file_path, block_size=65536):
        hasher = hashlib.md5()
        try:
            with open(file_path, 'rb') as f:
                buf = f.read(block_size)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = f.read(block_size)
            return hasher.hexdigest()
        except (PermissionError, FileNotFoundError):
            return None

    def scan_directory(self, target_directory):
        self.fingerprints.clear()
        self.duplicate_count = 0
        self.space_savable = 0

        for root, _, files in os.walk(target_directory):
            for filename in files:
                full_path = os.path.join(root, filename)
                file_hash = self.calculate_md5_hash(full_path)
                if not file_hash:
                    continue

                if file_hash in self.fingerprints:
                    self.fingerprints[file_hash].append(full_path)
                    self.duplicate_count += 1
                    self.space_savable += os.path.getsize(full_path)
                else:
                    self.fingerprints[file_hash] = [full_path]

        return self.get_duplicate_summary()

    def get_duplicate_summary(self):
        true_duplicates = {}
        for file_hash, paths in self.fingerprints.items():
            if len(paths) > 1:
                true_duplicates[file_hash] = paths[1:]
        
        mb_saved = round(self.space_savable / (1024 * 1024), 2)
        return true_duplicates, self.duplicate_count, mb_saved

    def purge_duplicates(self, duplicate_paths):
        deleted_count = 0
        for path in duplicate_paths:
            try:
                os.remove(path)
                deleted_count += 1
            except Exception:
                pass
        return deleted_count
