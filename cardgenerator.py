from win32com.client import Dispatch

ps = Dispatch(r"Photoshop.Application")
file_path = r'C:\Users\jorge\Projetos\Chaos-Card-Generator\PS_templates\ps_template.psd'


docRef = ps.Open(file_path)
ps.Visible = False

card_name = docRef.ArtLayers['name']
card_name.TextItem.contents = 'Test Name'



ps.Quit()