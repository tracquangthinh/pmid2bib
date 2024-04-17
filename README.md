# PMID2BIB

**pmid2bib** is a tool to extract PMID in your tex files and convert them to BIB profiles.


## Installation
```
git clone https://github.com/tracquangthinh/pmid2bib.git
cd pmid2bib
pip install .
```

## How to use

Suppose you have some PMIDs in your **my_file** tex file:


```
This is a citation [PMID: 26432225].
```

You can extract BIB by a simple command line:

```
pmid2bib -i path_to_my_file
```

Your output will be saved in **path_to_my_file/bib_out**, including two files:

```
This is a citation \cite{pmid26432225}.
```

```
@article{pmid26432225,
	Author = {Green, E. D.  and Watson, J. D.  and Collins, F. S. },
	Title = {{{H}uman {G}enome {P}roject: {T}wenty-five years of big biology}},
	Journal = {Nature},
	Year = {2015},
	Volume = {526},
	Number = {7571},
	Pages = {29--31}
}
```




