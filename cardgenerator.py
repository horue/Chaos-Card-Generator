from win32com.client import Dispatch

ps = Dispatch(r"Photoshop.Application")
file_path = r'C:\Users\jorge\Projetos\Chaos-Card-Generator\PS_templates\ps_template.psd'


docRef = ps.Open(file_path)
group1_name = 'Criatura'

group = docRef.LayerSets[group1_name]


card_name = group.ArtLayers['namea']
card_name.TextItem.Contents = 'Artilharia de Batalha'



