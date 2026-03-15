from .base_agent import BaseAgent
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class AutoMLAgent(BaseAgent):
    execution_stage = 5
    def __init__(self):
        super().__init__("AutoMLAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running AutoML Predictive Analysis...")

        if not data:
            return {}

        # Prepare time-series data
        df = pd.DataFrame(data)
        if 'datetime' not in df.columns:
            return {"automl_prediction": "Insufficient Data"}

        df['datetime'] = pd.to_datetime(df['datetime'], utc=True)
        df['day'] = df['datetime'].dt.date

        daily_counts = df.groupby('day').size().reset_index(name='count')
        daily_counts['day_num'] = np.arange(len(daily_counts))

        if len(daily_counts) < 2:
            return {"automl_prediction": "Insufficient history for regression"}

        # Linear Regression for trend
        X = daily_counts[['day_num']]
        y = daily_counts['count']

        model = LinearRegression()
        model.fit(X, y)

        prediction = model.predict([[len(daily_counts)]])[0]
        trend = "INCREASING" if model.coef_[0] > 0 else "DECREASING"

        self.logger.info(f"Forecasted Activity: {trend} (Avg predicted posts/day: {round(prediction, 2)})")

        return {
            "automl_insights": {
                "trend": trend,
                "predicted_volume_next_day": round(float(prediction), 2),
                "growth_coefficient": float(model.coef_[0])
            }
        }
