# M-Pesa Expense Tracker
**Live demo:** https://mpesa-expense-tracker-qvfndobch5zrdlxtzz5ewz.streamlit.app/
A tool that reads M-Pesa transaction messages, sorts them into spending
categories, and shows where your money goes.

> **Privacy:** only fake sample data is included in this repo. Never commit
> your real M-Pesa messages.

## Status

- [x] Message parser
- [x] Categorizer (food, transport, airtime, ...)
- [x] Dashboard with charts
- [x] Deployed demo

## Run it

```bash
python parser.py          # parse the sample messages
pip install pytest
pytest                    # run the tests
```

## Tech stack

Python 3.11+, regular expressions, pandas, Streamlit, pytest

## License

MIT
