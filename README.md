# Distributed Key-Value Store
This project is my attempt to create a fault-tolerant, distributed key-value store in Python. 
It is based on [NUS' Distributed Systems Lab](https://github.com/nus-sys/cs5223-labs), 
which, in turn, is based on [Ellis Michael's DSLabs](https://ellismichael.com/dslabs/).


## Getting started
To create a virtual environment and install the source code as an editable package, run:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Some implementation details
### At least once RPC
For the first version, _at least once RPC_ is implemented. The client will keep a timer and will resend the
command to the server if there's no reply when the timer expires. This process repeats until the client receives a response.
The server simply executes all commands sent by its clients. 

### Exactly once RPC
After _at least once RPC_, the next step is to implement _exactly once RPC_.
To do so, each RPC must be executed _at most once_. A unique ID is needed to identify each request, 
and the server keeps a history of requests it has already answered.
If it receives a duplicate request, it simply resends the result (without re-execution).

In this implementation, `server_address, sequence_number` tuple is used to uniquely identify the requests.

One important question is when can the server discard old requests history. To answer this, a simplifying assumption was made.
Each client is required to have _at most_ one outstanding request. Therefore, when the server receives a request having ID = X, 
it can discard all requests having ID < X.

## References and Resources
These are some resources I referred to while implementing this project.
- [DSLabs](https://ellismichael.com/dslabs/)
- [Automated Testing in Python with pytest, tox, and GitHub Actions (mCoding)](https://www.youtube.com/watch?v=DhUpxWjOhME)
- [attrs vs dataclasses (mCoding)](https://www.youtube.com/watch?v=1S2h11XronA)
- [mypy type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)