from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from textblob import TextBlob
from openbb import obb

load_dotenv()

def compute_risk_score(text, stock_symbol):
    """
    Compute a risk score based on news sentiment and financial volatility.
    
    :param text: News article text
    :param stock_symbol: Ticker symbol of the stock
    :return: A dictionary with sentiment and risk scores
    """

    # Sentiment Analysis (TextBlob)
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)

    # Financial Risk (Volatility, Beta, etc.)
    try:
        stock_metrics = obb.econometrics.volatility(stock_symbol)
        volatility = stock_metrics['volatility']
        beta = obb.stocks.fa.beta(stock_symbol)  # Market risk measure
    except Exception as e:
        volatility = None
        beta = None
        print(f"Error fetching risk data: {e}")

    # Normalize risk score (combine sentiment & volatility)
    risk_score = abs(sentiment_score) * 100 + (volatility if volatility else 0) + (beta if beta else 0)
    
    print({
                "sentiment_score": sentiment_score,
        "subjectivity": subjectivity,
        "volatility": volatility,
        "beta": beta,
        "risk_score": risk_score
    })

    return {
        "sentiment_score": sentiment_score,
        "subjectivity": subjectivity,
        "volatility": volatility,
        "beta": beta,
        "risk_score": risk_score
    }
    

risk_agent = Agent(
    name="RiskManagementAgent",
    role="Analyze market data and news sentiment to generate risk-adjusted trade signals",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[compute_risk_score],  # You could integrate additional tools here for reinforcement learning or risk calculation.
    instructions=[
        "Combine the structured market data and sentiment scores to calculate a risk metric.",
        "Factor in historical volatility from persistent storage.",
        "Generate a detailed trade recommendation report with risk scores, confidence levels, and suggested actions.",
        "Output in a comprehensive table format."
    ],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
)
