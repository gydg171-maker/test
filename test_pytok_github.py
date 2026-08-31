import asyncio
import importlib.metadata as metadata

from pytok.tiktok import PyTok


SEARCH_TERM = "funny videos"
MAX_RESULTS = 3


async def main():
    print("=" * 70)
    print("PYTOK - GITHUB ACTIONS BROWSER TEST")
    print("=" * 70)
    print(f"PyTok: {metadata.version('pytok')}")
    print(f"Search: {SEARCH_TERM}")
    print("Browser mode: headless=False + Xvfb")
    print()

    results = []
    seen = set()

    print("🚀 Starting PyTok...")

    async with PyTok(
        headless=False,
        request_delay=1,
        browser_args=["--no-sandbox"],
    ) as api:
        print("✅ PyTok session started")
        print()
        print(f"🔎 Searching: {SEARCH_TERM}")

        search = api.search(SEARCH_TERM)

        async for video in search.videos(count=MAX_RESULTS):
            video_id = (
                getattr(video, "id", None)
                or getattr(video, "video_id", None)
            )

            author = getattr(video, "author", None)
            username = ""

            if author:
                username = (
                    getattr(author, "unique_id", None)
                    or getattr(author, "username", None)
                    or ""
                )

            if not video_id:
                continue

            if username:
                url = f"https://www.tiktok.com/@{username}/video/{video_id}"
            else:
                url = f"https://www.tiktok.com/video/{video_id}"

            if url in seen:
                continue

            seen.add(url)
            results.append(url)
            print(f"[{len(results)}] {url}")

            if len(results) >= MAX_RESULTS:
                break

    print()
    print("=" * 70)
    print("✅ PYTOK GITHUB ACTIONS TEST COMPLETED")
    print("=" * 70)
    print(f"Links found: {len(results)}")

    if not results:
        raise RuntimeError("PyTok started but returned no TikTok video links.")


if __name__ == "__main__":
    asyncio.run(main())
