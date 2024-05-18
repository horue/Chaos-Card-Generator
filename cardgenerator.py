from win32com.client import Dispatch
import PIL

ps = Dispatch(r"Photoshop.Application")
file_path = r'C:\Users\jorge\Projetos\Chaos-Card-Generator\PS_templates\ps_template.psd'
docRef = ps.Open(file_path)


def change_name(): 
    group_name = 'Criatura'

    group = docRef.LayerSets[group_name]

    new_name = input('Qual o novo nome da carta? ')
    if new_name == '':
        pass
    else:
        card_name = group.ArtLayers['namea']
        card_name.TextItem.Contents = new_name

def change_effect():
    group_name = 'Criatura'

    group = docRef.LayerSets[group_name]

    new_effect = input('Qual o novo efeito da carta? ')
    if new_effect == '':
        pass
    else:
        card_name = group.ArtLayers['effect']
        card_name.TextItem.Contents = new_effect

def change_mana():
    group_name = 'Criatura'
    group = docRef.LayerSets[group_name]

    new_mana = input('Qual o novo custo de mana? ')
    if new_mana == '':
        pass
    else:
        card_config = group.ArtLayers['mana']
        card_config.TextItem.Contents = new_mana

def change_power():
    group_name = 'Criatura'
    group = docRef.LayerSets[group_name]

    new_power = input('Qual a nova força? ')
    if new_power == '':
        pass
    else:
        card_config = group.ArtLayers['atk']
        card_config.TextItem.Contents = new_power



change_name()
change_effect()
change_mana()
change_power()



