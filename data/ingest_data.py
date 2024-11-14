import csv
import pandas as pd

def generate_feedback_csv(df, filename="product_feedback.csv"):
    """
    Generate a CSV file with mock product feedback data.
    
    Args:
        filename (str): Name of the output CSV file
    """

    filename = "data/" + filename
    
    try:
        df.to_csv(filename, index=False)
        print(f"Successfully created {filename}")
    except Exception as e:
        print(f"Error creating CSV file: {str(e)}")


def generate_quality_ctrl_csv(df, headers, filename="quality_ctrl.csv"):
    """
    Generate a CSV file with mock product feedback data, quality control questions only.
    
    Args:
        filename (str): Name of the output CSV file
    """

    filename = "data/" + filename
    df = df[headers]
    
    try:
        df.to_csv(filename, index=False)
        print(f"Successfully created {filename}")
    except Exception as e:
        print(f"Error creating CSV file: {str(e)}")


def aggregate_feedback(df, user_filename, product_filename):
    """
    Aggregate feedback data into user-level and product-level summaries.
    
    Args:
        df (pandas.DataFrame): Input feedback DataFrame
        
    Returns:
        tuple: (user_metrics_df, product_metrics_df)
            - user_metrics_df: DataFrame with user-level metrics
            - product_metrics_df: DataFrame with product-level metrics from verified users
    """
    
    # User-level aggregation
    user_metrics = df.groupby('user_id').agg({
        'tried_feature': lambda x: (x == 'Yes').mean(),  # Quality control success rate
        'price_rating': 'mean',
        'recommend_likelihood': 'mean',
        'suggested_price': 'mean',
        'ease_of_use': 'mean',
        'feature_satisfaction': 'mean',
        'product_id': 'count'  # Number of reviews per user
    }).round(3).reset_index()
    
    # Rename columns for clarity
    user_metrics.columns = [
        'user_id',
        'quality_control_rate',
        'avg_price_rating',
        'avg_recommend_likelihood',
        'avg_suggested_price',
        'avg_ease_of_use',
        'avg_feature_satisfaction',
        'total_reviews'
    ]

    user_filename = "data/" + user_filename
    try:
        user_metrics.to_csv(user_filename, index=False)
        print(f"Successfully created {user_filename}")
    except Exception as e:
        print(f"Error creating CSV file: {str(e)}")
    
    # Product-level aggregation (filtered for verified users)
    verified_feedback = df[df['tried_feature'] == 'Yes']
    
    product_metrics = verified_feedback.groupby('product_name').agg({
        'price_rating': ['mean', 'count', 'std'],
        'recommend_likelihood': ['mean', 'std'],
        'suggested_price': ['mean', 'std'],
        'ease_of_use': ['mean', 'std'],
        'feature_satisfaction': ['mean', 'std']
    }).round(3).reset_index()
    
    # Flatten column names
    product_metrics.columns = [
        'product_name',
        'avg_price_rating', 'review_count', 'price_rating_std',
        'avg_recommend_likelihood', 'recommend_likelihood_std',
        'avg_suggested_price', 'suggested_price_std',
        'avg_ease_of_use', 'ease_of_use_std',
        'avg_feature_satisfaction', 'feature_satisfaction_std'
    ]

    product_filename = "data/" + product_filename
    try:
        product_metrics.to_csv(product_filename, index=False)
        print(f"Successfully created {product_filename}")
    except Exception as e:
        print(f"Error creating CSV file: {str(e)}")

    # print(user_metrics)
    # print(product_metrics)
    
    # return user_metrics, product_metrics

