# M-Pesa Expense Tracker

A tool that reads M-Pesa transaction messages, sorts them into spending
categories, and shows where your money goes.

> **Privacy:** only fake sample data is included in this repo. Never commit
> your real M-Pesa messages.

## Status

- [x] Message parser
- [ ] Categorizer (food, transport, airtime, ...)
- [ ] Dashboard with charts
- [ ] Deployed demo

## Run it

```bash
python parser.py          # parse the sample messages
pip install pytest
pytest                    # run the tests
```

## Tech stack

Python 3.11+, regular expressions, pytest. (Streamlit dashboard coming later.)

## License

MIT
