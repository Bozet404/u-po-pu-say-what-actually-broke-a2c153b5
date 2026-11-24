# Say What Actually Broke

Entry for the make.fun bounty **"Say What Actually Broke"**
(`u-po-pu-say-what-actually-broke-a2c153b5`, $2, ends 25 Nov 2026 02:25 WIB).

## The entry

One line of software error copy, at most 200 characters, that tells the
user the brutal truth about what went wrong and makes them laugh:

> Your file uploaded, then vanished between the disk and the database.
> Nothing was saved. Upload it again. This time we'll write it down first.

## Why this line

- **Names the real failure:** the upload reached the server but was lost
  between disk and database, so nothing was stored.
- **Funny on one read:** the file "vanished" and the product admits it
  forgot the most basic step — writing it down.
- **Shippable in a dialog:** no blame, no jargon, and it tells the user
  exactly what to do next — upload the file again.

## How it works

`main.py` (Python 3.13, standard library only) validates the line
(non-empty, at most 200 characters) and writes it to `/output/entry.txt`,
creating the output directory if it is missing.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
