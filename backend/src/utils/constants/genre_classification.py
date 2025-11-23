import torch

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

genre_classification_output = [{'score': 0.878203809261322, 'label': 'pop'}, {'score': 0.05743027478456497, 'label': 'disco'}, {'score': 0.022425798699259758, 'label': 'reggae'}, {'score': 0.01588517799973488, 'label': 'hiphop'}, {'score': 0.0055113728158175945, 'label': 'rock'}, {'score': 0.005201443564146757, 'label': 'classical'}, {'score': 0.00443338043987751, 'label': 'country'}, {'score': 0.004057861864566803, 'label': 'jazz'}, {'score': 0.004044713452458382, 'label': 'metal'}, {'score': 0.0028061410412192345, 'label': 'blues'}]