# Project 3
## 1 Introduction
In Project 3, you’ll conduct a comparative analysis using multiple methods
that solve the sorting problem. You’ll experiment with various approaches and
assess their performance on a chosen dataset. Find a data set that contains
a few monotonic criteria, over 100 alternatives, and at least 2 classes (if the
problem has more classes, you can binearize them). One of the following data
sets can be used [link](https://en.cs.uni-paderborn.de/is/research/research-projects/software/monotone-learning-datasets)
<br>
Briefly describe the data set including the criteria descriptions. For this dataset, train the following models: <br>
1. One interpretable ML model (XGBoost or rankSVM or Logistic Regression) <br>
2. One interpretable neural MCDA method (ANN-Ch-Constr. or ANNUTADIS) <br>
3. Neural network with a few layers with nonlinear activation functions <br>
## 2 Experiments
For each model: <br>
• report Accuracy, F1 and AUC <br>
• Models should be presented with all visualizations to facilitate interpretation. <br>
• All presented values should be rounded to a maximum of 4 decimal places. <br>
• A brief summary taking into account the conclusions of the following analyses <br>

### 2.1 Explanation of the decisions
• Explain why the decision was made for the 3 selected alternatives (In the case of a neural network, you can use, for example, a guided gradient). <br>
• Take 3 alternatives and say what the minimum change to a single criterion should be done so that the option is classified into a different class. <br>
1. Try to answer this question in an analytical way based only on the values of the model parameters and explain why such a change is minimal (without sampling).  <br>
2. Perform space sampling by slightly changing the evaluations of alternatives to get a different class. Do the results agree with theoretical predictions? <br>
3. Explain the predictions for these objects using at least one technique ([Anchors](https://github.com/marcotcr/anchor) [LIME](https://lime-ml.readthedocs.io/en/latest/), [SHAP](https://shap-lrjball.readthedocs.io/en/docs_update/index.html), ... ) <br>

### 2.2 Interpretation of the model
• Based on the parameters obtained, can we say something about the user’s preferences? <br>
• What was the influence of the criteria? Are there any criteria that have no effect, or have a decisive influence? <br>
• Are there any dependencies between the criteria? <br>
• What is the nature of the criterion, gain, cost, non-monotonic? <br>
• Whether there are any preference thresholds? Are there any evaluations on criteria that are indifferent in terms of preferences? <br>
• Interpret the model by at least one ([Global Surrogate](https://christophm.github.io/interpretable-ml-book/global.html), [Partial Dependence Plot](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html), [Permutation Feature Importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance) ...)

### A list of tools that contain various techniques for explaining and interpreting the model:
• [Shapash](https://shapash.readthedocs.io/en/latest/) <br>
• [Alibi](https://github.com/SeldonIO/alibi) <br>
• [Explainerdashboard](https://explainerdashboard.readthedocs.io/en/latest/) <br>
• [DALEX](https://github.com/ModelOriented/DALEX) <br>
• [eli5](https://eli5.readthedocs.io/en/latest/overview.html) <br>
• [aix360](https://github.com/Trusted-AI/AIX360)
