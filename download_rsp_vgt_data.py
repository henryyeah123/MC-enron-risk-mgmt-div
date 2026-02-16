#!/usr/bin/env python3
"""Download RSP and VGT data for backtesting"""

import pandas as pd
from pipeline.alpaca import (
    get_rest, save_bars, clean_market_data,
    _parse_timeframe, _normalize_bars, _to_rfc3339
)

api = get_rest()

periods = [
    ("2020-01-01", "2022-12-31", ""),
    ("2022-01-01", "2024-12-31", "_2022_2024"),
    ("2024-01-01", "2026-02-15", "_2024_today")
]

for symbol in ['RSP', 'VGT']:
    for start, end, suffix in periods:
        print(f"\nDownloading {symbol} ({start} to {end})...")
        
        bars = api.get_bars(
            symbol, _parse_timeframe("1Day"),
            start=_to_rfc3339(pd.Timestamp(start, tz="UTC")),
            end=_to_rfc3339(pd.Timestamp(end, tz="UTC")),
            limit=10000, feed="iex"
        ).df
        
        if bars is not None and not bars.empty:
            df = _normalize_bars(bars, symbol)
            raw = save_bars(df, f"{symbol}{suffix}", "1Day", "stock")
            clean = clean_market_data(raw)
            print(f"  ✓ Saved: {clean}")

print("\n✅ Complete!")
