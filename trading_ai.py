from phi.agent import Agent
from agents.market_data_agent import market_agent
from agents.news_sentiment_agent import news_agent
from agents.risk_management_agent import risk_agent
from phi.model.groq import Groq 
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app

load_dotenv()



# Combine market, news, and risk management agents
trading_system = Agent(
    name="TradingRiskOrchestrator",
    team=[market_agent, news_agent, risk_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=[
        "1.Aggregate outputs from all agents",
        "2. Collect and aggregate real-time stock market data, news sentiment analysis, and risk metrics.",
        "3. Cross-analyze financial indicators, sentiment trends, and risk factors to identify market patterns.",
        "4. Generate a structured report summarizing market conditions, sentiment insights, risk evaluation, and potential trading opportunities.",
        "5. If uncertainty is high, highlight risk factors and suggest a cautious approach instead of trade execution.",
        "6. Ensure transparency in decision-making by showing key data sources and justifications for recommendations.",
    ],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
)


# response = trading_system.print_response(
#     "Provide a consolidated real-time report for apple including market data, recent news sentiment, risk metrics, and trade recommendation",
#     stream=True
# )

app = Playground(agents=[trading_system]).get_app()

if __name__ == "__main__":
    serve_playground_app("trading_ai:app", reload=True, port=7777)