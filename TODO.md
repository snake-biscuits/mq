# TODOs

## Core Operation

 * `.md` -> `base` Python Objects
 * `base` -> `.json` w/ `json.JsonEncoder`
 * `.json` -> `base` w/ `json.JsonDecoder`
 * `base` -> `.md`


## Code Layout
 * `div/` & `span/` modules
   - 1 script per subclass


## Query Language

being able to navigate document heirarchy would be nice
though maybe we can't use `jq` for that directly
maybe just have reserved keywords?
or functions in our own `jq`-like language

also means we can sidestep json encoding & decoding
can still keep that for processing w/ `jq`

probably also the only way to get citations linked to an isolated prose section

need to think through some use cases
e.g. find divs meeting some criteria and give `n` lines of context after/before/both


## Manpage
 * `mq(1)`


## TUI
 * `--json`
   - return `jq` output
 * accept pipe / stdin

```sh
mq [--flags] 'query' file.md
```
