import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime, timedelta

# 데이터 로드
df = pd.read_csv('/Users/jouijae/Desktop/GitHub/research/traffic.csv')

# DateTime 컬럼을 datetime 타입으로 변환
df['DateTime'] = pd.to_datetime(df['DateTime'])

# 필요한 특성 추출: 일별 총 교통량을 사용하기 위해 날짜별 집계
df['Date'] = df['DateTime'].dt.date
daily_traffic = df.groupby('Date')['Vehicles'].sum().reset_index()

# ARIMA 모델에 사용할 시계열 데이터 생성
daily_traffic.set_index('Date', inplace=True)
traffic_series = daily_traffic['Vehicles']

# ARIMA 모델 학습
arima_model = ARIMA(traffic_series, order=(5, 1, 0))
arima_result = arima_model.fit()

# 모델 평가
print(arima_result.summary())
# 미래 날짜 설정 및 예측 수행
future_date = '2017-09-01'
future_date = datetime.strptime(future_date, '%Y-%m-%d').date()
last_date = traffic_series.index[-1]

delta_days = (future_date - last_date).days

# ARIMA 모델을 사용하여 미래의 교통량 예측
forecast = arima_result.forecast(steps=delta_days)

# 예측된 교통량 출력
print(f"Predicted Traffic Volume on {future_date}: {forecast.iloc[-1]}")

# 실제 데이터와 예측 데이터 시각화
plt.figure(figsize=(10, 6))
plt.plot(traffic_series, label='Actual Traffic')
forecast_index = pd.date_range(start=last_date + timedelta(days=1), periods=delta_days)
plt.plot(forecast_index, forecast, label='Forecasted Traffic', color='red')
plt.xlabel('Date')
plt.ylabel('Traffic Volume')
plt.title('Traffic Volume Forecast')
plt.legend()
plt.show()
