from pprint import pprint
import csv
import gzip
import pandas as pd

if __name__=="__main__":
    # From http://ec.europa.eu/eurostat/statistics-explained/index.php/Tutorial:Country_codes_and_protocol_order
    eu = ["BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR",
          "IT", "CY", "LV", "LT", "LU", "HU", "MT", "NL", "AT", "PL", "PT",
          "RO", "SI", "SK", "FI", "SE", "UK"]

    data = {country: {} for country in eu}

    le = csv.reader(gzip.open("demo_mlexpec.tsv.gz", "rt"), delimiter="\t")
    for row in le:
        unit, sex, age, geo = row[0].split(",")
        if sex == "T" and age == "Y1" and geo in eu:
            data[geo]["le"] = \
                "".join([c for c in row[3] if c.isdigit() or c == "."])

    # hle = csv.reader(gzip.open("hlth_hlye.tsv.gz", "rt"), delimiter="\t")
    # for row in hle:
    #     code, geo = row[0].split(",")
    #     #age = code.split("_")[1].strip()
    #     if code == "F_0_DFLE" and geo in eu:
    #         data[geo]["hle_f"] = \
    #             "".join([c for c in row[3] if c.isdigit() or c == "."])
    #     if code == "M_0_DFLE" and geo in eu:
    #         data[geo]["hle_m"] = \
    #             "".join([c for c in row[3] if c.isdigit() or c == "."])


    bme = csv.reader(gzip.open("hlth_ehis_bm1e.tsv.gz", "rt"), delimiter="\t")
    bme_header = next(bme)
    for row in bme:
        unit,bmi,isced11,sex,age,time = row[0].split(",")
        if bmi.strip() == "BMI_GE30" and time.strip() == "2014"\
           and sex.strip() == "T" and age.strip() == "TOTAL":
            #print(bmi, time)
            for i, field in enumerate(row):
                geo = bme_header[i].strip()
                if geo in eu:
                    data[geo]["obese"] = \
                        "".join([c for c in field if c.isdigit() or c == "."])

    sk = csv.reader(gzip.open("hlth_ehis_sk1e.tsv.gz", "rt"), delimiter="\t")
    sk_header = next(sk)
    for row in sk:
        unit,smoking,isced11,sex,age,time = row[0].split(",")
        if smoking.strip() == "SM_CUR" and time.strip() == "2014"\
           and sex.strip() == "T" and age.strip() == "Y_GE18":
            #print(bmi, time)
            for i, field in enumerate(row):
                geo = sk_header[i].strip()
                if geo in eu:
                    data[geo]["sk"] = \
                        "".join([c for c in field if c.isdigit() or c == "."])

    fv = csv.reader(gzip.open("hlth_ehis_fv3e.tsv.gz", "rt"), delimiter="\t")
    fv_header = next(fv)
    for row in fv:
        unit,n_portion,isced11,sex,age,time = row[0].split(",")
        if n_portion.strip() == "GE5" and time.strip() == "2014"\
           and sex.strip() == "T" and age.strip() == "TOTAL":
            #print(bmi, time)
            for i, field in enumerate(row):
                geo = fv_header[i].strip()
                if geo in eu:
                    data[geo]["fv"] = \
                        "".join([c for c in field if c.isdigit() or c == "."])


    ex = csv.reader(gzip.open("hlth_ehis_pe2e.tsv.gz", "rt"), delimiter="\t")
    ex_header = next(ex)
    for row in ex:
        unit,duration,isced11,sex,age,time = row[0].split(",")
        if duration.strip() == "MN_GE150" and time.strip() == "2014"\
           and sex.strip() == "T" and age.strip() == "TOTAL":
            #print(bmi, time)
            for i, field in enumerate(row):
                geo = ex_header[i].strip()
                if geo in eu:
                    data[geo]["ex"] = \
                        "".join([c for c in field if c.isdigit() or c == "."])

    # US life expectancy published from birth -- subtracted 1 so it's comparable
    # to EU 1YR expectancy.
    data["US"] = {"sk": 15.5, "obese": 37.7, "le": 77.7, "fv": 10, "ex": 51.7}
    df = pd.DataFrame(data).transpose()
    df.index.name = "country"
    df.to_csv("euro-health.csv")
