from setuptools import setup

setup(name='pmid2bib',
      version='0.1',
      description='Convert PMID to BIB for Latex',
      url='http://github.com/tracquangthinh/pmid2bib',
      author='Thinh Trac',
      license='MIT',
      packages=['pmid2bib'],
      install_requires=[
        'pubmed_bibtex',
        'bibtexparser @ git+https://github.com/sciunto-org/python-bibtexparser@main'
      ],
      entry_points={
          'console_scripts': ['pmid2bib=pmid2bib.pmid2bib:main'],
      },
      include_package_data=True,
      zip_safe=False)
