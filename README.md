# postgres-full-text-search
Postgres full text search options (tsearch, trigram) examples.

Polish dictonary files come from: https://github.com/judehunter/polish-tsearch.

*.affix, *.stop and *.dict files for languages that are not supported by default
should be copied to postgres `tsearch_data` location, e.g. `/usr/share/postgresql/13/tsearch_data`