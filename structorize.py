import csv
import zipsetter

IL = []
registration, district_wise, principal, groupwise = {}, {}, {}, {}


def structurize(fname):
    """
        This function is for structurizing our data.
    """
    with open(fname, encoding='cp1252') as f:
        fo = csv.DictReader(f)
        for i in fo:
            """
             - this if function will check all entities and filter out
               companies into their respective "AUTHORIZED_CAP" Group.
            """
            if(i['AUTHORIZED_CAP'].isdigit()):
                IL.append(int(i['AUTHORIZED_CAP']))

            """
             - this trick will split year of registration
               from 'DATE_OF_REGISTRATION'.
            """

            if(i['DATE_OF_REGISTRATION'] != 'NA'):
                year = i['DATE_OF_REGISTRATION'].split("-")

                """
                 - This if loop will only allows entities
                   from year 2015 to 2020 Registration Year
                 - Count the "PRINCIPAL_BUSINESS_ACTIVITY"
                   for each year respectevely.
                 - store it in a dict i.e. `principle:{year:{activity:count}}`
                 - this trick will make code more dynamic
                   and reduce the time complexity.
                """
                if(15 <= int(year[2]) < 20):
                    key_year = 2000 + int(year[2])
                    activity = i['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']
                    if(not principal.get(key_year)):
                        principal[key_year] = {activity: 1}
                    else:
                        if(not principal[key_year].get(activity)):
                            principal[key_year][activity] = 1
                        else:
                            principal[key_year][activity] += 1

                """
                 - Only allows the entities of registration year 2015.
                 - For extraction of zip code from address and search
                   it into `zip_code` dictionary.
                 - Count district-wise number of companies
                   register in year 2015
                """
                if(int(year[2]) == 15):
                    z = i["Registered_Office_Address"]
                    zips = str(z[-6:len(z)])
                    if(zips.isdigit()):
                        if(zipsetter.zip_code.get(zips)):
                            z = zipsetter.zip_code[zips]
                            if(not district_wise.get(z)):
                                district_wise[zipsetter.zip_code[zips]] = 1
                            else:
                                district_wise[zipsetter.zip_code[zips]] += 1
                """
                 - Count Companies register by thier respective years
                   from year 2000 to 2020.
                """
                if(0 <= int(year[2]) < 21):
                    year = 2000 + int(year[2])
                    if(not registration.get(year)):
                        registration[year] = 1
                    else:
                        registration[year] += 1
        sorted(registration)
    return([IL, registration, district_wise])
