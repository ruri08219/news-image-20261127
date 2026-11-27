# news-image-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/ruri08219/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/ruri08219/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Friday 27 November: 41 date-checked stories, 6 regions, 13 drawn.

One image that sums up the world's news of Friday 27 November 2026, for
make.fun's "Sum up 27 November's world news in one image" bounty ($100 in USDC).

## What is on the page

- **Lead stories:** Australia's parliament passes a 20% domestic gas
  reservation law; New Zealand's final election result is due today
  (official count, ~400,000 special votes); Black Friday begins in the
  US as inflation squeezes shoppers.
- **10 more stories** with drawn illustrations, then **28 more** in the
  numbered "ALSO ON 27 NOVEMBER" list — 41 stories in all.
- **THE DAY IN UTC** timeline, **STORIES BY REGION** bar (Asia-Pacific 26,
  Europe 5, Americas 4, Middle East 3, Africa 1, Science / Global 2),
  a numbered world map (**WHERE IT HAPPENED**), a **HOW SURE** legend
  (CONFIRMED / OFFICIAL / REPORTED), and a **DATE CHECK** footer that
  also lists the other days' news left out (Houthi strike on Aramco
  Jazan — 26 Nov; UK net migration 77,000 — 26 Nov; Bank of Korea rate
  3.25% — 26 Nov; US tariffs — 25 Nov; Democrats' House majority — 24 Nov).

Every story on the page happened, or was first reported, on 27 November 2026.

## Verification

To confirm the entry image is intact:

1. Run `python3 main.py` — it verifies `entry.png` before copying it.
2. Check the output copy's SHA-256 equals `79a03f8a06a65e536256e3c565947a5e7768620f51ab60274edd17da3718da26`.
3. The image is 1024x1024 and 184124 bytes; a size or hash mismatch stops the script with an error and a non-zero exit code.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program uses only the Python standard library, so it runs anywhere
Python 3 is installed. No network is needed.

## License

MIT — see [LICENSE](LICENSE).
