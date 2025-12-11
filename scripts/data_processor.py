"""
Data Processing Script
Handles data cleaning, transformation, and analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import json

class DataProcessor:
    """Main data processing class"""
    
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.data = None
        self.processed_data = None
        
    def load_data(self) -> pd.DataFrame:
        """Load data from CSV or JSON file"""
        print(f"[v0] Loading data from {self.input_file}")
        try:
            if self.input_file.endswith('.csv'):
                self.data = pd.read_csv(self.input_file)
            elif self.input_file.endswith('.json'):
                self.data = pd.read_json(self.input_file)
            else:
                raise ValueError("Unsupported file format")
            
            print(f"[v0] Data loaded successfully. Shape: {self.data.shape}")
            return self.data
        except Exception as e:
            print(f"[v0] Error loading data: {str(e)}")
            return None
    
    def clean_data(self) -> pd.DataFrame:
        """Clean and validate data"""
        print("[v0] Starting data cleaning process")
        if self.data is None:
            print("[v0] Error: No data loaded")
            return None
        
        # Remove duplicates
        initial_rows = len(self.data)
        self.processed_data = self.data.drop_duplicates()
        print(f"[v0] Removed {initial_rows - len(self.processed_data)} duplicate rows")
        
        # Handle missing values
        missing_before = self.processed_data.isnull().sum().sum()
        self.processed_data = self.processed_data.fillna(method='ffill')
        print(f"[v0] Handled {missing_before} missing values")
        
        return self.processed_data
    
    def analyze_statistics(self) -> dict:
        """Generate statistical analysis"""
        print("[v0] Analyzing data statistics")
        if self.processed_data is None:
            print("[v0] Error: No processed data available")
            return {}
        
        stats = {
            'total_rows': len(self.processed_data),
            'total_columns': len(self.processed_data.columns),
            'memory_usage': str(self.processed_data.memory_usage(deep=True).sum()),
            'numeric_summary': self.processed_data.describe().to_dict(),
            'data_types': self.processed_data.dtypes.to_dict(),
        }
        
        print("[v0] Statistics generated successfully")
        return stats
    
    def save_processed_data(self, output_file: str) -> bool:
        """Save processed data to file"""
        print(f"[v0] Saving processed data to {output_file}")
        try:
            if output_file.endswith('.csv'):
                self.processed_data.to_csv(output_file, index=False)
            elif output_file.endswith('.json'):
                self.processed_data.to_json(output_file)
            print(f"[v0] Data saved successfully")
            return True
        except Exception as e:
            print(f"[v0] Error saving data: {str(e)}")
            return False


def process_files_in_directory(directory: str, pattern: str = "*.csv"):
    """Process multiple files in a directory"""
    print(f"[v0] Processing files in {directory} with pattern {pattern}")
    path = Path(directory)
    
    for file in path.glob(pattern):
        processor = DataProcessor(str(file))
        processor.load_data()
        processor.clean_data()
        stats = processor.analyze_statistics()
        
        output_file = str(file).replace(file.suffix, '_processed.csv')
        processor.save_processed_data(output_file)
        
        print(f"[v0] Completed processing: {file.name}")


if __name__ == "__main__":
    # Example usage
    processor = DataProcessor("sample_data.csv")
    processor.load_data()
    processor.clean_data()
    stats = processor.analyze_statistics()
    processor.save_processed_data("processed_data.csv")
