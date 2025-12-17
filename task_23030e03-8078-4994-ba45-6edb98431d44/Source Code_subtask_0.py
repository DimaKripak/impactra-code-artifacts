# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
def load_data(file_path):
    try:
        # Load data into a pandas DataFrame
        data = pd.read_csv(file_path)
        
        # Convert timestamp column to datetime format
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Calculate change in sqrtPriceX96
def calculate_change(data):
    try:
        # Ensure sqrtPriceX96 is numeric
        data['sqrtPriceX96'] = pd.to_numeric(data['sqrtPriceX96'])
        
        # Calculate change in sqrtPriceX96
        data['change'] = data['sqrtPriceX96'].diff()
        
        return data
    except Exception as e:
        print(f"Error calculating change: {e}")
        return None

# Generate histogram of change in sqrtPriceX96
def generate_histogram(data):
    try:
        # Create a histogram of change in sqrtPriceX96
        plt.hist(data['change'].dropna(), bins=50)
        
        # Add title and labels
        plt.title('Histogram of Change in sqrtPriceX96')
        plt.xlabel('Change')
        plt.ylabel('Frequency')
        
        # Show the plot
        plt.show()
    except Exception as e:
        print(f"Error generating histogram: {e}")

# Main function
def main():
    # Load data from CSV file
    file_path = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(file_path)
    
    if data is not None:
        # Calculate change in sqrtPriceX96
        data = calculate_change(data)
        
        if data is not None:
            # Generate histogram of change in sqrtPriceX96
            generate_histogram(data)

# Run the main function
if __name__ == "__main__":
    main()