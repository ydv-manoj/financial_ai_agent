from phi.tools.duckduckgo import DuckDuckGo
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.newspaper4k import Newspaper4k
from textblob import TextBlob


load_dotenv()

def advanced_sentiment_score(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
    subjectivity = blob.sentiment.subjectivity  # Ranges from 0 (objective) to 1 (subjective)
    print({"sentiment_score": sentiment_score, "subjectivity": subjectivity})
    return {"sentiment_score": sentiment_score, "subjectivity": subjectivity}


news_agent = Agent(
    name="NewsSentimentAgent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo(), Newspaper4k(),advanced_sentiment_score],
    instructions=[
        "Search for the latest financial news for the given stock symbol.",
        "Extract article texts using Newspaper4k.",
        "Apply advanced_sentiment_score on the extracted text to obtain a sentiment score and confidence level.",
        "Return the sentiment analysis along with source citations in Markdown format."
    ],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
)
