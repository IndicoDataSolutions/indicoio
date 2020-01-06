from pathlib import Path
from typing import Union

from .base import IPAObject



class DocumentBuilder(IPABuilder):
    def __init__(self, client: IPARequestClient, *, document: Document)
class Document(IPAObject):
    def __init__(self, *, filepath: Union[str, Path]):
        super().__init__(filepath=filepath)



from indicoio import (
    IndicoClient,
    ModelGroupClient,
    DatasetClient,
    DocumentClient
)

indico_client = IndicoClient()

# Get Resource Clients
dataset_client = indico_client.get_client(DatasetClient)
model_group_client = indico_client.get_client(ModelGroupClient)
document_client = indico_client.get_client(DocumentClient)

# Create Resources
document = document_client.new(filepath="/path/to/file").create()
dataset = (
    dataset_client.new(name="dataset name")
    .add_files(document)
    .create()
)

model_group = model_group_client.new(
    name="model group name",
    dataset_id=dataset.id,
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
document = document_client.new(filepath="/path/to/file").create()
jsonstring = document_client.pdfextraction(document)