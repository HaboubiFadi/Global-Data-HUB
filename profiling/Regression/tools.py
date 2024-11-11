import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
import math
from functools import reduce
from sklearn.model_selection import cross_val_score 
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe, space_eval 
from hyperopt.early_stop import no_progress_loss
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score, mean_absolute_error
from statsmodels.stats.outliers_influence import variance_inflation_factor 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score 


from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_importance(model, features, num:int = 0):
    if num <= 0:
        num = features.shape[1]
    feature_imp = pd.DataFrame({'Value': model.feature_importances_, 'Feature': features.columns})
    plt.figure(figsize=(10, 10))
    sns.set(font_scale=1)
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value",
                                                                     ascending=False)[0:num])
    plt.title('Features')
    plt.tight_layout()
    plt.show()
       
def get_regression_metrics(y_pred,y_test):
    
    mse = mean_squared_error(y_pred, y_test)
    print(f'Mean Squared Error: {mse}')
    print('\n')
    r2 = r2_score(y_pred, y_test)
    print(f'R²: {r2}')
    print('\n')
    mae = mean_absolute_error(y_pred, y_test)
    print(f'Mean Absolute Error: {mae}')
    print('\n')
    print(f'Root Mean Squared Error: {    math.sqrt(mse)}')
    dic={'MSE':mse,'MAE':mae,'R2':r2,'RMSE':math.sqrt(mse)}
    return dic

     
def plot_learning_curves(estimator, X_train, y_train,scoring_type='neg_root_mean_squared_error'):
    train_sizes = [*range(500,int(y_train.shape[0]/3*2),500)]  
    train_sizes, train_scores, test_scores = learning_curve(estimator, X_train, y_train, train_sizes=train_sizes, cv=5, scoring=scoring_type)

    # Recalculate the mean scores and standard deviation for plotting
    train_scores_mean = np.mean(train_scores, axis=1)*-1
    train_scores_std = np.std(train_scores, axis=1)*-1
    test_scores_mean = np.mean(test_scores, axis=1)*-1
    test_scores_std = np.std(test_scores, axis=1)*-1

    # Plotting the learning curves again
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="g")
    label_string=scoring_type+  ' Score'
    plt.title('Learning Curves for a Regression Model')
    plt.xlabel('Training set size')
    plt.ylabel(label_string)
    plt.legend(loc="best")
    plt.grid()
    plt.show()
def VIF_features_selection(df,variance_coff):
    feature_names = df.columns
    vif = pd.DataFrame()
    vif["VIF Factor"] = [variance_inflation_factor(df, i) for i in range(df.shape[1])]
    vif["features"] = feature_names

    print('*******************')
    print('VIF Score lower than ',variance_coff)
    print(vif[vif["VIF Factor"]<=variance_coff])

    print('*******************')
    print('VIF Score higher than ',variance_coff)
    print(vif[vif["VIF Factor"]>variance_coff])
    # Plot the transposed DataFrame as a bar plot
    plt.figure(figsize=(30,17))

    sns.barplot(data=vif, x='features', y='VIF Factor')
    plt.xlabel('Features')
    plt.ylabel('Value')
    plt.title('Variance Inflation Factor ')
    plt.show()
   
    liste=list(vif[vif["VIF Factor"]<=variance_coff]['features'])
    df1=df[liste]
    return df1  



def modeling_regression(model,objective_fun,search_space,X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # Split Data 
    default_model=  model()    
    plot_learning_curves(default_model, X_train, y_train)     # Learning Curve

    default_model.fit(X_train,y_train)    #Train model
    y_pred=default_model.predict(X_test)

    metrics=get_regression_metrics(y_pred,y_test)     # Metrics (RMSE , MAE , r**2)

    print('\n\n\n')    
    print('********************** Hyperparameter Optimization ****************************')# Hyperparameter Baysien 
    
    trials = Trials()

    best_hyperparams = fmin(fn=objective_fun, space=search_space,algo=tpe.suggest,max_evals=500,trials=trials, return_argmin=False, early_stop_fn=no_progress_loss(10))

    optimized_model_param = best_hyperparams.copy()

    # `eval_metric` is a key that is not a hyperparameter of the classifier
    if 'eval_metric' in optimized_model_param:
        optimized_model_param = {key:optimized_model_param[key] for key in optimized_model_param if key!='eval_metric'}

    
    print('Best Params= ',optimized_model_param)
    optimized_model= model(**optimized_model_param)                       
    plot_learning_curves(optimized_model, X_train, y_train)     # Learning Curve

    optimized_model.fit(X_train,y_train)
    y_pred=optimized_model.predict(X_test)
    
   
    metrics=get_regression_metrics(y_pred,y_test)


    print('                    /*************************************\ \n'  )

    return optimized_model_param
from functools import reduce

def model_comparasion(liste_dic,models_names,feature_traited):
    metrics_name=list(liste_dic[0].keys())
    ldf=[]
    for i in range(len(models_names)):
        print(metrics_name[i],':',liste_dic[i].values())
        tmp = pd.DataFrame(liste_dic[i].values(), index = metrics_name,columns=[models_names[i]])
            
            
        ldf.append(tmp)
        
    frame_scores = reduce(lambda x,y: pd.merge(x,y, left_index = True, right_index = True), ldf).T
        
    
    
    fig, ax  = plt.subplots(1,1, figsize = (10,5))

    frame_scores.plot.bar(ax = ax, cmap = 'RdYlBu', edgecolor = "black")
    ax.legend(loc = 'best')
    ax.set_xlabel("Score")
    string=feature_traited+' models benchmark'
    ax.set_title(string)

def get_random_number_from_matrix(matrix):
    random_index = np.random.randint(0, matrix.shape[0])
    
    return matrix[random_index],random_index
def Lime_explainer(explainer,best_model,X_test,y_test,number_of_random_points=10):
    liste=[]
    for i in range(number_of_random_points):
        liste.append(get_random_number_from_matrix(y_test.to_numpy()))
        
    


    for i in liste:
        y_true,index=i    
        instance=X_test[index]
        y_pred=best_model.predict(instance.reshape((1,-1)))
        print('Predicted Value = ',y_pred)    
        print('\n')
        print('Real Value = ',y_true)    
             
        explanation = explainer.explain_instance(
        data_row=instance, 
        predict_fn=best_model.predict
        )
        explanation.show_in_notebook(show_table=True)
        plt.show()
        print('\n*****************************************\n')