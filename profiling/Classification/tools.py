import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.metrics import roc_auc_score
import xgboost as xgb 
from sklearn.model_selection import cross_val_score 
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe, space_eval 
from hyperopt.early_stop import no_progress_loss
from functools import reduce

import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

def show_cluster_distrid(data,target):
    count = ""
    if isinstance(data, pd.DataFrame):
        count=data[target].value_counts()
    else:
        count = data.value_counts()


    count.plot(kind = 'pie', 

              figsize = (6, 6), autopct = '%1.1f%%', shadow = True)
    plt.ylabel("Target distribution")
    plt.legend()
    plt.show()


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

def Knn_nighbert_params(X_train,y_train,max_num):
    scores = []
    for i in range(1,max_num):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train,y_train)
        y_pred = knn.predict(X_train)
        scores.append(accuracy_score(y_train, y_pred))

    plt.plot(range(1,max_num),scores)
    plt.show()


def calculate_tpr_fpr(y_real, y_pred):
    '''
    Calculates the True Positive Rate (tpr) and the True Negative Rate (fpr) based on real and predicted observations
    
    Args:
        y_real: The list or series with the real classes
        y_pred: The list or series with the predicted classes
        
    Returns:
        tpr: The True Positive Rate of the classifier
        fpr: The False Positive Rate of the classifier
    '''
    
    # Calculates the confusion matrix and recover each element
    cm = confusion_matrix(y_real, y_pred)
    TN = cm[0, 0]
    FP = cm[0, 1]
    FN = cm[1, 0]
    TP = cm[1, 1]
    
    # Calculates tpr and fpr
    tpr =  TP/(TP + FN) # sensitivity - true positive rate
    fpr = 1 - TN/(TN+FP) # 1-specificity - false positive rate
    
    return tpr, fpr
def get_all_roc_coordinates(y_real, y_proba):
    
    tpr_list = [0]
    fpr_list = [0]
    for i in range(len(y_proba)):
        threshold = y_proba[i]
        y_pred = y_proba >= threshold
        tpr, fpr = calculate_tpr_fpr(y_real, y_pred)
        tpr_list.append(tpr)
        fpr_list.append(fpr)
    return tpr_list, fpr_list
def plot_roc_curve(tpr, fpr, scatter = True, ax = None):
   
    if ax == None:
        plt.figure(figsize = (5, 5))
        ax = plt.axes()
    
    if scatter:
        sns.scatterplot(x = fpr, y = tpr, ax = ax)
    sns.lineplot(x = fpr, y = tpr, ax = ax)
    sns.lineplot(x = [0, 1], y = [0, 1], color = 'green', ax = ax)
    plt.xlim(-0.05, 1.05)
    plt.ylim(-0.05, 1.05)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")


def plot_learning_curves(estimator, X_train, y_train):
    train_sizes = [*range(500,int(y_train.shape[0]/3*2),500)]  
    train_sizes, train_scores, test_scores = learning_curve(estimator, X_train, y_train, train_sizes=train_sizes, cv=5, scoring='accuracy')

    # Recalculate the mean scores and standard deviation for plotting
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    # Plotting the learning curves again
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="g")

    plt.title('Learning Curves for a Classification Model')
    plt.xlabel('Training set size')
    plt.ylabel('accuracy Score')
    plt.legend(loc="best")
    plt.grid()
    plt.show()
    

def val_curve_params(model, X, y, param_name, param_range, scoring="accuracy", cv=5):
    train_score, test_score = validation_curve(
        model, X=X, y=y, param_name=param_name, param_range=param_range, scoring=scoring, cv=cv)

    mean_train_score = np.mean(train_score, axis=1)
    mean_test_score = np.mean(test_score, axis=1)

    plt.plot(param_range, mean_train_score,
             label="Training Score", color='b')

    plt.plot(param_range, mean_test_score,
             label="Validation Score", color='g')

    plt.title(f"Validation Curve for {type(model).__name__}")
    plt.xlabel(f"Number of {param_name}")
    plt.ylabel(f"{scoring}")
    plt.tight_layout()
    plt.legend(loc='best')
    plt.show(block=True)
from sklearn import metrics

def get_metrics(y_pred,y_true):
    accuracy = metrics.accuracy_score(y_true, y_pred)
    f1_score = metrics.f1_score(y_true, y_pred, average='weighted')
    precision = metrics.precision_score(y_true, y_pred, average='weighted')
    recall = metrics.recall_score(y_true, y_pred, average='weighted')
    confusion_matrix=metrics.confusion_matrix(y_true, y_pred)
    evaluation_dict = {
        'Accuracy': accuracy,
        'F1 Score': f1_score,
        'Precision': precision,
        'Recall': recall,
        'confusion_matrix':confusion_matrix
    }
    return evaluation_dict
    
