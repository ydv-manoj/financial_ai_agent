# 📈 Real-Time Multi-Agent Trading & Risk Management System

## 🚀 Overview
This project is an advanced **AI-powered trading and risk management system** that leverages **Phi-Agents, Groq LLM, OpenBB, TextBlob, and YFinance** to analyze market data, assess news sentiment, and compute risk metrics. It provides real-time financial insights and trade recommendations based on aggregated intelligence from multiple agents.

## 🏗️ Project Structure
```
trading-system/
│── agents/
│   ├── market_data_agent.py
│   ├── news_sentiment_agent.py
│   ├── risk_management_agent.py
│── trading_ai.py
│── requirements.txt
│── .env
│── README.md
```

## 🧩 Agent Responsibilities
### 1️⃣ Market Data Agent (`market_data_agent.py`)
- Fetches **real-time stock market data** using **YFinanceTools**
- Computes **technical indicators** (e.g., RSI, MACD, moving averages)
- Provides **market trend insights**

### 2️⃣ News Sentiment Agent (`news_sentiment_agent.py`)
- Collects recent news articles from **Google News, OpenBB, or other sources**
- Analyzes sentiment using **TextBlob**
- Scores news impact on stock price movement

### 3️⃣ Risk Management Agent (`risk_management_agent.py`)
- Computes risk scores based on **sentiment analysis and market volatility**
- Fetches **beta, volatility, and other risk metrics** from **OpenBB**
- Suggests a **risk-aware strategy** for trading

## 🤖 Parent Orchestrator Agent (`trading_ai.py`)
The **TradingRiskOrchestrator** combines the three agents to generate a consolidated report:
```python
trading_system = Agent(
    name="TradingRiskOrchestrator",
    team=[market_agent, news_agent, risk_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=[
        "1. Collect and aggregate real-time stock market data, news sentiment analysis, and risk metrics.",
        "2. Cross-analyze financial indicators, sentiment trends, and risk factors to identify market patterns.",
        "3. Generate a structured report summarizing market conditions, sentiment insights, risk evaluation, and potential trading opportunities.",
        "4. If uncertainty is high, highlight risk factors and suggest a cautious approach instead of trade execution.",
        "5. Ensure transparency in decision-making by showing key data sources and justifications for recommendations.",
    ],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
)
```

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/trading-system.git
cd trading-system
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and add your API keys (e.g., OpenBB, Phi, YFinance, etc.)
```ini
GROQ_API_KEY=your_phi_api_key
```

or

```bash
export GROQ_API_KEY=your_phi_api_key
```

### 4️⃣ Run the Trading System
```bash
python trading_ai.py
```

## 🏆 Features
✅ **Real-time stock market data aggregation**  
✅ **Automated news sentiment analysis**  
✅ **Risk assessment using market volatility & sentiment**  
✅ **Multi-agent architecture using Phi-Agents**  
✅ **Orchestrated trade recommendations with Groq LLM**  

## 📌 Future Enhancements
- 📊 **Web dashboard** to visualize insights
- 🤝 **Integration with brokerage APIs** for live trade execution
- 🔍 **AI-powered anomaly detection** for market movements


🚀 **Built with Phi-Agents, Groq LLM, OpenBB, YFinance, and TextBlob**

