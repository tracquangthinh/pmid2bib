from pubmed_bibtex import bibtex_entry_from_pmid
import bibtexparser
from bibtexparser.middlewares import BlockMiddleware

class BibMiddleware(BlockMiddleware):
    def transform_entry(self, entry, *args, **kwargs):
        fields = entry.fields
        new_fields = []
        for field in fields:
            if field.key not in ["Month", "Note"]:
                if field.key == "Author":
                    authors = field.value.split("and")
                    if len(authors) > 5:
                        authors = authors[0:4]
                        authors.append(" others")
                    authors = "and".join(authors)
                    field.value = authors
                new_fields.append(field)

        entry.fields = new_fields

        # Return the transformed entry
        return entry

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)

def convert(lines):
    res_text = []
    res_bib = {}

    for line in lines:
        if "PMID" in line:
            start_pos = list(find_all(line, "[PMID"))
            end_pos = [line.find("]", s) + 1 for s in start_pos]

            replace_dict = {}

            for i in range(len(start_pos)):
                s = line[start_pos[i]:end_pos[i]]
                replace_key = s
                s = s.replace("PMID", "").replace("[", "").replace("]", "").replace(" ", "").replace(":", "")
                s = s.split(",")
                replace_values = []
                for id in s:
                    print("[Extract] PMID: " + id)
                    replace_values.append("pmid" + id)

                    bibtex = bibtex_entry_from_pmid(id)
                    bibtex = bibtexparser.parse_string(bibtex)
                    k = bibtex.entries[0].key
                    bibtex = bibtexparser.write_string(bibtex,
                            prepend_middleware=[BibMiddleware()])
                    res_bib[k] = bibtex
             
                replace_values = "\\cite{" + ",".join(replace_values) + "}"
                replace_dict[replace_key] = replace_values

            for k, v in replace_dict.items():
                line = line.replace(k, v)
            res_text.append(line)

        else:
            res_text.append(line)

    return res_text, res_bib
