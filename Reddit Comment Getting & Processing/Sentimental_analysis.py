import xlrd
from textblob import TextBlob
import nltk
import numpy as np
import pandas as pd

submissions_df['polarity'] = submissions_df.apply(lambda x: TextBlob(x['body']).sentiment.polarity, axis=1)
submissions_df['subjectivity'] = submissions_df.apply(lambda x: TextBlob(x['body']).sentiment.subjectivity, axis=1)

submissions_df.to_csv('total4600-4799.csv',index=False, encoding='utf-8')
