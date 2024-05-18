from win32com.client import Dispatch
import PIL

ps = Dispatch(r"Photoshop.Application")
file_path = r'C:\Users\jorge\Projetos\Chaos-Card-Generator\PS_templates\ps_template.psd'
docRef = ps.Open(file_path)


def change_name(): 
    group1_name = 'Criatura'

    group = docRef.LayerSets[group1_name]

    newname = input('Qual o novo nome da carta?')
    card_name = group.ArtLayers['namea']
    card_name.TextItem.Contents = newname

change_name()



