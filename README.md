# RSP/VGT Pair Trading Strategy

Mean-reversion pair trading between S&P 500 Equal Weight (RSP) and Technology Sector (VGT).

## Performance

Backtested 2020-2025:
- Average return: **11.92%**
- Worst case: **6.50%**
- Best case: **15.01%**

## Strategy

**Entry:**
- Short RSP / Long VGT when ratio RSI > 65
- Long RSP / Short VGT when ratio RSI < 30

**Exit:**
- Close when ratio RSI returns to 50

**Parameters:**
- Capital usage: 90%
- Market-neutral (always hedged)

## Usage

Backtest:
```bash
python3 backtest_final_rsp_vgt.py
```

Live trading:
```bash
python3 run_live_rsp_vgt.py
```

## Files

- `backtest_final_rsp_vgt.py` - Backtest engine
- `run_live_rsp_vgt.py` - Live deployment
- `rsp_vgt_3period_optimization.csv` - Optimization results

## Results

Tested across 45 different ETF pairs. RSP/VGT was the only pair profitable in all market regimes (2020-2022, 2022-2024, 2024-present).
