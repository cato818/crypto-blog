import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import seaborn as sns

# Configurar el estilo de las gráficas
plt.style.use('default')  # Usar estilo predeterminado
sns.set_style("whitegrid")  # Aplicar estilo de seaborn

# ...rest of the existing code...