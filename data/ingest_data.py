import csv
from datetime import datetime

def generate_feedback_csv(filename="product_feedback.csv"):
    """
    Generate a CSV file with mock product feedback data.
    
    Args:
        filename (str): Name of the output CSV file
    """

    filename = "project/data/" + filename
    
    # Define the header and data
    headers = [
        'submission_date',
        'product_id',
        'product_name',
        'price_rating',
        'recommend_likelihood',
        'suggested_price',
        'ease_of_use',
        'feature_satisfaction',
        'purchase_intent',
        'additional_comments'
    ]
    
    data = [
        ['2024-01-15', 'P101', 'Smart Watch Pro', 4, 8, 249.99, 5, 4, 'Very Likely', 'Great features but slightly overpriced'],
        ['2024-01-15', 'P102', 'Wireless Earbuds', 5, 9, 129.99, 5, 5, 'Definitely', 'Perfect balance of quality and price'],
        ['2024-01-16', 'P101', 'Smart Watch Pro', 3, 6, 199.99, 4, 4, 'Maybe', 'Good product but too expensive'],
        ['2024-01-16', 'P103', 'Fitness Tracker', 4, 7, 89.99, 5, 3, 'Likely', 'Need more advanced fitness features'],
        ['2024-01-17', 'P102', 'Wireless Earbuds', 5, 8, 139.99, 4, 5, 'Very Likely', 'Battery life could be better'],
        ['2024-01-17', 'P103', 'Fitness Tracker', 2, 4, 59.99, 3, 2, 'Unlikely', 'Basic features only, not worth the price'],
        ['2024-01-18', 'P101', 'Smart Watch Pro', 5, 9, 299.99, 5, 5, 'Definitely', 'Premium product worth every penny'],
        ['2024-01-18', 'P104', 'Smart Speaker', 3, 5, 79.99, 4, 3, 'Maybe', 'Sound quality needs improvement'],
        ['2024-01-19', 'P104', 'Smart Speaker', 4, 7, 99.99, 5, 4, 'Likely', 'Good for the price point'],
        ['2024-01-19', 'P102', 'Wireless Earbuds', 4, 8, 119.99, 5, 4, 'Very Likely', 'Would recommend with minor reservations'],
        ['2024-01-20', 'P103', 'Fitness Tracker', 5, 8, 99.99, 4, 4, 'Likely', 'Great value for money'],
        ['2024-01-20', 'P104', 'Smart Speaker', 2, 4, 69.99, 3, 2, 'Unlikely', 'Competitors offer better value'],
        ['2024-01-21', 'P101', 'Smart Watch Pro', 4, 7, 229.99, 4, 4, 'Likely', 'Good but needs software updates'],
        ['2024-01-21', 'P102', 'Wireless Earbuds', 5, 9, 134.99, 5, 5, 'Definitely', 'Best earbuds I\'ve used'],
        ['2024-01-22', 'P104', 'Smart Speaker', 4, 6, 89.99, 4, 3, 'Maybe', 'Decent but room for improvement']
    ]
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
        print(f"Successfully created {filename}")
        
    except Exception as e:
        print(f"Error creating CSV file: {str(e)}")

if __name__ == "__main__":
    generate_feedback_csv()