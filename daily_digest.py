import os
import random
import urllib.request
import xml.etree.ElementTree as ET
from html import escape

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]

FEEDS = [
    ("Ilm-fan 🔬", "https://phys.org/rss-feed/"),
        ("Kosmos 🌌", "https://www.nasa.gov/news-release/feed/"),
            ("Texnologiya 🤖", "https://techcrunch.com/feed/"),
                ("Psixologiya 🧠", "https://www.psychologytoday.com/us/blog/feed"),
                ]

                def get_news(url):
                    req = urllib.request.Request(
                            url, headers={"User-Agent": "Mozilla/5.0"}
                                )
                                    with urllib.request.urlopen(req, timeout=20) as response:
                                            root = ET.fromstring(response.read())

                                                items = root.findall(".//item")
                                                    if items:
                                                            item = random.choice(items[:10])
                                                                    title = item.findtext("title", "Yangilik")
                                                                            link = item.findtext("link", "")
                                                                                    return title.strip(), link.strip()

                                                                                        return None

                                                                                        posts = []
                                                                                        for category, url in FEEDS:
                                                                                            try:
                                                                                                    result = get_news(url)
                                                                                                            if result:
                                                                                                                        title, link = result
                                                                                                                                    posts.append(
                                                                                                                                                    f"<b>{category}</b>\n"
                                                                                                                                                                    f"{escape(title)}\n{escape(link)}"
                                                                                                                                                                                )
                                                                                                                                                                                    except Exception as e:
                                                                                                                                                                                            print(f"{category}: {e}")

                                                                                                                                                                                            if posts:
                                                                                                                                                                                                message = "🌍 <b>KUNLIK BILIMLAR</b>\n\n" + "\n\n".join(posts)
                                                                                                                                                                                                    data = urllib.parse.urlencode({
                                                                                                                                                                                                            "chat_id": CHANNEL,
                                                                                                                                                                                                                    "text": message,
                                                                                                                                                                                                                            "parse_mode": "HTML"
                                                                                                                                                                                                                                }).encode()
importimportimport
                                                                                                                                                                                                                                    req = urllib.request.Request(
                                                                                                                                                                                                                                            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                                                                                                                                                                                                                                                    data=data
                                                                                                                                                                                                                                                        )
                                                                                                                                                                                                                                                            with urllib.request.urlopen(req, timeout=20) as response:
                                                                                                                                                                                                                                                                    print(response.read().decode())
                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                        print("Hozircha yangilik topilmadi.")importimportimportimportimport