# Frontline
NETS 2130 Final Project: Crowdsourcing customer-facing employees to evaluate new products

## Architecture
Our application serves two clients: those that produce new products that need evaluation (management), and customer-facing employees that review those products (employees).

1) (5 pt) An **general interface** will serve as the primarily place where management can create surveys about their products asking questions about optimal pricing, likelihood to buy, projected usefulness, as well as the amount of fake "credits" they would put behind this product etc. This can be done using various third party tools such as Qualtrics, SurveyMonkey, or Google Forms in which the resulting data can be exported as a CSV file. On the other side, employees will provide their responses through an embedded version of the respondent survey.
   - Milestones:
     - (1) Basic setup and create proof of concept with third party survey tools
     - (2) Integrate sending survey results as a CSV file output
     - (3) Integrate feedback and dashboarding for results

3) (3 pt) A **quality control module** which has two possible implementations based on the methods we discussed in class. Embedding test questions means that the quality control algorithms would act on the data as a filter after the data has been collected in a CSV format from the third party survey tools. This is likely the method we will choose since our crowdsourcing audience is already supposed to be qualified/restricted by definition (as customer facing employees, who would know the company and its products). Therefore, we can weed out any employees who seem to be answering insincerely. In summary, the input to this module would be the raw CSV data and the output would be a filtered version in addition to a list of responses that were analyzed to be insincere. We can further enhance our quality control module by utilizing questions that establish a baseline understanding of our users. Questions like what color is an orange, or what's 2+3 allow us to weed out botted users or users which are simply moving through the survey as quickly as possible without regard for correctness.
The `generate_quality_ctrl_csv` function is specifically designed to handle quality control data by creating a CSV file that contains only certain feedback attributes. This function takes a DataFrame (df) and a list of column names (headers) as inputs, filters the DataFrame to include only the specified columns, and then saves this filtered DataFrame as a CSV file. The selected columns are specifically relevant to quality control questions, such as the product `tried_feature` status and `current_year`, which are used to verify whether the user has interacted with the feature and to validate the recency of the feedback.
   - Input: `product_feedback.csv`
   - Output: `quality_ctl.csv`
   - Code: `ingest_data.py`
   - Milestones:
     - (1) Implement basic quality control based on majority voting
     - (2) Test further methods of voting such as weighted voting and compare results

5) (5 pt) An **aggregation module** will compute relevant statistics specific to the product as well as between products. Some examples would be the most useful product, the product with the highest value (based on price someone would pay), and of course the favorable products that employees put their credits on. This involves some exploratory data analysis and calculations in dataframes. The input would be the filtered CSV data from the quality control module, and the output would be a set of relevant statistics in dataframes or possibly a CSV output.
The `aggregate_feedback` function performs most of the aggregation on the feedback data to create summary statistics at both the user and product levels. The function uses groupby on `user_id` to calculate user-level metrics, such as average ratings (`avg_price_rating`, `avg_recommend_likelihood`, etc.), a quality control rate based on the proportion of positive responses in tried_feature, and an accuracy check for the current year (`correct_year`). It then applies another groupby on `product_name`, restricted to verified feedback (where `tried_feature` is "Yes" and `current_year` is "2024"), to compute product-level metrics such as average, count, and standard deviation for ratings. These summaries are saved as separate CSV files for user-level and product-level metrics, providing an aggregated view of user engagement and product performance for further analysis.
    - Input: `product_feedback.csv`
    - Output: `product_aggregation.csv`, `user_aggregation.csv`
    - Code: `ingest_data.py`
    - Milestones:
      - (1) Achieve basic analysis of simple statistics as dataframes (e.g. lists based on highest overall rating for each column)
      - (2) Complex data analytics, including developing a weighting for the different columns and nonobvious stastics
      - (3) exporting the data in a way that the visualization / interface can use it
  

7) (2 pt) A **data visualization module** whose job is to take the relevant stastics from the aggregation module and display them in a human-friendly format for management to analyze. This code could be part of the frontend interface depending on specific implementation, and may not be a fully independent module like the others.

8) (2 pt) A **feedback rewards module** which distributes a prize to employees that bet on a successful product. This module is a big motivational aspect as employees can be rewarded from the topline profit the product makes, or a predetermined prize pool which management decides to reward after passing a certain threshold of success. It uses a simple algorithm to determine the certain employees that bet the most on a product (and not that distributed their credits evenly), for example the top 25%, and distributes the prize proportionally. 
