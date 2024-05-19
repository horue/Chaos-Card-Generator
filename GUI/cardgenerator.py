from win32com.client import Dispatch
import PIL

ps = Dispatch(r"Photoshop.Application")
file_path = r'C:\Users\jorge\Projetos\Chaos-Card-Generator\PS_templates\ps_template.psd'
docRef = ps.Open(file_path)

def save_temp():
    # Configurar as opções de salvamento para PNG
    png_options = Dispatch("Photoshop.PNGSaveOptions")
    png_options.Interlaced = False
    
    output_path = "C:\\Users\\jorge\\Desktop\\arquivo_temp.png"
    
    # Salvar o documento sem interação do usuário
    docRef.Save()
    
    # Exportar o documento como PNG no caminho especificado
    docRef.Export(output_path, 6, png_options)



def change_name(new_name=''): 
    group_name = 'Criatura'

    group = docRef.LayerSets[group_name]

    if new_name == '':
        pass
    else:
        card_name = group.ArtLayers['namea']
        card_name.TextItem.Contents = new_name

def change_effect(new_effect=''):
    group_name = 'Criatura'

    group = docRef.LayerSets[group_name]

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