def make_confusion_matrix(cf,
                          group_names=None,
                          categories='auto',
                          count=True,
                          percent=True,
                          cbar=True,
                          xyticks=True,
                          xyplotlabels=True,
                          sum_stats=True,
                          figsize=None,
                          cmap='Blues',
                          title=None):
   



    # CODE TO GENERATE TEXT INSIDE EACH SQUARE
    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names)==cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    if percent:
        group_percentages = ["{0:.2%}".format(value) for value in cf.flatten()/np.sum(cf)]
    else:
        group_percentages = blanks

    box_labels = [f"{v1}{v2}{v3}".strip() for v1, v2, v3 in zip(group_labels,group_counts,group_percentages)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0],cf.shape[1])


    # CODE TO GENERATE SUMMARY STATISTICS & TEXT FOR SUMMARY STATS
    if sum_stats:
        #Accuracy is sum of diagonal divided by total observations
        accuracy  = np.trace(cf) / float(np.sum(cf))

        #if it is a binary confusion matrix, show some more stats
        if len(cf)==2:
            #Metrics for Binary Confusion Matrices
            precision = cf[1,1] / sum(cf[:,1])
            recall    = cf[1,1] / sum(cf[1,:])
            f1_score  = 2*precision*recall / (precision + recall)
            stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy,precision,recall,f1_score)
        else:
            stats_text = "\n\nAccuracy={:0.3f}".format(accuracy)
    else:
        stats_text = ""


    # SET FIGURE PARAMETERS ACCORDING TO OTHER ARGUMENTS
    if figsize==None:
        #Get default figure size if not set
        figsize = plt.rcParams.get('figure.figsize')

    if xyticks==False:
        #Do not show categories if xyticks is False
        categories=False


    # MAKE THE HEATMAP VISUALIZATION
    plt.figure(figsize=figsize)
    sns.heatmap(cf,annot=box_labels,fmt="",cmap=cmap,cbar=cbar,xticklabels=categories,yticklabels=categories)

    if xyplotlabels:
        plt.ylabel('True label')
        plt.xlabel('Predicted label' + stats_text)
    else:
        plt.xlabel(stats_text)
    
    if title:
        plt.title(title)
def xgb_objective(space):
    results = xgb.cv(space, 
                   dtrain=dtrain_clf, #DMatrix (xgboost specific)
                   num_boost_round=500, 
                   nfold=5, 
                   stratified=True,  
                   early_stopping_rounds=20,
                   metrics = ['mlogloss','auc','merror'])
  
    best_score = results['test-merror-mean'].max()
    return {'loss':-best_score, 'status': STATUS_OK}
def objective(space):
    cv_results = cross_validate(rf_final,X_train, y_train, cv=5, scoring=["max_error"])
    best_score = cv_results['test_accuracy'].mean()
    return {'loss':-best_score, 'status': STATUS_OK}

def ROC_multi_class(model_multiclass,y_pred_u,y_proba,X_test,y_test,target):
    classes = model_multiclass.classes_
    # Plots the Probability Distributions and the ROC Curves One vs Rest
    plt.figure(figsize = (12, 8))
    bins = [i/20 for i in range(20)] + [1]
    roc_auc_ovr = {}

    for i in range(len(classes)):
        # Gets the class
        c = classes[i]

        # Prepares an auxiliar dataframe to help with the plots
        df_aux = X_test.copy()
        try:
            df_aux['class'] = [1 if y == c else 0 for y in y_test[target]]
        except:
            df_aux['class'] = [1 if y == c else 0 for y in y_test]
            pass
       
        df_aux['prob'] = y_proba[:, i]
        df_aux = df_aux.reset_index(drop = True)

        # Plots the probability distribution for the class and the rest
        ax = plt.subplot(2, len(classes), i+1)
        sns.histplot(x = "prob", data = df_aux, hue = 'class', color = 'b', ax = ax, bins = bins)
        ax.set_title(c)
        ax.legend([f"Class: {c}", "Rest"])
        ax.set_xlabel(f"P(x = {c})")

        # Calculates the ROC Coordinates and plots the ROC Curves
        ax_bottom = plt.subplot(2, len(classes), i+1+len(classes))
        tpr, fpr = get_all_roc_coordinates(df_aux['class'], df_aux['prob'])
        plot_roc_curve(tpr, fpr, scatter = False, ax = ax_bottom)
        ax_bottom.set_title("ROC Curve OvR")

        # Calculates the ROC AUC OvR
        roc_auc_ovr[c] = roc_auc_score(df_aux['class'], df_aux['prob'])
    plt.tight_layout()
    
    
