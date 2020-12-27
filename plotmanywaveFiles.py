

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from glob import glob


data_dir = '/Files/Claps'

audio_files = glob(data_dir + '/*.wv')

audio, sfeq = lr.load(audio_files[0])

