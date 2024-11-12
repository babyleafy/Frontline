# Frontline
NETS 2130 Final Project: Crowdsourcing customer-facing employees to evaluate new products

## Architecture
Our application serves two clients: those that produce new products that need evaluation (management), and customer-facing employees that review those products (employees).
- An general **interface** will serve as the primarily place where management can create surveys about their products asking questions about optimal pricing, likelihood to buy, projected usefulness, as well as the amount of fake "credits" they would put behind this product etc. This can be done using various third party tools such as Qualtrics, SurveyMonkey, or Google Forms in which the resulting data can be exported as a CSV file. On the other side, employees will provide their responses through an embedded version of the respondent survey.
