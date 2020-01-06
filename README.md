# Indico IPA platform API
### A python client library for the [Indico IPA Platform](https://app.indico.io/).

# Installation
--------------
From PyPI:
```bash
pip3 install indicoio
```

From source:
```bash
git clone https://github.com/IndicoDataSolutions/indicoio-py.git
python3 setup.py install
```

Running in a Docker container:
```
docker build -t indicoio .
docker run -it indicoio bash
```

# Getting Started

First, download an API token from your [user dashboard](https://app.indico.io/auth/user), and save the downloaded file as `indico_api_token.txt` in either your home directory or working directory.

## API Examples
```python3
from indicoio import IndicoClient, ModelGroupClient, DatasetClient

# Get Resource Clients
dataset_client = indico_client.get_client(DatasetClient)
model_group_client = indico_client.get_client(ModelGroupClient)

# Create Resources
dataset = (
    dataset_client.new(name="dataset name")
    .add_files("path_to_file", "path_to_file", "path_to_file")
    .create()
)

model_group = model_group_client.new(
    name="model group name",
    dataset_id=dataset["id"],
    source_column_id=dataset.datacolumns[0].id,
    target_labelset_id=dataset.labelsets[0].id,
).create()

# Train
model_group_client.train(model_group)
model_group_client.wait(model_group)

# Load & Predict
model_group_client.load(model_group)
model_group_client.predict(model_group, data=["some", "input", "text"])

# Delete Resources
model_group_client.delete(model_group)
dataset_client.delete(dataset)

# PDFExtraction Results
document = Document("filepath")
doc_client = indico_client.api_client(DocumentClient)
jsonstring = doc_client.pdfextraction(document)
```