if __name__ == "__main__":
    headers = [
        'submission_date',
        'user_id',
        'product_id',
        'product_name',
        'price_rating',
        'recommend_likelihood',
        'suggested_price',
        'ease_of_use',
        'feature_satisfaction',
        'purchase_intent',
        'tried_feature',
        'additional_comments',
    ]

    data = [
        ['2024-01-15', 'U1001', 'P101', 'Smart Watch Pro', 4, 8, 249.99, 5, 4, 'Very Likely', 'Yes', 'Great features but slightly overpriced'],
        ['2024-01-15', 'U1002', 'P102', 'Wireless Earbuds', 5, 9, 129.99, 5, 5, 'Definitely', 'Yes', 'Perfect balance of quality and price'],
        ['2024-01-16', 'U1003', 'P101', 'Smart Watch Pro', 3, 6, 199.99, 4, 4, 'Maybe', 'No', 'Good product but too expensive'],
        ['2024-01-16', 'U1004', 'P103', 'Fitness Tracker', 4, 7, 89.99, 5, 3, 'Likely', 'Yes', 'Need more advanced fitness features'],
        ['2024-01-17', 'U1002', 'P102', 'Wireless Earbuds', 5, 8, 139.99, 4, 5, 'Very Likely', 'Yes', 'Battery life could be better'],
        ['2024-01-17', 'U1005', 'P103', 'Fitness Tracker', 2, 4, 59.99, 3, 2, 'Unlikely', 'No', 'Basic features only, not worth the price'],
        ['2024-01-18', 'U1006', 'P101', 'Smart Watch Pro', 5, 9, 299.99, 5, 5, 'Definitely', 'Yes', 'Premium product worth every penny'],
        ['2024-01-18', 'U1007', 'P104', 'Smart Speaker', 3, 5, 79.99, 4, 3, 'Maybe', 'No', 'Sound quality needs improvement'],
        ['2024-01-19', 'U1008', 'P104', 'Smart Speaker', 4, 7, 99.99, 5, 4, 'Likely', 'Yes', 'Good for the price point'],
        ['2024-01-19', 'U1009', 'P102', 'Wireless Earbuds', 4, 8, 119.99, 5, 4, 'Very Likely', 'Yes', 'Would recommend with minor reservations'],
        ['2024-01-20', 'U1010', 'P103', 'Fitness Tracker', 5, 8, 99.99, 4, 4, 'Likely', 'Yes', 'Great value for money'],
        ['2024-01-20', 'U1011', 'P104', 'Smart Speaker', 2, 4, 69.99, 3, 2, 'Unlikely', 'No', 'Competitors offer better value'],
        ['2024-01-21', 'U1012', 'P101', 'Smart Watch Pro', 4, 7, 229.99, 4, 4, 'Likely', 'Yes', 'Good but needs software updates'],
        ['2024-01-21', 'U1013', 'P102', 'Wireless Earbuds', 5, 9, 134.99, 5, 5, 'Definitely', 'Yes', 'Best earbuds I\'ve used'],
        ['2024-01-22', 'U1014', 'P104', 'Smart Speaker', 4, 6, 89.99, 4, 3, 'Maybe', 'No', 'Decent but room for improvement'],
        ['2024-01-23', 'U1015', 'P101', 'Smart Watch Pro', 5, 9, 279.99, 5, 5, 'Definitely', 'Yes', 'Excellent fitness tracking capabilities'],
        ['2024-01-23', 'U1016', 'P103', 'Fitness Tracker', 3, 5, 79.99, 4, 3, 'Maybe', 'No', 'Missing advanced sleep tracking'],
        ['2024-01-24', 'U1017', 'P102', 'Wireless Earbuds', 4, 7, 124.99, 5, 4, 'Likely', 'Yes', 'Noise cancellation is impressive'],
        ['2024-01-24', 'U1008', 'P104', 'Smart Speaker', 5, 8, 94.99, 4, 5, 'Very Likely', 'Yes', 'Recent software update improved performance'],
        ['2024-01-25', 'U1018', 'P101', 'Smart Watch Pro', 3, 6, 219.99, 4, 3, 'Maybe', 'No', 'Battery life needs improvement'],
        ['2024-01-25', 'U1019', 'P103', 'Fitness Tracker', 4, 8, 94.99, 5, 4, 'Likely', 'Yes', 'Great for beginners'],
        ['2024-01-26', 'U1020', 'P102', 'Wireless Earbuds', 5, 9, 139.99, 5, 5, 'Definitely', 'Yes', 'Perfect for workouts'],
        ['2024-01-26', 'U1021', 'P104', 'Smart Speaker', 3, 5, 74.99, 3, 3, 'Unlikely', 'No', 'Voice recognition needs work'],
        ['2024-01-27', 'U1022', 'P101', 'Smart Watch Pro', 4, 7, 259.99, 4, 4, 'Likely', 'Yes', 'Good integration with phone'],
        ['2024-01-27', 'U1023', 'P103', 'Fitness Tracker', 5, 8, 99.99, 5, 4, 'Very Likely', 'Yes', 'Accurate step counting'],
        ['2024-01-28', 'U1024', 'P102', 'Wireless Earbuds', 4, 8, 129.99, 4, 4, 'Likely', 'Yes', 'Good sound quality for price'],
        ['2024-01-28', 'U1025', 'P104', 'Smart Speaker', 4, 7, 89.99, 4, 4, 'Likely', 'Yes', 'Nice improvement over previous model'],
        ['2024-01-29', 'U1026', 'P101', 'Smart Watch Pro', 3, 5, 209.99, 3, 3, 'Maybe', 'No', 'Interface could be more intuitive'],
        ['2024-01-29', 'U1027', 'P103', 'Fitness Tracker', 5, 9, 104.99, 5, 5, 'Definitely', 'Yes', 'Best fitness tracker I\'ve used'],
        ['2024-01-30', 'U1028', 'P104', 'Smart Speaker', 4, 7, 84.99, 4, 4, 'Likely', 'Yes', 'Good smart home integration']
    ]

    df = pd.DataFrame(data, columns=headers)

    generate_feedback_csv(df)

    qc_headers = [
        'submission_date',
        'user_id',
        'product_id',
        'product_name',
        'tried_feature',
    ]

    generate_quality_ctrl_csv(df, qc_headers)
    aggregate_feedback(df, "user_aggregation.csv", "product_aggregation.csv")
    