export const json = {
    "title": "Product Review Survey - A24 Highest Grossing Films",
    "description": "We value your feedback. Please take a moment to review the new product.",
    "logoPosition": "right",
    "pages": [
      {
        "name": "page1",
        "elements": [
          {
            "type": "text",
            "name": "question1",
            "title": "Your User ID: ",
            "isRequired": true
          },
          {
            "type": "dropdown",
            "name": "question2",
            "title": " Product: ",
            "isRequired": true,
            "choices": [
              {
                "value": "Item 1",
                "text": "Everything Everywhere All At Once"
              },
              {
                "value": "Item 2",
                "text": "Civil War"
              },
              {
                "value": "Item 3",
                "text": "Uncut Gems"
              },
              {
                "value": "Item 4",
                "text": "Lady Bird"
              },
              {
                "value": "Item 5",
                "text": "Talk to Me"
              },
              {
                "value": "Item 6",
                "text": "Hereditary"
              },
              {
                "value": "Item 7",
                "text": "The Iron Claw"
              },
              {
                "value": "Item 8",
                "text": "Moonlight"
              },
              {
                "value": "Item 9",
                "text": "Midsommar"
              },
              {
                "value": "Item 10",
                "text": "Ex Machina"
              }
            ]
          },
          {
            "type": "rating",
            "name": "question3",
            "title": " Product Rating: ",
            "isRequired": true,
            "rateType": "smileys"
          },
          {
            "type": "boolean",
            "name": "question4",
            "title": "Would you recommend this product? "
          },
          {
            "type": "text",
            "name": "question5",
            "title": "Recommended Price: ",
            "isRequired": true
          },
          {
            "type": "text",
            "name": "question6",
            "title": "What did you like most about the product? "
          },
          {
            "type": "text",
            "name": "question7",
            "title": "What improvements would you suggest? "
          },
          {
            "type": "text",
            "name": "question8",
            "title": "Additional Comments: "
          }
        ]
      }
    ]
  }
  