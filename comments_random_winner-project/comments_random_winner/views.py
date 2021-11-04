from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np

def home(request):
    return render(request, 'home.html')

def comments(request):
    df = pd.read_csv('/home/imjaimeortiz/Descargas/comments_new.csv')
    df_html = df.to_html()
    return render(request, 'comments.html', {'comments' : df_html})

def winner(request):
    df = pd.read_csv('/home/imjaimeortiz/Descargas/comments_new.csv')
    chosen_idx = np.random.choice(len(df.index), replace = True, size = 1)
    df2 = df.iloc[chosen_idx]
    return render(request, 'winner.html', {'winner' : df2.to_html()})
