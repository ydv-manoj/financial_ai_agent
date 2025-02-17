from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq  # Using xAI wrapper for Groq-based inference
from dotenv import load_dotenv
import asyncio

load_dotenv()


market_agent = Agent(
    name="MarketDataAgent",
    model=Groq(id="qwen-2.5-32b"),
    tools=[YFinanceTools(stock_price=True, technical_indicators=True)],
    instructions=[
        "Continuously stream and validate market data for the given symbol.",
        "Compute and append technical indicators (RSI, MACD, SMA) to the data.",
        "Ensure data quality by cross-checking timestamps and volume anomalies.",
        "Return a structured JSON payload."
    ],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
)
