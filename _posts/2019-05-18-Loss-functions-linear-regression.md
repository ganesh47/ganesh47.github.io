---
title: "Loss Functions in Linear Regression"
date: 2019-05-18
categories: [blog]
tags: [machine-learning, statistics, optimization, linear-regression]
author: Ganesh Raman
---

Linear regression models rely on a *loss function* to quantify how far predicted values are from the actual observations. Minimizing this loss is what drives the learning process. In practice there are several ways to define the discrepancy between predictions and ground truth.

## Common Loss Functions

### Mean Squared Error (MSE)

MSE is perhaps the most widely used loss for regression. For predictions $\hat{y}$ and true values $y$:

$$L_{\mathrm{MSE}} = \frac{1}{n}\sum_{i=1}^n \bigl(\hat{y_i} - y_i\bigr)^2$$

Squaring the residuals penalizes large deviations more heavily, encouraging the model to fit outliers.

### Mean Absolute Error (MAE)

Here the absolute difference is taken instead of the square:

$$L_{\mathrm{MAE}} = \frac{1}{n}\sum_{i=1}^n |\hat{y_i} - y_i|$$

MAE is more robust to outliers because each error contributes linearly.

### Huber Loss

Huber loss combines the benefits of MSE and MAE, using a quadratic region near zero and a linear region for large residuals. With threshold $\delta$:

$$
L_{\mathrm{Huber}} = \begin{cases}
  \tfrac{1}{2}(\hat{y} - y)^2 & \text{if } |\hat{y}-y| \le \delta \\
  \delta(|\hat{y}-y| - \tfrac{1}{2}\delta) & \text{otherwise}
\end{cases}
$$

It acts like MSE close to the solution while limiting the impact of outliers.

## Loss vs. Error

*Loss* measures the objective minimized during training, while *error* often refers to how far predictions deviate from ground truth in evaluation. For example, MSE is a loss function, whereas metrics like mean absolute percentage error (MAPE) are used to report error on a test set. Lowering the loss usually reduces evaluation error, but the two terms are not strictly interchangeable.

## Optimization Strategies

To reduce errors, we must minimize the chosen loss function. Some common optimization techniques include:

- **Normal Equations:** For ordinary least squares (MSE loss), the solution has a closed form $\theta = (X^T X)^{-1} X^T y$ when the matrix inverse exists.
- **Gradient Descent:** Iteratively update the parameters in the direction that decreases the loss.
- **Stochastic Gradient Descent (SGD):** Approximates the gradient using mini-batches for scalability on large datasets.
- **Regularization:** Adding penalties like $L^1$ or $L^2$ helps prevent overfitting by discouraging extreme parameter values.

## Gradient Descent in Depth

Gradient descent updates model parameters by subtracting a fraction of the gradient from the current parameters. For linear regression using MSE, the gradient with respect to the weight vector $\boldsymbol{w}$ is:

$$\nabla_w L = \tfrac{2}{n} X^T (X\boldsymbol{w} - y)$$

The update step for learning rate $\alpha$ is then

$$\boldsymbol{w}_{t+1} = \boldsymbol{w}_t - \alpha \nabla_w L.$$

Choosing $\alpha$ is critical: too small and training is slow, too large and the algorithm may diverge. Practical variants like momentum or Adam adapt the learning rate or smooth updates to improve convergence.

Gradient descent continues until the loss stops decreasing or some stopping criterion (like a maximum number of iterations) is met. Because the MSE loss surface for linear regression is convex, gradient descent is guaranteed to find the global minimum provided the learning rate is appropriate.

In practice, the choice of loss function shapes how a model prioritizes different types of mistakes. MSE punishes large errors heavily, MAE treats every miss with equal weight, and hybrid approaches like Huber offer a compromise. Pairing the right loss with a suitable optimizer can lead to models that are both accurate and resilient.

Finally, always validate on a held-out dataset. Improvements in training loss should correspond to genuine gains in predictive performance. With these foundations—careful loss selection, efficient optimization, and thorough evaluation—you can build linear regression models that generalize well and provide reliable insights.
