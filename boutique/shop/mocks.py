import requests
 
# l'ecoscore est stocké dans une constante et sera réutilisé dans nos tests
ECOSCORE_GRADE = 'd'
 
def mock_openfoodfact_success(self, method, url):
    def monkey_json():
        return {
            'product': {
            'ecoscore_grade': ECOSCORE_GRADE
            }
        }
 
    response = requests.Response()
    response.status_code = 200
    response.json = monkey_json
    return response