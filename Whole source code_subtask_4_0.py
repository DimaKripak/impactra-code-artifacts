import pandas as pd
import matplotlib.pyplot as plt

def create_chart(data):
    # Check if required columns exist
    required_columns = ['date', 'close']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Data is missing required columns")

    # Create the chart
    plt.figure(figsize=(10,6))
    plt.plot(data['date'], data['close'])
    plt.title('ETH-USDC Chart')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    return plt

def save_chart(chart, filename):
    # Save the chart as a PNG file
    chart.savefig(filename + '.png', bbox_inches='tight')
    # Save the chart as a PDF file
    chart.savefig(filename + '.pdf', bbox_inches='tight')

def load_data(filename):
    try:
        # Load the data from the CSV file
        data = pd.read_csv(filename)
        # Convert the 'date' column to datetime format
        data['date'] = pd.to_datetime(data['date'])
        return data
    except Exception as e:
        print(f"Failed to load data: {e}")
        return None

def main():
    filename = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(filename)
    if data is not None:
        chart = create_chart(data)
        save_chart(chart, 'eth_usdc_chart')
        plt.close()

if __name__ == "__main__":
    main()