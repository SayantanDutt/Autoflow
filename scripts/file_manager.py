"""
File Management Script
Handles file operations, cleanup, and organization
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict

class FileManager:
    """File management and organization"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        print(f"[v0] FileManager initialized at {self.base_path}")
    
    def list_files(self, directory: str = None, recursive: bool = False) -> List[Dict]:
        """List files in directory"""
        target_dir = self.base_path / directory if directory else self.base_path
        print(f"[v0] Listing files in {target_dir}")
        
        files = []
        pattern = '**/*' if recursive else '*'
        
        for file_path in target_dir.glob(pattern):
            if file_path.is_file():
                stat = file_path.stat()
                files.append({
                    'name': file_path.name,
                    'path': str(file_path),
                    'size_bytes': stat.st_size,
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'type': file_path.suffix
                })
        
        print(f"[v0] Found {len(files)} files")
        return files
    
    def cleanup_old_files(self, directory: str, days: int = 30, extensions: List[str] = None) -> int:
        """Remove files older than specified days"""
        print(f"[v0] Cleaning up files older than {days} days in {directory}")
        target_dir = self.base_path / directory
        deleted_count = 0
        cutoff_date = datetime.now() - timedelta(days=days)
        
        for file_path in target_dir.glob('**/*'):
            if file_path.is_file():
                # Check extension filter
                if extensions and file_path.suffix not in extensions:
                    continue
                
                # Check file age
                file_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                if file_time < cutoff_date:
                    try:
                        file_path.unlink()
                        print(f"[v0] Deleted: {file_path.name}")
                        deleted_count += 1
                    except Exception as e:
                        print(f"[v0] Error deleting {file_path.name}: {str(e)}")
        
        print(f"[v0] Deleted {deleted_count} files")
        return deleted_count
    
    def organize_by_extension(self, directory: str = None) -> bool:
        """Organize files into folders by extension"""
        target_dir = self.base_path / directory if directory else self.base_path
        print(f"[v0] Organizing files in {target_dir} by extension")
        
        try:
            for file_path in target_dir.glob('*'):
                if file_path.is_file():
                    ext = file_path.suffix[1:] or 'no_extension'
                    ext_dir = target_dir / ext
                    ext_dir.mkdir(exist_ok=True)
                    
                    dest_path = ext_dir / file_path.name
                    shutil.move(str(file_path), str(dest_path))
                    print(f"[v0] Moved {file_path.name} to {ext}/")
            
            print("[v0] File organization completed")
            return True
        except Exception as e:
            print(f"[v0] Error organizing files: {str(e)}")
            return False
    
    def get_directory_size(self, directory: str = None) -> Dict:
        """Calculate directory size"""
        target_dir = self.base_path / directory if directory else self.base_path
        print(f"[v0] Calculating size of {target_dir}")
        
        total_size = 0
        file_count = 0
        
        for file_path in target_dir.rglob('*'):
            if file_path.is_file():
                total_size += file_path.stat().st_size
                file_count += 1
        
        return {
            'total_bytes': total_size,
            'total_mb': round(total_size / (1024**2), 2),
            'total_gb': round(total_size / (1024**3), 2),
            'file_count': file_count
        }
    
    def backup_directory(self, source: str, destination: str) -> bool:
        """Backup directory to destination"""
        source_path = self.base_path / source
        dest_path = self.base_path / destination
        
        print(f"[v0] Backing up {source} to {destination}")
        
        try:
            if dest_path.exists():
                shutil.rmtree(dest_path)
            
            shutil.copytree(source_path, dest_path)
            print("[v0] Backup completed successfully")
            return True
        except Exception as e:
            print(f"[v0] Error during backup: {str(e)}")
            return False


if __name__ == "__main__":
    manager = FileManager()
    
    # List files
    files = manager.list_files()
    
    # Get directory size
    size_info = manager.get_directory_size()
    print(json.dumps(size_info, indent=2))
