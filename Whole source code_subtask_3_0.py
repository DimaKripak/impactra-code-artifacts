import matplotlib.pyplot as plt
import pandas as pd

def load_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def generate_chart(data):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data['Close'])
        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.title('ETH-USDC Chart')
        return plt
    except Exception as e:
        print(f"Error generating chart: {str(e)}")
        return None

def save_chart(chart, filename):
    try:
        plt.savefig(filename)
        print(f"Chart saved as {filename}")
    except Exception as e:
        print(f"Error saving chart: {str(e)}")

def main():
    filename = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(filename)
    if data is not None:
        chart = generate_chart(data)
        if chart is not None:
            save_chart(chart, 'eth_usdc_chart.png')

if __name__ == "__main__":
    main()