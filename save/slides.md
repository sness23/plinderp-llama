# title
hello.  my name is shimmer and i'm on the bioAI
team led by doctor steven ness and our project
for this hackathon is to use llama3.2 to
understand and gain insights from scientific
papers in the field of molecular docking of a
ligand to a protein target.

# nobelprize
this is a field in highlight due to the recent
nobel prize in chemistry for protein design
using computers.

# mlsb
there is a neurips workshop happening in
december, the machine learning in structural
biology meeting and at that workshop there is a
competition of people using Machine Learning to
dock ligand molecules to proteins using the
plinder dataset.

# plinder
PLINDER (Protein-Ligand Interactions Dataset and
Evaluation Resource) is a comprehensive dataset
designed to enhance the prediction of
protein-ligand interactions (PLI), crucial for
small molecule drug design. The dataset consists
of 449,383 PLI systems with over 500
annotations each, enabling detailed analyses
at various structural levels, including protein,
pocket, interaction, and ligand
assessments. PLINDER aims to overcome
limitations found in existing datasets, such as
size, diversity, and information leakage that
can skew method evaluations.

# citations
recently we downloaded the plinder dataset and
looked up one of the structures doctor ness had
published in the PBD and noticed that there
was no citation information for the structures.
we contacted the PLINDER team via their discord
and they said we should download it from the PDB.

# plinderp
In order to assist the community and accellerate
research we present Plinderp, a database of
citations, metadata links to papers and in some
cases full text of papers for all the entries
in Plinder.

For this hackathon we developed a number of different
outputs.

# website
Number one, we developed a new website,
plinderp.doi.bio.  On this website we have collected
citation links for all the entries in the Plinder
dataset.  One can simply go to, for instance,
https://plinder.doi.bio/1erm and see the information
for 1erm, a beta-lactamase, that is an enzyme in E. coli
that confers drug resistance to penicillin and similar
drugs.

# full_text
Currently, some of these entries also have
additional information and metadata associated
with them.  For example, the entry for 1erm
contains a link to the full plinder entry, the
pubmed version version of the citation
information, and a link to the DOI which
provides links to where the paper can be found
online, and in this case the full text of the
TEM beta-lactamase paper, which was found as an
alternate version of the paper downloaded from
Simon Fraser University in Canada.

# api
we also developed an API for plinderp.doi.bio
that can be found at https://plinderp.doi.bio/api/v1
and can be queried using curl

# plinderpdoibio
we also developed a Python package that provides
easy access to the plinderp dataset.  It is hosted
on PyPi and can be installed with "pip install plinderpdoibio"
It also provides a fast cached copy of the original Plinder
dataset to allow for easier access to this vital community
dataset.

# llama3.2

for this hackathon we are focusing on the
Reducing Barriers for Llama Developers pillar.
In our work in hackathons for lablab.ai this
year we have noticed a lack of support for
developers in the new emerging field of
Artificial General Intelligence for Structural
Biology, a field that requires vast amounts of
data.  Developing with LLMs in this space is
complex with many challenges including data
preparation and evaluation.  Many of the papers
in the scientific literature are difficult for
automated tools to access, and breaking down
barriers in this field could help accellerate
research and science into this extremely
important area.
