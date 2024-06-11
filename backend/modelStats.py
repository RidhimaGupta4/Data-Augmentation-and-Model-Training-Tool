import os
import pandas as pd
import numpy as np 

def get_model_stats(folder):

    model_options = os.listdir(folder)
    temp = []
    for model_option in model_options:
        if os.path.isfile(os.path.join(os.path.join(folder, model_option), 'log.csv')):
            temp.append(model_option)
    
    model_options = temp
    model_options.sort()

    model_types = []
    for i, model in enumerate(model_options):
        model_types.append({'title': model, 'id':i})
    
    # print(model_options, model_types)
    
    val_precision = []
    train_accuracy = []
    val_accuracy = []
    val_recall = []
    train_f1 = []
    val_f1 = []
    train_recall = []
    train_precision = []

    ROUND = 2

    for model in model_options:
        
        try:
            # print(model, '-log.csv found')
            df = pd.read_csv(os.path.join(os.path.join(folder, model), 'log.csv'))
            columns = df.columns

            if 'accuracy' in columns:
                train_accuracy.append(str(round((df['accuracy'].values[-1])*100, ROUND))+'%')
            else:
                train_accuracy.append("NAN")

            if 'f1_m' in columns:
                train_f1.append(round(df['f1_m'].values[-1], ROUND))
            else:
                train_f1.append("NAN")

            if 'precision_m' in columns:
                train_precision.append(round(df['precision_m'].values[-1], ROUND))
            else:
                train_precision.append("NAN")

            if 'recall_m' in columns:
                train_recall.append(round(df['recall_m'].values[-1], ROUND))
            else:
                train_recall.append("NAN")

            if 'val_accuracy' in columns:
                val_accuracy.append(str(round(df['val_accuracy'].values[-1]*100, ROUND))+'%')
            else:
                val_accuracy.append("NAN")

            if 'val_f1_m' in columns:
                val_f1.append(round(df['val_f1_m'].values[-1],ROUND))
            else:
                val_f1.append("NAN")

            if 'val_precision_m' in columns:
                val_precision.append(round(df['val_precision_m'].values[-1], ROUND))
            else:
                val_precision.append("NAN")

            if 'val_recall_m' in columns:
                val_recall.append(round(df['val_recall_m'].values[-1], ROUND))
            else:
                val_recall.append("NAN")
        
 
        except:

            train_accuracy.append('NAN')
            train_f1.append('NAN')
            val_accuracy.append('NAN')
            val_f1.append('NAN')
            val_precision.append('NAN')
            val_recall.append('NAN')
            train_precision.append('NAN')
            train_recall.append('NAN')
        


    
    stats = {
            'baseline_on_original': {
                'precision': 0.995, 
                'accuracy': '99.43%',
                'recall': 0.993,
                'f1': 0.994,
            },
            'baseline_on_augmented': {
                'precision': 0.97, 
                'accuracy': '38.30%',
                'recall': 0.23,
                'f1': 0.37
            },
            'model_options': model_options,
            'model_types': model_types,
            'train_accuracy': train_accuracy,
            'val_accuracy': val_accuracy,
            'train_f1': train_f1, 
            'val_f1': val_f1,
            'val_precision': val_precision,
            'val_recall': val_recall,
            'train_precision': train_precision,
            'train_recall': train_recall,
        
        }

    return stats


# get_model_stats('static/models')