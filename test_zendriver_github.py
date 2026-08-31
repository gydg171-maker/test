import asyncio
import zendriver as zd


async def main():
    print("=" * 70)
    print("ZENDRIVER - GITHUB ACTIONS BROWSER TEST")
    print("=" * 70)

    browser = await zd.start(
        headless=True,
        sandbox=False,
        browser_args=[
            "--disable-dev-shm-usage",
        ],
    )

    print("✅ Browser started")

    page = await browser.get("https://www.tiktok.com/")
    print("✅ TikTok page opened")

    await asyncio.sleep(5)

    await browser.stop()
    print("✅ Browser stopped")


if __name__ == "__main__":
    asyncio.run(main())
