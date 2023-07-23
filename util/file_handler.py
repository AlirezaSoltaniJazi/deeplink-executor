import pandas as pd

from model.read_file_model import DataClassReadFromFile


def read_from_file(file: str, sheet_name: str):
    file_extension = file.split('.')[2]
    print(f'File type: {file_extension}')
    if file_extension == 'csv':
        file_data = pd.read_csv(file)
    elif file_extension == 'xlsx':
        file_data = pd.read_excel(file, sheet_name=sheet_name)
    else:
        raise TypeError('Wrong file type, pls enter only csv or xlsx file.')
    excel_data_count = file_data.count()
    print('File data count: %s', excel_data_count)

    # options: ('dict', list, 'series', 'split', 'records', 'index')
    data = file_data.to_dict('records')
    final_data = []
    for datum in data:
        print('datum.Deeplink:', datum['Deeplink'])
        name = datum.get('Name')
        deeplink = datum.get('Deeplink')
        model_data_receiver = DataClassReadFromFile(name, deeplink)
        print('model_data_receiver.deeplink:', model_data_receiver.deeplink)
        final_data.append(model_data_receiver)
    print('final_data:', final_data)
    return final_data, excel_data_count