def box_plot_dic(metrics):
    dic=metrics.copy()
    dic.pop('confusion_matrix')
    metric_names = list(dic.keys())
    metric_values = list(dic.values())

    # Define colors for each bar
    colors = ['skyblue', 'salmon', 'lightgreen', 'orange']

    # Plotting
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed

    # Plot horizontal bars with different colors
    plt.barh(metric_names, metric_values, color=colors[:len(metric_names)])

    plt.xlabel('Metric Value')
    plt.ylabel('Metric Name')
    plt.title('Metrics Plots')
    plt.show()


def graphs(metrics,model,y_pred,y_proba,X_test,y_test):
    box_plot_dic(metrics)
    plt.show()
    print('                    /*************************************\                   ')

    make_confusion_matrix(metrics['confusion_matrix'], figsize=(8,6), cbar=False)
    plt.show()
    print('                    /*************************************\                   ')
    #ROC_multi_class(model,y_pred,y_proba,X_test,y_test)
    plt.show()
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
    
        
def Gridhyperparameter(model,grid_search_space,X_train,y_train):
                                  
    grid =GridSearchCV(SVC(),param_grid=param_grid,refit=True,verbose=3,random_state=100,n_jobs=-1)
    grid.fit(X_train,y_train)
    best_params_=grid.best_params_
    best_estimator=grid.best_estimator_
    return best_params_                            
                                  
def Randomhyperparameter(model,search_space,X_train,y_train):
    
    rf_randomcv=RandomizedSearchCV(estimator=model,param_distributions=search_space,n_iter=100,cv=3,verbose=2,
                               random_state=100,n_jobs=-1)
    rf_randomcv.fit(X_train,y_train)
    best_param=rf_randomcv.best_params_

    best_estimator=rf_randomcv.best_estimator_
    return  best_param                            
                                  
    
def baysien_hyperparamters(model,search_space,X_train,y_trainxgb=False):
    trials = Trials()
    if xgb==True:
        dtrain_clf = xgb.DMatrix(X_train, y_train, enable_categorical = True)
        best_hyperparams = fmin(fn=xgb_objective, space=search_space,algo=tpe.suggest,max_evals=500,trials=trials, return_argmin=False, early_stop_fn=no_progress_loss(10))
    else:
        best_hyperparams = fmin(fn=objective, space=search_space,algo=tpe.suggest,max_evals=500,trials=trials, return_argmin=False, early_stop_fn=no_progress_loss(10))
                          
    best_params = best_hyperparams.copy()

    # `eval_metric` is a key that is not a hyperparameter of the classifier
    if 'eval_metric' in best_params:
        best_params = {key:best_params[key] for key in best_params if key!='eval_metric'}

    print('Bayesin Optimiazation best :',best_params)
    return best_params                             
        

    

    
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
       
def modeling(model,X,y,grid_search_space,proba=True):
    # Split Data
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    
    y_proba=0
    # Start with the default model 
    default_model=  model()    
    plot_learning_curves(default_model, X_train, y_train)
    default_model.fit(X_train,y_train)
    y_pred=default_model.predict(X_test)
    if proba==True:
        y_proba=default_model.predict_proba(X_test)
        plot_importance(default_model,X_train)
    metrics=get_metrics(y_pred,y_test)
    print(metrics)
    graphs(metrics,default_model,y_pred,y_proba,X_test,y_test)
    #
    # Optimization Process :
    # Grid Hyperparameters
    name_optimizer=['Random']
    #best_params=Gridhyperparameter(model(),grid_search_space,X_train,y_train)
    #optimized_liste.append(best_params)
    # Random Hyperparameters
    best_params=Randomhyperparameter(model(),grid_search_space,X_train,y_train)
    optimized_liste=[]
    optimized_liste.append(best_params)
    # Baysien Hyperparameters 
    #best_params= baysien_hyperparamters(model(),baysien_search_space,xgb)
    #optimized_liste.append(best_params)
    # Compare results hyperpar technique
    print('\n\n\n'  )                        
    for optimized_model_param in optimized_liste:  
        print('***************** ',name_optimizer[optimized_liste.index(optimized_model_param)],' **************************\n'  )                                         
       
        print('Best Params= ',optimized_model_param)
        optimized_model= model(**optimized_model_param)                       
        optimized_model.fit(X_train,y_train)
        y_pred=optimized_model.predict(X_test)
        if proba==True:
            y_proba=optimized_model.predict_proba(X_test)
            plot_importance(optimized_model,X_train)
        plot_learning_curves(optimized_model, X_train, y_train)

        metrics=get_metrics(y_pred,y_test)
        print(metrics)

        graphs(metrics,optimized_model,y_pred,y_proba,X_test,y_test)    

        print('                    /*************************************\n'  )

    return optimized_model_param  
