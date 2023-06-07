from .models import District


def getDistrict(commumne_id):
    district = District.objects.raw('''
    SELECT 
           id, name 

        FROM surveys_district 

        where commune_id = %s;
    ''',[1]
                                    )

    print(district.query)
    return district