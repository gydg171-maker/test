import asyncio
import shutil
import sys

import zendriver as zd


async def main():
    print("=" * 70, flush=True)
    print("ZENDRIVER - GITHUB ACTIONS BROWSER DEBUG", flush=True)
    print("=" * 70, flush=True)

    print(f"Python: {sys.executable}", flush=True)
    print(
        f"Chrome path: {shutil.which('google-chrome')}",
        flush=True,
    )
    print(
        f"Chromium path: {shutil.which('chromium')}",
        flush=True,
    )

    print("STEP 1: main started", flush=True)

    print("STEP 2: starting browser...", flush=True)

    browser = await zd.start(
        headless=True,
        sandbox=False,
        browser="chrome",
        browser_executable_path="/usr/bin/google-chrome",
        browser_args=[
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
        ],
    )

    print("STEP 3: browser started", flush=True)

    print("STEP 4: opening TikTok...", flush=True)

    page = await browser.get("https://www.tiktok.com/")

    print("STEP 5: TikTok page opened", flush=True)

    await asyncio.sleep(5)

    print("STEP 6: stopping browser...", flush=True)

    await browser.stop()

    print("STEP 7: browser stopped", flush=True)

    print("=" * 70, flush=True)
    print("✅ ZENDRIVER TEST COMPLETED", flush=True)
    print("=" * 70, flush=True)


if __name__ == "__main__":
    asyncio.run(main())
