from moeda.models import Moeda

def run():
    result = Moeda.objects.all()
    print(result)