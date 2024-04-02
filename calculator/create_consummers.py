import pandas as pd
import os
import django
import sys

current_directory = os.path.dirname(os.path.realpath(__file__))

project_directory = os.path.abspath(os.path.join(current_directory, '..'))

sys.path.append(project_directory)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from calculator.models import Consumer, RegrasDeDesconto

excel_file = os.path.join(os.path.dirname(__file__), '..', 'consumers.xlsx')



def import_data_from_excel(excel_file):
    df = pd.read_excel(excel_file, dtype=str)  

    for index, row in df.iterrows():
        name = row['Nome']
        document = row['Documento']
        city = row['Cidade']
        state = row['Estado']
        consumption = row['Consumo(kWh)']
        distributor_tax = row['Tarifa da Distribuidora']
        
        # Encontre ou crie a regra de desconto apropriada
        consumer_type = row['Tipo']
        cover_value = row['Cobertura(%)']
        
        discount_rule = RegrasDeDesconto.objects.get(consumer_type=consumer_type.upper(), cover_value=f'{cover_value}%')
        try:
            consumer = Consumer.objects.create(
                name=name,
                document=document,
                city=city,
                state=state,
                consumption=consumption,
                distributor_tax=distributor_tax,
                discount_rule=discount_rule
            )
            print(f"Consumer {name} criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar o Consumer {name}: {str(e)}")

if __name__ == "__main__":
    import_data_from_excel(excel_file)