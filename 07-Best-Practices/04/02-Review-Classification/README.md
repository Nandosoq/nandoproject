## Review Classification

Measuring customer satisfaction is an important part of successful online services. Airbnb, Amazon or Uber leverage precious information contained in customer reviews to predict demand patterns, filter out low quality supply and ever improve their offer. 

In this section we want to build a classification model that will inform us, whether a review is a `low_review` or not. We define low reviews as ones with a 1 or 2 `review_score`. 

If this model is precise enough, it can help teams focus on at risk orders and target their efforts to manage and improve customer expectations. 

### Features 

- Retrieve `orders` training_set defined in previous exercises and define a new column `dim_is_low_review`. 

👉Hint: `dim_is_low_review` is defined as reviews with 1 or 2 stars.

👉 Hint: you can load existing order training set, with the following command: 

```python
from olist.order import Order 
orders = Order().get_training_data()
```

- What's the probability of getting a low order review? 
- Plot side by side distribution plot for each variable contained in `orders` object. What do you observe? 

### First Model 

We now want to build a classification model to predict whether an order is low review or not. 

- Load `orders` training data and split it with a 30% test size in `X_train`, `X_test`, `y_train`, `y_test`.

- Train a classification model with the algorithm of your choice. Evaluate the performance of your model with the following metrics: 

  - `confusion_matrix`
  - `accuracy_score`
  - `recall_score`

### More features 

Let's add more features to our model. For the sake of this exercise, we will add more features available from `olist_order_reviews_dataset`. 

- In file `olist/reviews.py`, add the method `get_training_data` that returns the following features: 

    - `review_id` (_str_) _the id of the review_
    - `order_id` (_str_) _the id of the order_
    - `review_comment_length` (_int_) _string length of review comment_
    - `product_category` (_str_) _name of the main category for that review. Main category is defined as the most expensive category in the order_.

- Plot a distribution of `review_comment_length` per `review_score`. What do you observe? 

- Fit `model_2`, the same model you used previously, but trained on a training set with those additional features. How much `accuracy` and `recall` do you gain? 

### AutoML

Using the library [Tpot](http://epistasislab.github.io/tpot/), find the best model to optimize `dim_is_low_review`. 
What is the best `accuracy` and `recall` scores you can achieve? 