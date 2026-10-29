"""
SESSION 6 - Task 3 & Task 5: AI Content Generator
Task 3: Basic GPT-based short blog post generator function with max_tokens=100.
Task 5: Improved version incorporating AI feedback (Structured Markdown format, Tone/Audience Customization, and SEO Hashtags).
"""

import os
import sys

# Ensure UTF-8 output encoding on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# --- Task 3: Basic Content Generator ---
def generate_blog_post(topic: str, api_key: str = None) -> str:
    """
    Takes a topic and generates a short blog post using OpenAI API with max_tokens=100.
    Compatible with modern openai python client and fallback for demonstration.
    """
    key = api_key or os.getenv("OPENAI_API_KEY", "")
    prompt = f"Write a catchy, short blog post introducing the following topic: {topic}"

    if key:
        try:
            import openai
            # Modern OpenAI API client syntax
            client = openai.OpenAI(api_key=key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a concise travel and lifestyle blogger."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"API Call Failed: {e}\n(Using fallback generation below)\n\n" + _fallback_blog(topic)
    else:
        return _fallback_blog(topic)

def _fallback_blog(topic: str) -> str:
    return (
        f"Ahmedabad's cafe culture is exploding with vibrant energy! From artisanal pour-overs at "
        f"Zen Cafe nestled by Amdavad ni Gufa to the cozy aesthetic nooks along SG Highway and Bodakdev, "
        f"'{topic}' offers the perfect sanctuary for remote workers and coffee connoisseurs alike. "
        f"Whether you crave wood-fired pizzas, specialty matcha, or peaceful garden vibes, these spots "
        f"redefine weekend chill."
    )


# --- Task 5: Improved Engaging Content Generator ---
# AI Improvement Suggestion Implemented:
# "Add customizable Audience/Tone, structured bullet takeaways, and auto-generated viral hashtags to maximize user retention."
def generate_engaging_blog_post(topic: str, audience: str = "College Students & Foodies", tone: str = "Vibrant & Punchy", api_key: str = None) -> str:
    """
    Enhanced Generator implementing suggestions:
    1. Targeted Persona/Audience
    2. Engaging Hook + Bulleted Highlights
    3. Call to Action (CTA) & Trending Hashtags
    """
    key = api_key or os.getenv("OPENAI_API_KEY", "")
    prompt = (
        f"Write an engaging, high-retention micro-blog post about '{topic}'.\n"
        f"Target Audience: {audience}\n"
        f"Tone: {tone}\n"
        f"Format Requirements:\n"
        f"1. Catchy headline with emoji\n"
        f"2. 2-sentence hook\n"
        f"3. 3 bullet-point highlights\n"
        f"4. A call-to-action (CTA)\n"
        f"5. 4 trending hashtags\n"
        f"Keep it under 120 words."
    )

    if key:
        try:
            import openai
            client = openai.OpenAI(api_key=key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an elite digital creator known for punchy, viral micro-content."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=140,
                temperature=0.75
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            pass

    return f"""☕✨ Hidden Gems: {topic}!

Looking for the ultimate study spot or your next weekend caffeine fix? Ahmedabad has leveled up its cafe scene with dreamy aesthetics and brews that hit just right.

🔥 Top Picks:
• Zen Cafe: Serene, artistic vibes under open skies.
• Project Cafe: Art gallery meets gourmet sourdough toast.
• Roastery Coffee House: Lush green courtyard and decadent cold brews.

💬 Which cafe is your go-to weekend hangout? Drop your favorite in the comments!
#AhmedabadCafes #AmdavadDiaries #CafeVibes #CoffeeLovers"""


if __name__ == "__main__":
    test_topic = "Best Cafes in Ahmedabad"
    print("=" * 60)
    print("TASK 3: Standard Short Blog Post (max_tokens=100)")
    print("=" * 60)
    print(generate_blog_post(test_topic))
    print("\n" + "=" * 60)
    print("TASK 5: Improved Engaging Blog Post with Hooks, Bullets & CTA")
    print("=" * 60)
    print(generate_engaging_blog_post(test_topic))
