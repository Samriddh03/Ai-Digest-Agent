from app.news_fetcher import fetch_ai_news
from app.summarizer import summarize_article
from app.shorts_generator import generate_shorts
from app.email_sender import send_email

def main():
    news = fetch_ai_news()

    email_content = "🚀 Daily AI Digest\n\n"

    for i, article in enumerate(news, 1):
        title = article['title']
        print(f"\n{i}. {title}")

        # Summary
        summary = summarize_article(article)
        print("\nSummary:")
        print(summary)

        # Shorts
        shorts = generate_shorts(summary)
        print("\n🎬 Shorts Script:")
        print(shorts)

        # Add to email
        email_content += f"{i}. {title}\n\n"
        email_content += f"Summary:\n{summary}\n\n"
        email_content += f"🎬 Shorts Script:\n{shorts}\n\n"
        email_content += "-" * 50 + "\n\n"

    # Send email
    send_email(email_content)
    print("\n✅ Email sent successfully!")

if __name__ == "__main__":
    main()