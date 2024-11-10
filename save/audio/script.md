# title
hello.  my name is shimmer and
i'm on the bioAI team.  we would
like to tell you about our project
for the llama three dot two hackathon
for lab lab.ai called accellerating
research in artificial intelligence
for structural biology

# steven_ness
we are led by doctor steven ness who
has a phd in Computer Science where he
worked on Machine Learning and UX.  his
primary experience is in structural biochemistry
and has been in the field since 1987.

# tem7a
our project for this hackathon is to use
llama three dot two to understand and
gain insights from scientific papers in
the field of molecular docking of a
ligand to a protein target.

# tem7
Protein-small molecule drug docking involves simulating how ligands bind to target proteins, focusing on their complementary shapes and interactions. This process reveals binding affinities and the specific molecular interactions, such as hydrogen bonds and hydrophobic contacts.

# tem7b
By understanding these binding patterns, researchers can optimize ligand design for improved therapeutic efficacy.

# nobelprize
this is a field in highlight due to the recent
nobel prize in chemistry for protein design
using computers.

# mlsb2024
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
small molecule drug design.

# plinder1
The dataset consists
of 449,383 PLI systems with over 500
annotations each, enabling detailed analyses
at various structural levels, including protein,
pocket, interaction, and ligand
assessments.

# plinder0
PLINDER aims to overcome
limitations found in existing datasets, such as
size, diversity, and information leakage that
can skew method evaluations.

# doibio1
recently we downloaded the plinder dataset and
looked up one of the structures doctor ness had
published in the PDB and noticed that there
was no citation information for the structures.

# discord
we contacted the PLINDER team via their discord
and they said we should download it from the PDB.

# doibio
In order to assist the community and
accellerate research we present
Plinderp, website and
database of citations, metadata links to
papers and in some cases full text of
papers for all the entries in Plinder

# plinderp
In addition we provide a Python package,
plinderpdoibio.

# website
For this hackathon we developed a number of different
outputs.
Number one, we developed a new                      
website, plinderp dee oh eye dot bio.  On this
website we have collected citation links for all the
entries in the Plinder dataset.

# doibio0
You can visit https colon slash slash plinderp dot dee oh eye dot bio slash one ee are em for information on one ee are em, a beta-lactamase enzyme in Escherichia coli that provides penicillin resistance. The entry includes links to the full Plinder entry, PubMed citation information, and the DOI for online access.

# tem
In this case the full text of the
TEM beta-lactamase paper, which was found as an
alternate version of the paper downloaded from
Simon Fraser University in Canada.

# api
we also developed an API for Plinderp dot dee oh eye dot bio
that can be found at https colon slash slash plinderp dot dee
oh eye dot bio slash api slash v1
and can be queried using curl

# plinderpdoibio
we also developed a Python package that provides
easy access to the Plinderp dataset.  It is hosted
on PyPi and can be installed with "pip install Plinderp dee oh eye bio"
It also provides a fast cached copy of the original Plinder
dataset to allow for easier access to this vital community
dataset.

# llama32
for this hackathon we are focusing on the
Reducing Barriers for Llama Developers pillar.
In our work in hackathons for lab lab dot ai this
year we have noticed a lack of support for
developers in the new emerging field of
Artificial General Intelligence for Structural
Biology, a field that requires vast amounts of
data.

# llama321
Developing with LLMs in this space is
complex with many challenges including data
preparation and evaluation.  Many of the papers
in the scientific literature are difficult for
automated tools to access, and breaking down
barriers in this field could help accellerate
research and science into this extremely
important area.

# tem8
for our demo, we use Llama three dot two to
analyze all the images from the TEM paper.
These images are all provided in base64
encoded format to help developers easy
pass this information into Llama three dot two.

# llama-output
We then ask Llama a question about the binding
site of this protein.  The output of the LLM
looks quite reasonable and we feel this approach
is worth pursuing further.
