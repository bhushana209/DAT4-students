Wow, you've clearly put a ton of work into the project and it looks like you're making good progress!

Here are some thoughts on your notebook:

- At the top of the notebook, I would advise giving more clarity on your project question, even if it might be obvious to some people. How do you define a "market trend", and what are you using to measure that trend? Why is that a reasonable measure? How are you defining success in answering that question?

- For any of the functions you define, it would be very helpful to have a precise description of the expected inputs and expected outputs. For instance, I'm still fuzzy on exactly what make_Xy_shift does.

- In cells 37, 45, and 49 your model is always predicting yes. You may want to check that that's not the result of a bug in your code.

- To answer your question in cell 40, it does look like you are doing cross-validation correctly, except you might want to use AUC instead of classification accuracy as your metric.

- In cells 47 and 74, you are taking the mean of your predicted probabilities. It's not clear to me why you might do that. It looks like cell 74 is printing that mean as if it's a score of your model, which is misleading because it's not a useful metric for measuring success.

- I would definitely advise against defining the same function twice in the same notebook (train_test_split_logreg_plot). That makes it very easy to make errors!

- Your results at the bottom look amazing... maybe too good to be true? I would recommend double-checking your work to make sure these results are real. Here are a couple ideas for how to do that:
    - Is it possible that you included a predictor that is highly correlated with the response variable? In other words, are there any predictor variables that implicitly know something about the response that a real-life out-of-sample data point wouldn't know about?
    - You may want to create a separate notebook that includes your best model, and only includes the code needed to read in and preprocess your data for that model. By eliminating all of the exploratory and irrelevant code, it makes it much easier to see if there are any errors.
    - Try holding out a year of data right after reading it in, then fit your best model to your training data and see how well it predicts on the held out data. If the result holds, you will have provided more validation of your results.

Regardless, this is strong work and you've done some great thinking! Let me know if you'd like to talk about any of these comments!
