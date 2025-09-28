import asyncio
from utils.configs import ConfigLoader
from collectors.telegram_scrapping import TelegramCollector
from collectors.web_scrapping import WebsiteCollector
from detection.rule_base import RuleDetector
from alert.email_alert import EmailAlert

async def main():
    # Load config
    config = ConfigLoader().config

    # Init collectors
    telegram_cfg = config["collectors"]["telegram"]
    website_cfg = config["collectors"]["website"]

    telegram = TelegramCollector(
        api_id = telegram_cfg["api_id"],
        api_hash = telegram_cfg["api_hash"],
        channels = telegram_cfg["channels"]
    )

    website = WebsiteCollector(
        urls=website_cfg
    )

    # Init detector
    detector = RuleDetector(
        keywords=config["detection"]["keywords"],
        regex_rules=config["detection"]["regex"]
    )

    # Init Alert
    alert_config = config["alert"]

    alert = EmailAlert(
        smtp_server= alert_config["smtp_server"],
        smtp_port= alert_config["smtp_port"],
        sender=alert_config["sender"],
        password=alert_config["password"],
        receiver=alert_config["receiver"]
    )

    # colect data
    message = await telegram.fetch_message(limit=30)
    contents = website.fetch_content()

    # Detect suspicious content
    for text in message + contents:
        findings = detector.detect(text)
        if findings:
            body = f"Suspicious content detected: \n\n{text[:500]}\n\nFindings: {findings}"
            alert.send_alert("Data Leak Alert", body)

if __name__ == '__main__':
    asyncio.run(main())